"""Unit tests for in-place corpus formula repair engine."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from kb.math.repair import CorpusFormulaRepairer, CorpusRepairGradeResult, RepairResult
from kb.storage.database import DatabaseManager
from kb.storage.models import Document, Formula


@pytest.fixture
def repairer() -> CorpusFormulaRepairer:
    return CorpusFormulaRepairer()


@pytest.mark.asyncio
async def test_repair_corpus_mocked(repairer: CorpusFormulaRepairer) -> None:
    session = AsyncMock()

    # Create mock invalid formula that can be repaired by Unicode normalization
    mock_formula = MagicMock()
    mock_formula.id = "f-123"
    mock_formula.chunk_id = "c-123"
    mock_formula.raw_latex = r"θ = α + β"
    mock_formula.sanitized_latex = r"θ = α + β"
    mock_formula.is_valid = False
    mock_formula.is_equality = False
    mock_formula.symbols = []

    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = [mock_formula]
    session.execute.return_value = result_mock

    # Test dry run
    res_dry = await repairer.repair_corpus(batch_size=10, dry_run=True, session=session)
    assert isinstance(res_dry, RepairResult)
    assert res_dry.total_scanned == 1
    assert res_dry.newly_recovered == 1
    assert res_dry.updated_records == 0
    assert res_dry.dry_run is True

    # Test non-dry run
    res_live = await repairer.repair_corpus(batch_size=10, dry_run=False, session=session)
    assert res_live.total_scanned == 1
    assert res_live.newly_recovered == 1
    assert res_live.updated_records == 1
    assert res_live.dry_run is False
    assert session.commit.called


@pytest.mark.asyncio
async def test_repair_and_grade_corpus_live_db() -> None:
    """Verifies that repair_and_grade_corpus updates scores and letter grades in SQLite."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_repair_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc = Document(id="doc_test", citekey="test2024", title="Test Paper")
        session.add(doc)
        await session.flush()

        # 1. Valid formula needing grade evaluation
        f1 = Formula(
            id="f_valid",
            document_id="doc_test",
            citekey="test2024",
            raw_latex="E = m c^2",
            sanitized_latex="E = m c^2",
            is_valid=True,
            validation_status=None,
        )
        # 2. Invalid formula that can be repaired
        f2 = Formula(
            id="f_repairable",
            document_id="doc_test",
            citekey="test2024",
            raw_latex=r"\mathrm{wOBA} = 0.69 \cdot \mathrm{uBB}",
            sanitized_latex=r"\mathrm{wOBA} = 0.69 \cdot \mathrm{uBB}",
            is_valid=False,
            validation_status=None,
        )
        session.add_all([f1, f2])
        await session.commit()

    repairer = CorpusFormulaRepairer()
    async with db.get_session() as session:
        res = await repairer.repair_and_grade_corpus(
            batch_size=10, dry_run=False, session=session
        )

    assert isinstance(res, CorpusRepairGradeResult)
    assert res.total_scanned == 2
    assert res.updated_records == 2
    assert len(res.evaluated_grades) > 0
    assert len(res.evaluated_statuses) > 0

    # Verify database was updated
    async with db.get_session() as session:
        from sqlalchemy import select

        f1_db = (
            await session.execute(select(Formula).where(Formula.id == "f_valid"))
        ).scalar_one()
        assert f1_db.validation_status is not None
        assert f1_db.validation_score is not None
        assert f1_db.validation_details is not None
        assert "letter_grade" in f1_db.validation_details

    await db.close()
