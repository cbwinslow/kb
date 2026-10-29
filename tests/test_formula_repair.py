"""Unit tests for in-place corpus formula repair engine."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from kb.math.repair import CorpusFormulaRepairer, RepairResult


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
