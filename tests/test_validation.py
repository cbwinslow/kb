"""Unit tests for the mathematical quality gate and multi-tier validation engine."""

from __future__ import annotations

import pytest

from kb.math.validation import (
    FormulaQualityGate,
    FormulaQualityScorecard,
    ValidationCheckResult,
    ValidationTier,
)
from kb.storage.models import Formula


def test_validation_tier_enum() -> None:
    """Verify validation tier enum string representations."""
    assert ValidationTier.TIER1_AST_ROUNDTRIP == "ast_roundtrip"
    assert ValidationTier.TIER2_SYMBOL_ENCODING == "symbol_encoding"
    assert ValidationTier.TIER3_BOUNDARY_INVARIANTS == "boundary_invariants"
    assert ValidationTier.TIER4_EMPIRICAL_BENCHMARK == "empirical_benchmark"


def test_validation_check_result_to_dict() -> None:
    """Verify serialization of individual check result."""
    check = ValidationCheckResult(
        name="Test Check",
        tier=ValidationTier.TIER1_AST_ROUNDTRIP,
        passed=True,
        score=10.0,
        max_score=10.0,
        message="Passed test check",
        details={"var": "x"},
    )
    d = check.to_dict()
    assert d["name"] == "Test Check"
    assert d["tier"] == "ast_roundtrip"
    assert d["passed"] is True
    assert d["score"] == 10.0
    assert d["details"]["var"] == "x"


def test_quality_gate_pythagorean_formula() -> None:
    """Verify validation gate produces an 'A' grade on Pythagorean expectation."""
    gate = FormulaQualityGate()
    raw = r"W = \frac{R_S^2}{R_S^2 + R_A^2}"
    card = gate.validate_formula(raw)

    assert isinstance(card, FormulaQualityScorecard)
    assert card.is_valid is True
    assert card.total_score >= 88.0
    assert card.letter_grade == "A"
    assert card.status == "verified"
    assert card.tier_scores[ValidationTier.TIER1_AST_ROUNDTRIP.value] == 25.0
    assert card.tier_scores[ValidationTier.TIER2_SYMBOL_ENCODING.value] == 25.0
    assert card.tier_scores[ValidationTier.TIER3_BOUNDARY_INVARIANTS.value] == 25.0
    assert card.tier_scores[ValidationTier.TIER4_EMPIRICAL_BENCHMARK.value] >= 18.0


def test_quality_gate_invalid_unparseable() -> None:
    """Verify validation gate assigns 0 points, Grade 'F', and 'failed' status to broken LaTeX."""
    gate = FormulaQualityGate()
    card = gate.validate_formula(r"\frac{broken}{")

    assert card.is_valid is False
    assert card.total_score == 0.0
    assert card.letter_grade == "F"
    assert card.status == "failed"
    assert len(card.recommendations) > 0


def test_quality_gate_cyclic_recursion_detection() -> None:
    """Verify cyclic LHS recursion is penalized in Tier 2."""
    gate = FormulaQualityGate()
    card = gate.validate_formula(r"x = 2 \cdot x + y")

    # Tier 2 acyclic check should fail
    acyclic_check = next(
        (c for c in card.checks if c.name == "Acyclic Definition Sanity"),
        None,
    )
    assert acyclic_check is not None
    assert acyclic_check.passed is False
    assert "cyclic recursion" in acyclic_check.message.lower()


def test_quality_gate_contradiction_detection() -> None:
    """Verify degenerate contradiction equations (x = x + 1) are flagged."""
    gate = FormulaQualityGate()
    card = gate.validate_formula("x = x + 1")

    ast_check = next(
        (c for c in card.checks if c.name == "SymPy Parseability"),
        None,
    )
    assert ast_check is not None
    assert ast_check.passed is False
    assert "degenerate boolean" in ast_check.message.lower()


def test_quality_gate_constant_expression() -> None:
    """Verify constants are handled gracefully without raising division or differentiation errors."""
    gate = FormulaQualityGate()
    card = gate.validate_formula("42")

    assert card.is_valid is True
    assert card.letter_grade in ("A", "B")
    finite_check = next(
        (c for c in card.checks if c.name == "Parameter Space Finite Evaluation"),
        None,
    )
    assert finite_check is not None
    assert finite_check.passed is True


def test_quality_gate_with_extracted_formula() -> None:
    """Verify validate_formula accepts ExtractedFormula objects."""
    gate = FormulaQualityGate()
    extracted = gate.extractor.parse_latex_string("y = 2 \\cdot x + 3")
    card = gate.validate_formula(extracted)

    assert card.is_valid is True
    assert card.letter_grade in ("A", "B")
    assert card.formula_id == extracted.formula_id


def test_quality_gate_with_formula_model() -> None:
    """Verify validate_formula accepts SQLAlchemy Formula model instances."""
    gate = FormulaQualityGate()
    formula_model = Formula(
        id="test_formula_123",
        document_id="doc_123",
        citekey="James1982",
        raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sympy_repr="Eq(W, R_S**2/(R_A**2 + R_S**2))",
        symbols=["W", "R_S", "R_A"],
        is_valid=True,
        is_equality=True,
    )
    card = gate.validate_formula(formula_model)

    assert card.formula_id == "test_formula_123"
    assert card.citekey == "James1982"
    assert card.total_score >= 88.0
    assert card.letter_grade == "A"


def test_scorecard_markdown_generation() -> None:
    """Verify scorecard markdown output contains key sections and no unicode crash."""
    gate = FormulaQualityGate()
    card = gate.validate_formula(r"FIP = \frac{13 \cdot H_R + 3 \cdot B_B - 2 \cdot K}{I_P} + 3.10")
    md = card.to_markdown()

    assert "# Formula Quality Scorecard" in md
    assert "Tier Breakdown" in md
    assert "Check Details" in md
    assert "[PASS]" in md


def test_formula_model_validation_fields() -> None:
    """Verify SQLAlchemy Formula model has the new validation columns."""
    f = Formula(
        id="f_sample",
        document_id="doc_sample",
        citekey="sample_citekey",
        raw_latex="x = y",
        sanitized_latex="x = y",
        validation_score=95.5,
        validation_status="verified",
        validation_details={"grade": "A"},
    )
    assert f.validation_score == 95.5
    assert f.validation_status == "verified"
    assert f.validation_details == {"grade": "A"}


@pytest.mark.asyncio
async def test_graphql_validate_formula_schema() -> None:
    """Verify validateFormula field is exposed on GraphQL Query schema."""
    from kb.graphql.schema import schema

    query = """
    query {
        validateFormula(id: "nonexistent_formula_xyz") {
            formulaId
            totalScore
            letterGrade
        }
    }
    """
    res = await schema.execute(query)
    assert res.errors is None
    assert res.data == {"validateFormula": None}
