"""Unit tests for ZoteroWatcher daemon and auto-ingestion dispatch."""

from __future__ import annotations

import asyncio
import sqlite3
from pathlib import Path
from typing import Any

import pytest

from kb.zotero.watcher import ZoteroWatcher


@pytest.fixture
def mock_zotero_env(tmp_path: Path) -> tuple[Path, Path]:
    """Sets up a mock Zotero directory with a sample PDF item and a state file path."""
    zotero_dir = tmp_path / "Zotero"
    zotero_dir.mkdir()
    db_path = zotero_dir / "zotero.sqlite"

    storage_dir = zotero_dir / "storage" / "MOCKPDFKEY"
    storage_dir.mkdir(parents=True)
    pdf_file = storage_dir / "paper.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 mock paper content")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE itemTypes (itemTypeID INTEGER PRIMARY KEY, typeName TEXT);
    INSERT INTO itemTypes VALUES (1, 'journalArticle'), (2, 'attachment');

    CREATE TABLE fields (fieldID INTEGER PRIMARY KEY, fieldName TEXT);
    INSERT INTO fields VALUES (1, 'title'), (2, 'date'), (3, 'extra');

    CREATE TABLE itemDataValues (valueID INTEGER PRIMARY KEY, value TEXT);
    INSERT INTO itemDataValues VALUES
        (1, 'Autonomous AI Agent Architectures'),
        (2, '2026'),
        (3, 'Citation Key: agent2026');

    CREATE TABLE items (
        itemID INTEGER PRIMARY KEY, itemTypeID INTEGER, dateAdded TEXT, dateModified TEXT, key TEXT
    );
    INSERT INTO items VALUES
        (10, 1, '2026-01-01', '2026-01-02', 'ITEMKEY1'),
        (11, 2, '2026-01-01', '2026-01-02', 'MOCKPDFKEY');

    CREATE TABLE itemData (itemID INTEGER, fieldID INTEGER, valueID INTEGER);
    INSERT INTO itemData VALUES
        (10, 1, 1),
        (10, 2, 2),
        (10, 3, 3);

    CREATE TABLE creators (creatorID INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT);
    INSERT INTO creators VALUES (1, 'Ada', 'Lovelace');

    CREATE TABLE itemCreators (
        itemID INTEGER, creatorID INTEGER, creatorTypeID INTEGER, orderIndex INTEGER
    );
    INSERT INTO itemCreators VALUES (10, 1, 1, 0);

    CREATE TABLE collections (
        collectionID INTEGER PRIMARY KEY, collectionName TEXT, parentCollectionID INTEGER, key TEXT
    );

    CREATE TABLE collectionItems (collectionID INTEGER, itemID INTEGER);

    CREATE TABLE itemAttachments (
        itemID INTEGER PRIMARY KEY, parentItemID INTEGER, contentType TEXT, path TEXT
    );
    INSERT INTO itemAttachments VALUES (11, 10, 'application/pdf', 'storage:paper.pdf');
    """)
    conn.commit()
    conn.close()

    state_file = tmp_path / "sync_state.json"
    return zotero_dir, state_file


def test_watcher_missing_database_graceful(tmp_path: Path) -> None:
    """Verifies that missing zotero.sqlite returns empty list without throwing."""
    non_existent = tmp_path / "does_not_exist"
    watcher = ZoteroWatcher(data_dir=non_existent, state_file=tmp_path / "state.json")
    new_items = watcher.check_for_new_items()
    assert new_items == []


def test_watcher_detects_new_item_and_persists_state(
    mock_zotero_env: tuple[Path, Path],
) -> None:
    """Verifies that watcher detects items with PDFs and remembers state on successive calls."""
    zotero_dir, state_file = mock_zotero_env
    watcher = ZoteroWatcher(data_dir=zotero_dir, state_file=state_file)

    # Initial check: finds 1 item
    new_items = watcher.check_for_new_items()
    assert len(new_items) == 1
    assert new_items[0].key == "ITEMKEY1"
    assert new_items[0].citekey == "agent2026"
    assert state_file.exists()

    # Second check without modifications: returns empty list
    second_check = watcher.check_for_new_items()
    assert second_check == []


@pytest.mark.asyncio
async def test_watcher_process_item_and_run_once(
    mock_zotero_env: tuple[Path, Path],
) -> None:
    """Verifies dispatching ingestion for new items via custom callback."""
    zotero_dir, state_file = mock_zotero_env
    watcher = ZoteroWatcher(data_dir=zotero_dir, state_file=state_file)

    ingested_calls: list[dict[str, Any]] = []

    async def mock_ingest(
        pdf_path: Path,
        citekey: str,
        title: str | None = None,
        authors: list[str] | None = None,
        year: int | None = None,
    ) -> int:
        ingested_calls.append(
            {
                "pdf_path": pdf_path,
                "citekey": citekey,
                "title": title,
                "authors": authors,
                "year": year,
            }
        )
        return 0

    count = await watcher.run_once(ingest_fn=mock_ingest)
    assert count == 1
    assert len(ingested_calls) == 1
    call = ingested_calls[0]
    assert call["citekey"] == "agent2026"
    assert call["title"] == "Autonomous AI Agent Architectures"
    assert call["authors"] == ["Ada Lovelace"]
    assert call["year"] == 2026

    # Verify item is now marked as processed
    assert "ITEMKEY1" in watcher.state["processed_item_keys"]

    # Running again should ingest 0 items
    count_second = await watcher.run_once(ingest_fn=mock_ingest)
    assert count_second == 0


@pytest.mark.asyncio
async def test_watcher_watch_loop_with_stop_event(
    mock_zotero_env: tuple[Path, Path],
) -> None:
    """Verifies that watch() loop runs and stops cleanly when stop_event is set."""
    zotero_dir, state_file = mock_zotero_env
    watcher = ZoteroWatcher(data_dir=zotero_dir, poll_interval=0.05, state_file=state_file)

    stop_event = asyncio.Event()

    async def mock_ingest(**_kwargs: Any) -> int:
        # Stop watcher after first ingestion
        stop_event.set()
        return 0

    watch_task = asyncio.create_task(watcher.watch(stop_event=stop_event, ingest_fn=mock_ingest))
    await asyncio.wait_for(watch_task, timeout=2.0)
    assert stop_event.is_set()
    assert "ITEMKEY1" in watcher.state["processed_item_keys"]
