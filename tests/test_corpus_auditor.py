"""Unit tests for CorpusAuditor relational integrity and invariant verification."""

from __future__ import annotations

import uuid

import pytest

from kb.qa.corpus_auditor import CorpusAuditor
from kb.storage.database import DatabaseManager
from kb.storage.models import Chunk, Document, Formula


@pytest.mark.asyncio
async def test_corpus_auditor_healthy_database() -> None:
    """Verifies that CorpusAuditor reports healthy metrics on valid corpus relationships."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_audit_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc = Document(id="doc_1", citekey="nathan2008", title="Physics of Baseball")
        session.add(doc)
        await session.flush()

        chunk = Chunk(
            id="chunk_1",
            document_id="doc_1",
            citekey="nathan2008",
            chunk_index=0,
            raw_text="content",
            enriched_text="content",
        )
        session.add(chunk)

        formula = Formula(
            id="f_1",
            document_id="doc_1",
            citekey="nathan2008",
            raw_latex="v = d / t",
            sanitized_latex="v = d / t",
            is_valid=True,
            validation_status="verified",
            validation_score=95.0,
        )
        session.add(formula)
        await session.commit()

    auditor = CorpusAuditor(db)
    report = await auditor.run_audit()

    assert report.total_documents == 1
    assert report.total_chunks == 1
    assert report.total_formulas == 1
    assert report.orphaned_chunks == 0
    assert report.orphaned_formulas == 0
    assert report.verified_formulas == 1
    assert report.is_healthy is True
    assert report.to_dict()["is_healthy"] is True

    await db.close()


@pytest.mark.asyncio
async def test_corpus_auditor_orphaned_records() -> None:
    """Verifies that CorpusAuditor identifies orphaned records correctly."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_orphan_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        # Add chunk and formula pointing to non-existent document
        chunk = Chunk(
            id="chunk_orphan",
            document_id="doc_missing",
            citekey="missing",
            chunk_index=0,
            raw_text="content",
            enriched_text="content",
        )
        session.add(chunk)

        formula = Formula(
            id="f_orphan",
            document_id="doc_missing",
            citekey="missing",
            raw_latex="x = 1",
            sanitized_latex="x = 1",
            is_valid=False,
            validation_status=None,
        )
        session.add(formula)
        await session.commit()

    auditor = CorpusAuditor(db)
    report = await auditor.run_audit()

    assert report.orphaned_chunks == 1
    assert report.orphaned_formulas == 1
    assert report.unvalidated_formulas == 1
    assert report.is_healthy is False
    assert len(report.violations) >= 2

    await db.close()
