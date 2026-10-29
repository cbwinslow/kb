"""Unit tests for Formula Coverage Metrics Engine."""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from kb.math.coverage import FormulaCoverageAnalyzer
from kb.math.extractor import ExtractedFormula
from kb.math.ontology import SymbolOntology


@pytest.fixture
def ontology() -> SymbolOntology:
    return SymbolOntology()


@pytest.fixture
def analyzer(ontology: SymbolOntology) -> FormulaCoverageAnalyzer:
    return FormulaCoverageAnalyzer(ontology=ontology)


def test_analyze_extracted_formulas(analyzer: FormulaCoverageAnalyzer) -> None:
    formulas = [
        ExtractedFormula(
            formula_id="f1",
            raw_latex=r"wOBA = \frac{0.7 \times BB + 0.9 \times 1B}{AB + BB}",
            sanitized_latex=r"w_{OBA} = \frac{0.7 \times B_{B} + 0.9 \times 1B}{A_{B} + B_{B}}",
            symbols=["A_{B}", "B_{B}", "w_{OBA}"],
            is_valid=True,
            is_equality=True,
            lhs="w_{OBA}",
            rhs=r"\frac{0.7 \times B_{B} + 0.9 \times 1B}{A_{B} + B_{B}}",
        ),
        ExtractedFormula(
            formula_id="f2",
            raw_latex=r"FIP = \frac{13 \times HR + 3 \times BB - 2 \times SO}{IP} + C",
            sanitized_latex=r"F_{IP} = \frac{13 \times H_{R} + 3 \times B_{B} - 2 \times S_{O}}{I_{P}} + C",
            symbols=["B_{B}", "C", "F_{IP}", "H_{R}", "I_{P}", "S_{O}"],
            is_valid=True,
            is_equality=True,
            lhs="F_{IP}",
            rhs=r"\frac{13 \times H_{R} + 3 \times B_{B} - 2 \times S_{O}}{I_{P}} + C",
        ),
        ExtractedFormula(
            formula_id="f3",
            raw_latex=r"θ \badmacro{x}",
            sanitized_latex=r"\theta \badmacro{x}",
            symbols=[],
            is_valid=False,
            is_equality=False,
            error_message="ANTLR syntax error at badmacro",
        ),
    ]

    report = analyzer.analyze_extracted_formulas(formulas)

    assert report.total_formulas == 3
    assert report.valid_formulas == 2
    assert report.invalid_formulas == 1
    assert report.equality_formulas == 2
    assert report.parse_yield_pct == round(2 / 3 * 100.0, 2)
    assert report.equality_yield_pct == 100.0

    # Defined symbols should contain LHS symbols
    assert "w_{OBA}" in report.defined_symbols
    assert "F_{IP}" in report.defined_symbols

    # Consumed symbols should contain RHS symbols
    assert "B_{B}" in report.consumed_symbols
    assert "H_{R}" in report.consumed_symbols
    assert "C" in report.consumed_symbols

    # Ontology mapped symbols
    assert "B_{B}" in report.ontology_mapped_symbols or "H_{R}" in report.ontology_mapped_symbols

    # C is an unconstrained constant, not defined on LHS and not in default baseball ontology
    assert "C" in report.orphan_symbols

    # Non-ASCII character accounting
    assert "θ" in report.character_accounting
    assert report.character_accounting["θ"] == 1

    # Error taxonomy
    assert any("ANTLR" in k for k in report.error_taxonomy)

    # Output formatting
    md = report.to_markdown()
    assert "# Mathematical Formula & Variable Coverage Report" in md
    assert "Executive Summary" in md

    js = report.to_json()
    data = json.loads(js)
    assert data["total_formulas"] == 3


@pytest.mark.asyncio
async def test_analyze_corpus_mocked(analyzer: FormulaCoverageAnalyzer) -> None:
    session = AsyncMock()
    mock_formula = MagicMock()
    mock_formula.is_valid = True
    mock_formula.is_equality = True
    mock_formula.lhs = "WAR"
    mock_formula.raw_latex = "WAR = wRAA + UZR"
    mock_formula.symbols = ["WAR", "wRAA", "UZR"]
    mock_formula.error_message = None

    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = [mock_formula]
    session.execute.return_value = result_mock

    report = await analyzer.analyze_corpus(limit=10, session=session)
    assert report.total_formulas == 1
    assert report.valid_formulas == 1
    assert "WAR" in report.defined_symbols
