"""Unit tests for Formula Sanitizer V3, delimiter rebalancer, and piecewise AST recovery."""

from __future__ import annotations

import polars as pl
import pytest
from sympy import Equality, Piecewise

from kb.codegen.compiler import FormulaCompiler
from kb.math.extractor import FormulaExtractor
from kb.math.repair import CorpusFormulaRepairer
from kb.math.sanitizer import EquationSanitizer


@pytest.fixture
def sanitizer() -> EquationSanitizer:
    """Fixture providing EquationSanitizer instance."""
    return EquationSanitizer()


@pytest.fixture
def extractor() -> FormulaExtractor:
    """Fixture providing FormulaExtractor instance."""
    return FormulaExtractor()


@pytest.fixture
def compiler() -> FormulaCompiler:
    """Fixture providing FormulaCompiler instance."""
    return FormulaCompiler()


def test_protect_acronyms_babip(extractor: FormulaExtractor) -> None:
    """Verify that multi-character sabermetric acronyms parse as atomic symbols."""
    raw = r"\text{BABIP} = \frac{H - HR}{AB - K - HR + SF}"
    result = extractor.parse_latex_string(raw, formula_id="test_babip")

    assert result.is_valid is True
    assert result.is_equality is True
    assert result.lhs == "BABIP"
    assert "BABIP" in result.symbols
    assert "HR" in result.symbols
    assert "AB" in result.symbols
    assert "SF" in result.symbols
    # Ensure it did NOT decompose into individual single letter multiplications
    assert "A" not in result.symbols
    assert "I" not in result.symbols


def test_protect_acronyms_woba(extractor: FormulaExtractor) -> None:
    """Verify that wOBA equation with multiple boxscore acronyms preserves symbols."""
    raw = r"wOBA = \frac{0.69 \cdot BB + 0.72 \cdot HBP + 2.10 \cdot HR}{AB + BB + SF}"
    result = extractor.parse_latex_string(raw, formula_id="test_woba")

    assert result.is_valid is True
    assert result.is_equality is True
    assert "wOBA" in result.symbols
    assert "BB" in result.symbols
    assert "HBP" in result.symbols
    assert "HR" in result.symbols
    assert "AB" in result.symbols


def test_protect_acronyms_fip(extractor: FormulaExtractor) -> None:
    """Verify that FIP equation preserves FIP, HR, BB, SO, and IP."""
    raw = r"FIP = \frac{13 \cdot HR + 3 \cdot BB - 2 \cdot SO}{IP} + c"
    result = extractor.parse_latex_string(raw, formula_id="test_fip")

    assert result.is_valid is True
    assert result.is_equality is True
    assert "FIP" in result.symbols
    assert "HR" in result.symbols
    assert "BB" in result.symbols
    assert "SO" in result.symbols
    assert "IP" in result.symbols


def test_balance_delimiters(sanitizer: EquationSanitizer, extractor: FormulaExtractor) -> None:
    """Verify rebalancing of unclosed delimiters and sizing tags."""
    # Unclosed \left(
    raw1 = r"y = \left( \frac{a}{b}"
    balanced1 = sanitizer.balance_delimiters(raw1)
    assert r"\right)" in balanced1
    res1 = extractor.parse_latex_string(raw1)
    assert res1.is_valid is True

    # Unclosed brackets
    raw2 = r"z = [a + b"
    balanced2 = sanitizer.balance_delimiters(raw2)
    assert balanced2.endswith("]")
    res2 = extractor.parse_latex_string(raw2)
    assert res2.is_valid is True

    # Odd pipe delimiter
    raw3 = r"w = |x"
    balanced3 = sanitizer.balance_delimiters(raw3)
    assert balanced3.endswith("|")


def test_piecewise_cases_reconstruction(extractor: FormulaExtractor) -> None:
    """Verify that \\begin{cases} environments are parsed into SymPy Piecewise objects."""
    raw = r"y = \begin{cases} x & x > 0 \\ -x & x \le 0 \end{cases}"
    result = extractor.parse_latex_string(raw, formula_id="test_cases_1")

    assert result.is_valid is True
    assert result.is_equality is True
    assert isinstance(result.sympy_expr, Equality)
    assert isinstance(result.sympy_expr.rhs, Piecewise)
    assert "x" in result.symbols
    assert "y" in result.symbols


def test_piecewise_cases_with_text_conditions(extractor: FormulaExtractor) -> None:
    """Verify piecewise equations containing explanatory text conditions."""
    raw = r"f(x) = \begin{cases} x^2 & \text{if } x \ge 0 \\ -x & \text{otherwise} \end{cases}"
    result = extractor.parse_latex_string(raw, formula_id="test_cases_2")

    assert result.is_valid is True
    assert isinstance(result.sympy_expr, Equality)
    assert isinstance(result.sympy_expr.rhs, Piecewise)
    assert "x" in result.symbols


def test_compiler_piecewise_polars_code(compiler: FormulaCompiler) -> None:
    """Verify that compiling a piecewise formula produces executable Python and Polars expressions."""
    raw = r"y = \begin{cases} x^2 & x \ge 0 \\ -x & x < 0 \end{cases}"
    compiled = compiler.compile(
        formula_id="pw_test",
        citekey="test2024",
        raw_latex=raw,
    )

    assert compiled.is_valid is True
    assert compiled.polars_expression is not None
    assert "pl.when" in compiled.polars_expression
    assert "then" in compiled.polars_expression

    # Verify Polars execution
    df = pl.DataFrame({"x": [-3.0, 0.0, 4.0]})
    # Execute polars expression
    expr = eval(compiled.polars_expression)
    out = df.select(expr).to_series().to_list()
    assert out == [3.0, 0.0, 16.0]


def test_corpus_repairer_single_recovery() -> None:
    """Verify that CorpusFormulaRepairer can repair single formulas in-memory."""
    repairer = CorpusFormulaRepairer()
    raw = r"\text{BABIP} = \frac{H - HR}{AB - K - HR + SF}"
    repaired = repairer.repair_single(raw, formula_id="single_test")

    assert repaired.is_valid is True
    assert "BABIP" in repaired.symbols
