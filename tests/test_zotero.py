"""Unit tests for Zotero SQLite reader and Better BibTeX citekey synchronization."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from kb.zotero.bbt import BetterBibTeXParser
from kb.zotero.reader import ZoteroReader


@pytest.fixture
def mock_zotero_dir(tmp_path: Path) -> Path:
    """Creates a mock Zotero data directory with a populated zotero.sqlite database."""
    db_path = tmp_path / "zotero.sqlite"
    storage_dir = tmp_path / "storage" / "MOCKKEY1"
    storage_dir.mkdir(parents=True, exist_ok=True)
    pdf_file = storage_dir / "miller2005.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 mock content")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Zotero schema tables
    cursor.executescript("""
    CREATE TABLE itemTypes (itemTypeID INTEGER PRIMARY KEY, typeName TEXT);
    INSERT INTO itemTypes VALUES (1, 'journalArticle'), (2, 'attachment'), (3, 'note');

    CREATE TABLE fields (fieldID INTEGER PRIMARY KEY, fieldName TEXT);
    INSERT INTO fields VALUES
        (1, 'title'), (2, 'date'), (3, 'DOI'), (4, 'url'), (5, 'abstractNote'), (6, 'extra');

    CREATE TABLE itemDataValues (valueID INTEGER PRIMARY KEY, value TEXT);
    INSERT INTO itemDataValues VALUES
        (1, 'A Derivation of the Pythagorean Expectation for Baseball'),
        (2, '2005-09-01'),
        (3, '10.1000/mock.doi'),
        (4, 'https://arxiv.org/abs/math/0509698'),
        (5, 'We derive the Pythagorean expectation using Weibull distributions.'),
        (6, 'Citation Key: miller2005');

    CREATE TABLE items (
        itemID INTEGER PRIMARY KEY,
        itemTypeID INTEGER,
        dateAdded TEXT,
        dateModified TEXT,
        key TEXT
    );
    INSERT INTO items VALUES
        (10, 1, '2024-01-01', '2024-01-02', 'ITEMKEY1'),
        (11, 2, '2024-01-01', '2024-01-02', 'MOCKKEY1');

    CREATE TABLE itemData (itemID INTEGER, fieldID INTEGER, valueID INTEGER);
    INSERT INTO itemData VALUES
        (10, 1, 1),
        (10, 2, 2),
        (10, 3, 3),
        (10, 4, 4),
        (10, 5, 5),
        (10, 6, 6);

    CREATE TABLE creators (creatorID INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT);
    INSERT INTO creators VALUES (1, 'Steven J.', 'Miller');

    CREATE TABLE itemCreators (
        itemID INTEGER, creatorID INTEGER, creatorTypeID INTEGER, orderIndex INTEGER
    );
    INSERT INTO itemCreators VALUES (10, 1, 1, 0);

    CREATE TABLE collections (
        collectionID INTEGER PRIMARY KEY, collectionName TEXT, parentCollectionID INTEGER, key TEXT
    );
    INSERT INTO collections VALUES (1, 'Baseball Sabermetrics', NULL, 'COLLKEY1');

    CREATE TABLE collectionItems (collectionID INTEGER, itemID INTEGER);
    INSERT INTO collectionItems VALUES (1, 10);

    CREATE TABLE itemAttachments (
        itemID INTEGER PRIMARY KEY,
        parentItemID INTEGER,
        contentType TEXT,
        path TEXT
    );
    INSERT INTO itemAttachments VALUES (11, 10, 'application/pdf', 'storage:miller2005.pdf');
    """)

    conn.commit()
    conn.close()
    return tmp_path


def test_zotero_reader_schema_extraction(mock_zotero_dir: Path) -> None:
    """Verifies reading items, creators, collections, and attachments from Zotero SQLite."""
    reader = ZoteroReader(data_dir=mock_zotero_dir)

    # 1. Test collections
    collections = reader.get_collections()
    assert collections == ["Baseball Sabermetrics"]

    # 2. Test items
    items = reader.get_items()
    assert len(items) == 1
    item = items[0]
    assert item.key == "ITEMKEY1"
    assert item.item_type == "journalArticle"
    assert item.title == "A Derivation of the Pythagorean Expectation for Baseball"
    assert item.creators == ["Steven J. Miller"]
    assert item.year == 2005
    assert item.doi == "10.1000/mock.doi"
    assert item.citekey == "miller2005"
    assert item.collections == ["Baseball Sabermetrics"]
    assert len(item.attachment_paths) == 1
    assert item.attachment_paths[0].name == "miller2005.pdf"

    # 3. Test filtering by collection
    matched = reader.get_items(collection_name="Baseball Sabermetrics")
    assert len(matched) == 1

    empty = reader.get_items(collection_name="Nonexistent")
    assert len(empty) == 0


def test_better_bibtex_parser() -> None:
    """Verifies Better BibTeX citekey extraction, fallback generation, and .bib parsing."""
    parser = BetterBibTeXParser()

    # Extra field extraction
    assert parser.extract_citekey_from_extra("Citation Key: albert2024") == "albert2024"
    assert parser.extract_citekey_from_extra("bibtex: jensen2009bayes") == "jensen2009bayes"
    assert parser.extract_citekey_from_extra("Random notes without citekey") is None

    # Fallback generator
    fb1 = parser.generate_fallback_citekey(
        first_author="Steven J. Miller",
        year=2005,
        title="A Derivation of the Pythagorean Expectation",
    )
    assert fb1 == "miller2005derivation"

    fb2 = parser.generate_fallback_citekey(
        first_author="Bill James",
        year=1982,
        title="The Baseball Abstract",
    )
    assert fb2 == "james1982baseball"

    # BibTeX file parsing
    bib_content = """
    @article{miller2005,
      title = {A Derivation of the Pythagorean Expectation},
      author = {Miller, Steven J.},
      year = {2005},
      doi = {10.1000/mock}
    }

    @book{albert2024,
      title = {Analyzing Baseball Data with R},
      author = {Albert, Jim and Marchi, Max},
      year = {2024}
    }
    """
    parsed = parser.parse_bibtex_file(bib_content)
    assert "miller2005" in parsed
    assert parsed["miller2005"]["title"] == "A Derivation of the Pythagorean Expectation"
    assert parsed["miller2005"]["doi"] == "10.1000/mock"
    assert "albert2024" in parsed
    assert parsed["albert2024"]["_type"] == "book"
