"""Unit tests for CorpusQAEngine."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from kb.search.qa import CorpusQAEngine, ResearchAnswer
from kb.storage.search import SearchResult


def test_research_answer_formatting() -> None:
    ans = ResearchAnswer(
        question="How does park factor affect linear weights?",
        synthesis="Park factors adjust baseline runs scored in offensive metrics.",
        cited_sources=[{
            "citekey": "fast2011",
            "title": "Park Factors in Sabermetrics",
            "authors": ["Mike Fast"],
            "year": 2011,
        }],
        relevant_formulas=[{
            "citekey": "fast2011",
            "latex": "PF = \\frac{RS_{home}}{RS_{away}}",
            "python_code": "def calc_pf(RS_home: float, RS_away: float) -> float:\n    return RS_home / RS_away",
        }],
        relevant_tables=[{
            "citekey": "fast2011",
            "caption": "Multi-year park factors",
            "columns": ["Team", "PF_3yr"],
            "num_rows": 30,
        }],
    )

    text = ans.format_terminal()
    assert "RESEARCH SYNTHESIS" in text
    assert "fast2011" in text
    assert "PF =" in text
    assert "def calc_pf" in text
    assert "Multi-year park factors" in text


@pytest.mark.asyncio
async def test_corpus_qa_engine_mocked() -> None:
    mock_db = MagicMock()
    mock_session = AsyncMock()

    mock_db.session_factory.return_value.__aenter__.return_value = mock_session

    engine = CorpusQAEngine(db_manager=mock_db)

    # Mock search_engine.search
    mock_chunks = [
        SearchResult(
            chunk_id="chunk_01",
            document_id="doc_01",
            citekey="james1980",
            section_path=["Introduction"],
            parent_section=None,
            text="The Pythagorean formula relates runs scored and runs allowed to win percentage.",
            rrf_score=0.92,
            dense_rank=1,
            sparse_rank=1,
            dense_score=0.85,
            sparse_score=12.4,
            has_math=True,
            has_table=False,
        )
    ]

    mock_doc = MagicMock()
    mock_doc.citekey = "james1980"
    mock_doc.title = "The 1980 Baseball Abstract"
    mock_doc.authors = ["Bill James"]
    mock_doc.year = 1980
    mock_doc.doi = None

    mock_formula = MagicMock()
    mock_formula.id = "f_01"
    mock_formula.citekey = "james1980"
    mock_formula.raw_latex = r"W = \frac{RS^2}{RS^2 + RA^2}"
    mock_formula.symbols = ["RS", "RA"]
    mock_formula.sympy_repr = None

    # Database query mocks
    async def mock_execute(stmt: object) -> MagicMock:
        res = MagicMock()
        stmt_str = str(stmt).lower()
        if "from kb_documents" in stmt_str:
            res.scalars.return_value.all.return_value = [mock_doc]
        elif "from kb_formulas" in stmt_str:
            res.scalars.return_value.all.return_value = [mock_formula]
        elif "from kb_benchmark_tables" in stmt_str:
            res.scalars.return_value.all.return_value = []
        return res

    mock_session.execute = mock_execute

    with patch.object(engine.search_engine, "search", new=AsyncMock(return_value=mock_chunks)):
        answer = await engine.answer("Pythagorean expectation derivation")

        assert answer.question == "Pythagorean expectation derivation"
        assert len(answer.cited_sources) == 1
        assert answer.cited_sources[0]["citekey"] == "james1980"
        assert len(answer.relevant_formulas) == 1
        assert answer.relevant_formulas[0]["citekey"] == "james1980"
        assert "calc_" in answer.relevant_formulas[0].get("python_code", "")
