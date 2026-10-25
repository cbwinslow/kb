"""Zotero library watcher daemon for automatic PDF ingestion into KB."""

from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from pathlib import Path
from typing import Any

from kb.zotero.reader import ZoteroItem, ZoteroReader

logger = logging.getLogger(__name__)

DEFAULT_STATE_FILE = Path("data/.zotero_sync_state.json")


class ZoteroWatcher:
    """Watches local Zotero library for new papers and attachments and triggers ingestion."""

    def __init__(
        self,
        data_dir: Path | str | None = None,
        poll_interval: float = 10.0,
        state_file: Path | str | None = None,
        reader: ZoteroReader | None = None,
    ) -> None:
        self.reader = reader or ZoteroReader(data_dir=data_dir)
        self.poll_interval = poll_interval
        self.state_file = Path(state_file) if state_file else DEFAULT_STATE_FILE
        self._state: dict[str, Any] = self._load_state()

    @property
    def state(self) -> dict[str, Any]:
        """Returns a read-only copy of the internal sync state."""
        return dict(self._state)

    def _load_state(self) -> dict[str, Any]:
        """Loads sync state from disk or initializes defaults."""
        if self.state_file.exists():
            try:
                with open(self.state_file, encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning("Could not read Zotero sync state file: %s", e)

        return {
            "last_mtime": 0.0,
            "processed_item_keys": [],
        }

    def _save_state(self) -> None:
        """Persists sync state to disk atomically."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        tmp_file = self.state_file.with_suffix(".tmp")
        try:
            with open(tmp_file, "w", encoding="utf-8") as f:
                json.dump(self._state, f, indent=2)
            tmp_file.replace(self.state_file)
        except Exception as e:
            logger.error("Failed to save Zotero sync state: %s", e)

    def check_for_new_items(self) -> list[ZoteroItem]:
        """Checks if zotero.sqlite has been modified and finds un-processed PDF items."""
        sqlite_path = self.reader.sqlite_path
        if not sqlite_path or not sqlite_path.exists():
            return []

        try:
            mtime = sqlite_path.stat().st_mtime
        except OSError:
            return []

        last_mtime = float(self._state.get("last_mtime", 0.0))
        processed_keys = set(self._state.get("processed_item_keys", []))

        # If file hasn't been modified since last check, skip
        if mtime <= last_mtime:
            return []

        # File modified or initial run: query items from Zotero
        items = self.reader.get_items()
        new_items: list[ZoteroItem] = []

        for item in items:
            if item.key in processed_keys:
                continue

            # Must have at least one existing PDF attachment
            pdf_attachments = [
                p for p in item.attachment_paths if p.suffix.lower() == ".pdf" and p.exists()
            ]
            if pdf_attachments:
                new_items.append(item)

        self._state["last_mtime"] = mtime
        self._save_state()
        return new_items

    async def process_item(
        self,
        item: ZoteroItem,
        ingest_fn: Callable[..., Any] | None = None,
    ) -> bool:
        """Ingests a new Zotero item's PDF attachment and marks the key as processed."""
        pdf_attachments = [
            p for p in item.attachment_paths if p.suffix.lower() == ".pdf" and p.exists()
        ]
        if not pdf_attachments:
            return False

        pdf_path = pdf_attachments[0]
        citekey = item.citekey or item.key

        logger.info(
            "Auto-ingesting Zotero item '%s' (%s) from %s",
            item.title,
            citekey,
            pdf_path,
        )

        try:
            if ingest_fn is not None:
                res = ingest_fn(
                    pdf_path=pdf_path,
                    citekey=citekey,
                    title=item.title,
                    authors=item.creators,
                    year=item.year,
                )
                if asyncio.iscoroutine(res):
                    await res
            else:
                from kb.cli import async_ingest

                await async_ingest(
                    pdf_path=pdf_path,
                    citekey=citekey,
                    title=item.title,
                    authors=item.creators,
                    year=item.year,
                )

            # Record success in state
            processed_keys: list[str] = self._state.setdefault("processed_item_keys", [])
            if item.key not in processed_keys:
                processed_keys.append(item.key)
            self._save_state()
            return True
        except Exception as e:
            logger.error("Error auto-ingesting item %s: %s", citekey, e)
            return False

    async def run_once(
        self,
        ingest_fn: Callable[..., Any] | None = None,
    ) -> int:
        """Runs a single polling cycle. Returns the number of items successfully ingested."""
        new_items = self.check_for_new_items()
        if not new_items:
            return 0

        ingested_count = 0
        for item in new_items:
            success = await self.process_item(item, ingest_fn=ingest_fn)
            if success:
                ingested_count += 1

        return ingested_count

    async def watch(
        self,
        stop_event: asyncio.Event | None = None,
        ingest_fn: Callable[..., Any] | None = None,
    ) -> None:
        """Continuously watches Zotero library until stop_event is set or cancelled."""
        logger.info(
            "Starting Zotero watcher daemon (poll interval: %.1fs, database: %s)",
            self.poll_interval,
            self.reader.sqlite_path,
        )
        while True:
            if stop_event and stop_event.is_set():
                break

            try:
                count = await self.run_once(ingest_fn=ingest_fn)
                if count > 0:
                    logger.info("Zotero watcher successfully ingested %d new papers.", count)
            except Exception as e:
                logger.error("Unexpected error in Zotero watcher cycle: %s", e)

            try:
                await asyncio.sleep(self.poll_interval)
            except asyncio.CancelledError:
                logger.info("Zotero watcher stopped.")
                break
