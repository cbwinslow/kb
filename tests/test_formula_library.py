"""Unit tests for standalone formula library compilation and export."""

from __future__ import annotations

import ast
from unittest.mock import MagicMock

import polars as pl
import pytest

from kb.library.generator import (
    FormulaLibraryGenerator,
    GeneratedFormulaFunction,
)
from kb.storage.models import Document, Formula


@pytest.fixture
def sample_formula() -> Formula:
    """Fixture providing a mock verified equality formula."""
    f = Formula(
        id="test-formula-1234",
        citekey="baumer2015",
        raw_latex=r"wOBA = \frac{0.69 \cdot BB + 0.89 \cdot 1B + 1.27 \cdot 2B}{AB + BB}",
        sanitized_latex="wOBA = (0.69*BB + 0.89*B_1 + 1.27*B_2) / (AB + BB)",
        sympy_repr="Eq(wOBA, (0.69*BB + 0.89*B_1 + 1.27*B_2)/(AB + BB))",
        symbols=["AB", "BB", "B_1", "B_2", "wOBA"],
        is_valid=True,
        is_equality=True,
        lhs="wOBA",
        rhs="(0.69*BB + 0.89*B_1 + 1.27*B_2) / (AB + BB)",
    )
    return f


@pytest.fixture
def sample_document() -> Document:
    """Fixture providing document metadata."""
    d = Document(
        citekey="baumer2015",
        title="Open-source Sabermetrics and Advanced Run Estimators",
        authors=["Benjamin S. Baumer", "Gregory J. Matthews"],
        year=2015,
        file_path="data/arxiv_papers/test.pdf",
    )
    return d


def test_sanitize_name():
    """Verify LaTeX math fragments are cleaned to valid identifiers."""
    gen = FormulaLibraryGenerator(db_manager=MagicMock())
    assert gen.sanitize_name(r"\alpha") == "metric"
    assert gen.sanitize_name("wOBA") == "woba"
    assert gen.sanitize_name("WAR_rep") == "war_rep"
    assert gen.sanitize_name("1205.4750") == "val_1205_4750"


def test_compile_formula(sample_formula: Formula, sample_document: Document):
    """Verify formula compilation emits valid scalar and Polars functions."""
    gen = FormulaLibraryGenerator(db_manager=MagicMock())
    res = gen.compile_formula(sample_formula, doc=sample_document)

    assert res is not None
    assert isinstance(res, GeneratedFormulaFunction)
    assert res.function_name.startswith("calc_woba_")
    assert res.expr_function_name.startswith("expr_woba_")
    assert set(res.parameters) == {"AB", "BB", "B_1", "B_2"}

    # Verify scalar function syntax
    ast.parse(res.scalar_code)
    # Verify docstring contains KaTeX formula and metadata
    assert "KaTeX Formula" in res.scalar_code
    assert "Benjamin S. Baumer" in res.scalar_code
    assert "Open-source Sabermetrics" in res.scalar_code

    # Verify Polars expression syntax
    ast.parse(res.polars_code)
    assert 'pl.col("AB")' in res.polars_code or 'pl.col(AB)' in res.polars_code
    assert 'pl.col("BB")' in res.polars_code or 'pl.col(BB)' in res.polars_code


def test_generate_module_source(sample_formula: Formula, sample_document: Document):
    """Verify generated standalone module has valid syntax and header."""
    gen = FormulaLibraryGenerator(db_manager=MagicMock())
    res = gen.compile_formula(sample_formula, doc=sample_document)
    assert res is not None

    source = gen.generate_module_source([res])
    assert "from __future__ import annotations" in source
    assert "import polars as pl" in source
    assert res.function_name in source
    assert res.expr_function_name in source

    # Check complete AST validity
    tree = ast.parse(source)
    assert len(tree.body) > 3


def test_scalar_and_polars_execution():
    """Verify numerical execution parity between scalar and Polars expressions."""

    # Define a sample compiled function pair manually to test runtime parity
    def calc_test_ops(OBP: float, SLG: float) -> float:
        return float(OBP + SLG)

    def expr_test_ops() -> pl.Expr:
        return pl.col("OBP") + pl.col("SLG")

    # Scalar check
    scalar_val = calc_test_ops(OBP=0.350, SLG=0.450)
    assert pytest.approx(scalar_val, rel=1e-4) == 0.800

    # Polars vectorized check
    df = pl.DataFrame(
        {
            "OBP": [0.300, 0.350, 0.400],
            "SLG": [0.400, 0.450, 0.500],
        }
    )
    df_out = df.with_columns(OPS=expr_test_ops())
    results = df_out["OPS"].to_list()
    assert pytest.approx(results[0], rel=1e-4) == 0.700
    assert pytest.approx(results[1], rel=1e-4) == 0.800
    assert pytest.approx(results[2], rel=1e-4) == 0.900
