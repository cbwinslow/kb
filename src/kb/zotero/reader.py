"""Zotero SQLite reader for extracting reference metadata, collections, and attachments."""

from __future__ import annotations

import logging
import os
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from kb.zotero.bbt import BetterBibTeXParser

logger = logging.getLogger(__name__)


@dataclass
class ZoteroItem:
    """Represents a reference item extracted from local Zotero library."""

    item_id: int
    key: str
    item_type: str
    title: str
    creators: list[str] = field(default_factory=list)
    year: int | None = None
    doi: str | None = None
    url: str | None = None
    abstract: str | None = None
    extra: str = ""
    citekey: str | None = None
    collections: list[str] = field(default_factory=list)
    attachment_paths: list[Path] = field(default_factory=list)


class ZoteroReader:
    """Discovers and parses local Zotero SQLite library in read-only mode."""

    def __init__(self, data_dir: Path | str | None = None) -> None:
        self.data_dir: Path | None = (
            Path(data_dir).resolve() if data_dir else self.find_zotero_dir()
        )
        self.bbt_parser = BetterBibTeXParser()

    @staticmethod
    def find_zotero_dir() -> Path | None:
        """Attempts to locate the default Zotero data directory across platforms."""
        candidates: list[Path] = []

        # 1. Environment override
        env_dir = os.getenv("ZOTERO_DATA_DIR")
        if env_dir:
            candidates.append(Path(env_dir))

        # 2. Windows default
        userprofile = os.getenv("USERPROFILE")
        if userprofile:
            candidates.append(Path(userprofile) / "Zotero")

        # 3. Unix / macOS defaults
        home = Path.home()
        candidates.append(home / "Zotero")
        candidates.append(home / ".zotero" / "zotero")
        candidates.append(home / "Library" / "Application Support" / "Zotero")

        for c in candidates:
            if (c / "zotero.sqlite").exists():
                return c.resolve()

        return None

    @property
    def sqlite_path(self) -> Path | None:
        """Returns the full path to zotero.sqlite if data_dir is valid."""
        if self.data_dir:
            path = self.data_dir / "zotero.sqlite"
            if path.exists():
                return path
        return None

    def _get_connection(self) -> sqlite3.Connection:
        """Opens a read-only URI connection to zotero.sqlite to prevent database locks."""
        if not self.sqlite_path:
            loc = self.data_dir / "zotero.sqlite" if self.data_dir else "unknown location"
            raise FileNotFoundError(f"Zotero SQLite database not found at {loc}")
        uri = f"file:{self.sqlite_path.as_posix()}?mode=ro"
        conn = sqlite3.connect(uri, uri=True)
        conn.row_factory = sqlite3.Row
        return conn

    def get_collections(self) -> list[str]:
        """Lists all collection names in the Zotero library."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT collectionName FROM collections ORDER BY collectionName ASC;")
            rows = cursor.fetchall()
            return [str(r["collectionName"]) for r in rows]

    def get_items(self, collection_name: str | None = None) -> list[ZoteroItem]:
        """Extracts items with metadata, creators, collections, and linked attachments."""
        with self._get_connection() as conn:
            cursor = conn.cursor()

            # Query base items (excluding attachments and notes)
            query = """
            SELECT
                i.itemID,
                i.key,
                it.typeName as itemType
            FROM items i
            JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
            WHERE it.typeName NOT IN ('attachment', 'note', 'annotation')
            """
            params: list[Any] = []

            if collection_name:
                query += """
                AND i.itemID IN (
                    SELECT ci.itemID
                    FROM collectionItems ci
                    JOIN collections c ON ci.collectionID = c.collectionID
                    WHERE c.collectionName = ?
                )
                """
                params.append(collection_name)

            cursor.execute(query, params)
            base_rows = cursor.fetchall()

            items: list[ZoteroItem] = []
            for row in base_rows:
                item_id = int(row["itemID"])
                key = str(row["key"])
                item_type = str(row["itemType"])

                # Fetch fields (title, date, doi, url, abstract, extra)
                fields = self._fetch_item_fields(conn, item_id)
                creators = self._fetch_item_creators(conn, item_id)
                collections = self._fetch_item_collections(conn, item_id)
                attachments = self._fetch_item_attachments(conn, item_id)

                title = fields.get("title", "Untitled")
                extra = fields.get("extra", "")
                doi = fields.get("DOI")
                url = fields.get("url")
                abstract = fields.get("abstractNote")
                year = self._parse_year(fields.get("date", ""))

                # Extract or generate citekey
                citekey = self.bbt_parser.extract_citekey_from_extra(extra)
                if not citekey:
                    first_author = creators[0] if creators else "Unknown"
                    citekey = self.bbt_parser.generate_fallback_citekey(first_author, year, title)

                item = ZoteroItem(
                    item_id=item_id,
                    key=key,
                    item_type=item_type,
                    title=title,
                    creators=creators,
                    year=year,
                    doi=doi,
                    url=url,
                    abstract=abstract,
                    extra=extra,
                    citekey=citekey,
                    collections=collections,
                    attachment_paths=attachments,
                )
                items.append(item)

            return items

    def _fetch_item_fields(self, conn: sqlite3.Connection, item_id: int) -> dict[str, str]:
        """Fetches key-value field data for an item."""
        cursor = conn.cursor()
        query = """
        SELECT f.fieldName, idv.value
        FROM itemData id
        JOIN fields f ON id.fieldID = f.fieldID
        JOIN itemDataValues idv ON id.valueID = idv.valueID
        WHERE id.itemID = ?;
        """
        cursor.execute(query, (item_id,))
        return {str(r["fieldName"]): str(r["value"]) for r in cursor.fetchall()}

    def _fetch_item_creators(self, conn: sqlite3.Connection, item_id: int) -> list[str]:
        """Fetches creator names for an item ordered by orderIndex."""
        cursor = conn.cursor()
        query = """
        SELECT c.firstName, c.lastName
        FROM itemCreators ic
        JOIN creators c ON ic.creatorID = c.creatorID
        WHERE ic.itemID = ?
        ORDER BY ic.orderIndex ASC;
        """
        cursor.execute(query, (item_id,))
        creators: list[str] = []
        for r in cursor.fetchall():
            first = str(r["firstName"]) if r["firstName"] else ""
            last = str(r["lastName"]) if r["lastName"] else ""
            full = f"{first} {last}".strip()
            if full:
                creators.append(full)
        return creators

    def _fetch_item_collections(self, conn: sqlite3.Connection, item_id: int) -> list[str]:
        """Fetches collection names associated with an item."""
        cursor = conn.cursor()
        query = """
        SELECT c.collectionName
        FROM collectionItems ci
        JOIN collections c ON ci.collectionID = c.collectionID
        WHERE ci.itemID = ?;
        """
        cursor.execute(query, (item_id,))
        return [str(r["collectionName"]) for r in cursor.fetchall()]

    def _fetch_item_attachments(self, conn: sqlite3.Connection, item_id: int) -> list[Path]:
        """Fetches resolved attachment file paths (e.g. PDFs) for an item."""
        cursor = conn.cursor()
        query = """
        SELECT ia.path, i.key
        FROM itemAttachments ia
        JOIN items i ON ia.itemID = i.itemID
        WHERE ia.parentItemID = ? AND ia.contentType = 'application/pdf';
        """
        cursor.execute(query, (item_id,))
        paths: list[Path] = []
        for r in cursor.fetchall():
            raw_path = str(r["path"]) if r["path"] else ""
            item_key = str(r["key"]) if r["key"] else ""
            resolved = self.resolve_attachment_path(raw_path, item_key)
            if resolved and resolved.exists():
                paths.append(resolved)
        return paths

    def resolve_attachment_path(self, raw_path: str, attachment_key: str = "") -> Path | None:
        """Resolves Zotero attachment storage path (storage:filename or absolute path)."""
        if not raw_path:
            return None

        if raw_path.startswith("storage:") and self.data_dir:
            filename = raw_path[len("storage:") :]
            if attachment_key:
                candidate = self.data_dir / "storage" / attachment_key / filename
                if candidate.exists():
                    return candidate
            # Fallback search under storage/
            return self.data_dir / "storage" / filename

        candidate = Path(raw_path)
        if candidate.exists():
            return candidate

        return None

    @staticmethod
    def _parse_year(date_str: str) -> int | None:
        """Extracts 4-digit year from date string."""
        import re

        match = re.search(r"\b(19\d\d|20\d\d)\b", date_str)
        if match:
            return int(match.group(1))
        return None
