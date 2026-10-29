"""Hermetic unit tests for legacy homelab migration adapter, vector parsing, and citekey."""

from __future__ import annotations

import uuid

import pytest
from sqlalchemy import text

from kb.storage import (
    DatabaseManager,
    LegacyMigrationAdapter,
    MigrationDocCandidate,
    parse_vector,
)


def test_parse_vector_formats() -> None:
    """Verifies that parse_vector handles string representations, sequences, and None values."""
    assert parse_vector(None) is None
    assert parse_vector("") is None
    assert parse_vector("[]") is None

    # String format
    vec_str = "[-0.0522, 0.1234, 0.9876]"
    parsed = parse_vector(vec_str)
    assert parsed is not None
    assert len(parsed) == 3
    assert pytest.approx(parsed[0], 0.0001) == -0.0522
    assert pytest.approx(parsed[2], 0.0001) == 0.9876

    # Sequence format
    seq = [-0.1, 0.2, 0.3]
    assert parse_vector(seq) == seq


def test_synthesize_citekey_rules() -> None:
    """Verifies deterministic citekey synthesis and collision resolution."""
    adapter = LegacyMigrationAdapter(db_manager=None)  # type: ignore[arg-type]
    existing: set[str] = {"existing_key"}

    # 1. ArXiv URL synthesis
    arxiv_candidate = MigrationDocCandidate(
        doc_id="doc1",
        title="Evaluating Throwing Ability",
        source="arxiv",
        url="https://arxiv.org/abs/0705.3257",
        quality=9,
        relevance=10,
    )
    key1 = adapter.synthesize_citekey(arxiv_candidate, None, existing)
    assert key1 == "arxiv_0705_3257"
    assert "arxiv_0705_3257" in existing

    # 2. Collision resolution
    arxiv_candidate_duplicate = MigrationDocCandidate(
        doc_id="doc2",
        title="Evaluating Throwing Ability Part 2",
        source="arxiv",
        url="https://arxiv.org/abs/0705.3257",
        quality=9,
        relevance=10,
    )
    key2 = adapter.synthesize_citekey(arxiv_candidate_duplicate, None, existing)
    assert key2 == "arxiv_0705_3257_2"

    # 3. Author and year in first chunk text
    author_candidate = MigrationDocCandidate(
        doc_id="doc3",
        title="Calculating Position Player WAR",
        source="fangraphs-library",
        url="https://library.fangraphs.com/war",
        quality=8,
        relevance=9,
    )
    chunk_text = (
        "Calculating Position Player WAR, A Complete Example by Neil Weinberg "
        "September 19, 2014. One of the hallmark statistics..."
    )
    key3 = adapter.synthesize_citekey(author_candidate, chunk_text, existing)
    assert "weinberg" in key3
    assert "2014" in key3


@pytest.fixture
def mock_db() -> DatabaseManager:
    """Creates an in-memory SQLite database manager for migration testing."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_migration_{db_id}?mode=memory&cache=shared&uri=true"
    return DatabaseManager(database_url=url, echo=False)


@pytest.mark.asyncio
async def test_legacy_migration_pipeline(mock_db: DatabaseManager) -> None:
    """Verifies end-to-end legacy candidate scanning, dry-run, and migration in SQLite."""
    await mock_db.init_db()

    # Create mock legacy tables in SQLite
    async with mock_db.get_session() as session:
        await session.execute(
            text("""
            CREATE TABLE legacy_docs (
                doc_id TEXT PRIMARY KEY,
                title TEXT,
                source TEXT,
                url TEXT,
                quality INTEGER,
                relevance INTEGER,
                topics TEXT,
                summary TEXT
            );
        """)
        )
        await session.execute(
            text("""
            CREATE TABLE legacy_chunks (
                chunk_id INTEGER PRIMARY KEY,
                position INTEGER,
                doc_id TEXT,
                text TEXT,
                emb_bgem3 TEXT,
                context TEXT
            );
        """)
        )
        await session.execute(
            text("""
            CREATE TABLE legacy_formulas (
                formula_id TEXT PRIMARY KEY,
                doc_id TEXT,
                section TEXT,
                label TEXT,
                latex TEXT
            );
        """)
        )

        # Seed mock candidate 1 (High quality, valid source)
        await session.execute(
            text("""
            INSERT INTO legacy_docs VALUES (
                'doc_good',
                'Win Expectancy Analysis',
                'sabr-journal',
                'https://sabr.org/journal/win_expectancy',
                9,
                9,
                '["baseball", "statistics"]',
                'Analysis of win expectancy in baseball.'
            );
        """)
        )
        # Seed mock candidate 2 (Low quality, should be filtered out)
        await session.execute(
            text("""
            INSERT INTO legacy_docs VALUES (
                'doc_low_quality',
                'Low Quality Scrape',
                'sabr-journal',
                'http://example.com/low',
                4,
                5,
                '[]',
                'Snippet summary.'
            );
        """)
        )
        # Seed mock candidate 3 (Unverified source, should be filtered out)
        await session.execute(
            text("""
            INSERT INTO legacy_docs VALUES (
                'doc_bad_source',
                'Abstract Snippet',
                'harvest-abstract',
                'http://example.com/snippet',
                8,
                8,
                '[]',
                'Abstract snippet.'
            );
        """)
        )

        # Seed chunks for doc_good
        await session.execute(
            text("""
            INSERT INTO legacy_chunks VALUES (
                101,
                0,
                'doc_good',
                'Introduction to Win Expectancy by Tom Tango 2006. Win expectancy measures.',
                '[-0.01, 0.05, 0.12]',
                'Introductory context'
            );
        """)
        )
        await session.execute(
            text("""
            INSERT INTO legacy_chunks VALUES (
                102,
                1,
                'doc_good',
                'The formula for win expectancy: $WE = \\frac{RS^2}{RS^2 + RA^2}$ with RS.',
                '[0.04, -0.02, 0.08]',
                'Formula derivation'
            );
        """)
        )

        # Seed formula for doc_good
        await session.execute(
            text("""
            INSERT INTO legacy_formulas VALUES (
                'form_1',
                'doc_good',
                'Formula derivation',
                'we_eq',
                'WE = \\frac{RS^2}{RS^2 + RA^2}'
            );
        """)
        )

    adapter = LegacyMigrationAdapter(
        db_manager=mock_db,
        doc_table="legacy_docs",
        chunk_table="legacy_chunks",
        formula_table="legacy_formulas",
    )

    # 1. Test scanning candidates
    async with mock_db.get_session() as session:
        candidates = await adapter.scan_candidates(
            session=session,
            min_quality=7,
            min_relevance=7,
        )
        assert len(candidates) == 1
        assert candidates[0].doc_id == "doc_good"

    # 2. Test dry-run migration
    dry_stats = await adapter.migrate_batch(
        min_quality=7,
        min_relevance=7,
        dry_run=True,
    )
    assert dry_stats.dry_run is True
    assert dry_stats.scanned_candidates == 1
    assert dry_stats.migrated_documents == 1
    assert dry_stats.migrated_chunks == 2
    assert dry_stats.migrated_formulas == 1

    # Verify no documents committed yet
    async with mock_db.get_session() as session:
        citekeys = await adapter.get_all_citekeys(session)
        assert len(citekeys) == 0

    # 3. Test live migration
    live_stats = await adapter.migrate_batch(
        min_quality=7,
        min_relevance=7,
        dry_run=False,
    )
    assert live_stats.dry_run is False
    assert live_stats.scanned_candidates == 1
    assert live_stats.migrated_documents == 1
    assert live_stats.migrated_chunks == 2
    assert live_stats.migrated_formulas == 1
    assert live_stats.valid_formulas >= 1

    # 4. Verify persisted records and fields
    async with mock_db.get_session() as session:
        # Check Document
        doc_stmt = text("SELECT citekey, title, year, extra_metadata FROM kb_documents")
        doc_res = await session.execute(doc_stmt)
        row = doc_res.fetchone()
        assert row is not None
        citekey = row[0]
        assert "tango" in citekey
        assert row[1] == "Win Expectancy Analysis"
        assert row[2] == 2006
        assert "doc_good" in row[3]

        # Check Chunks
        chunk_sql = (
            "SELECT chunk_index, citekey, enriched_text, previous_chunk_id, next_chunk_id "
            "FROM kb_chunks ORDER BY chunk_index"
        )
        chunk_res = await session.execute(text(chunk_sql))
        chunks = chunk_res.fetchall()
        assert len(chunks) == 2
        assert chunks[0][0] == 0
        assert chunks[0][1] == citekey
        assert "[Document: Win Expectancy Analysis" in chunks[0][2]
        assert chunks[0][3] is None  # first chunk has no previous
        assert chunks[0][4] is not None  # next chunk id is linked
        assert chunks[1][3] is not None  # second chunk previous is linked

        # Check Formulas
        f_res = await session.execute(
            text("SELECT citekey, sanitized_latex, is_valid FROM kb_formulas")
        )
        formulas = f_res.fetchall()
        assert len(formulas) == 1
        assert formulas[0][0] == citekey
        assert "R_{S}" in formulas[0][1]
        assert bool(formulas[0][2]) is True

    # 5. Test idempotency: re-running scan returns 0 un-imported candidates
    async with mock_db.get_session() as session:
        candidates_after = await adapter.scan_candidates(
            session=session,
            min_quality=7,
            min_relevance=7,
        )
        assert len(candidates_after) == 0

    await mock_db.close()


@pytest.mark.asyncio
async def test_cli_migrate_legacy_dry_run(
    mock_db: DatabaseManager, capsys: pytest.CaptureFixture[str]
) -> None:
    """Verifies that async_migrate_legacy CLI runs dry-run without writing to database."""
    from kb.cli import async_migrate_legacy

    await mock_db.init_db()

    # Create empty public tables in mock_db
    async with mock_db.get_session() as session:
        await session.execute(
            text("""
            CREATE TABLE IF NOT EXISTS documents (
                doc_id TEXT PRIMARY KEY,
                title TEXT,
                source TEXT,
                url TEXT,
                quality INTEGER,
                relevance INTEGER,
                topics TEXT,
                summary TEXT
            );
        """)
        )

    exit_code = await async_migrate_legacy(
        dry_run=True,
        min_quality=7,
        min_relevance=7,
        manager=mock_db,
    )
    assert exit_code == 0

    captured = capsys.readouterr()
    assert "[DRY-RUN]" in captured.out
    assert "Migration Summary:" in captured.out

    await mock_db.close()
