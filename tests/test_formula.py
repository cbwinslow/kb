"""Tests for equation sanitization, formula extraction, and AST code generation."""

import math

import pytest
from sympy.core.relational import Equality

from kb.ingest.chunker import EnrichedChunk
from kb.math.ast_gen import FormulaCodeGenerator
from kb.math.extractor import FormulaExtractor
from kb.math.sanitizer import EquationSanitizer


@pytest.fixture
def sanitizer() -> EquationSanitizer:
    return EquationSanitizer()


@pytest.fixture
def extractor() -> FormulaExtractor:
    return FormulaExtractor()


@pytest.fixture
def code_gen() -> FormulaCodeGenerator:
    return FormulaCodeGenerator()


@pytest.mark.parametrize(
    ("raw_input", "expected_contains"),
    [
        (r"$$\frac{RS^2}{RS^2 + RA^2}$$", r"\frac{R_{S}^2}{R_{S}^2 + R_{A}^2}"),
        (
            r"\begin{equation}\tag{1} W = \frac{RS^\gamma}{RS^\gamma + RA^\gamma} \end{equation}",
            "W =",
        ),
        (r"W = \frac{RS^2}{RS^2 + RA^2} (2.1)", r"\frac{R_{S}^2}{R_{S}^2 + R_{A}^2}"),
        (
            r"13 \times HR + 3 \cdot BB - 2 \times SO",
            r"13 \times H_{R} + 3 \cdot B_{B} - 2 \times S_{O}",
        ),
        (r"\frac {A}{B + C}", r"\frac{A}{B + C}"),
        (
            r"\[ W = \frac{\text{RS}^2}{\text{RS}^2 + \text{RA}^2} \]",
            r"\frac{R_{S}^2}{R_{S}^2 + R_{A}^2}",
        ),
    ],
)
def test_equation_sanitizer_parameterized(
    sanitizer: EquationSanitizer, raw_input: str, expected_contains: str
) -> None:
    sanitized = sanitizer.sanitize(raw_input)
    assert expected_contains in sanitized
    assert "$$" not in sanitized
    assert r"\tag" not in sanitized


def test_formula_extractor_symbolic_parsing(extractor: FormulaExtractor) -> None:
    # Pythagorean Expectation
    raw = r"$$W = \frac{RS^2}{RS^2 + RA^2}$$"
    formula = extractor.parse_latex_string(raw)

    assert formula.is_valid is True
    assert formula.is_equality is True
    assert formula.lhs == "W"
    assert formula.sympy_expr is not None
    assert isinstance(formula.sympy_expr, Equality)
    assert "R_{S}" in formula.symbols
    assert "R_{A}" in formula.symbols


def test_formula_extractor_from_chunk(extractor: FormulaExtractor) -> None:
    chunk_text = (
        "The model predicts win ratio: $$W = \\frac{RS^2}{RS^2 + RA^2}$$ with parameter $k=2$."
    )
    chunk = EnrichedChunk(
        chunk_id="test_chunk_001",
        document_id="doc_miller",
        citekey="miller2008",
        chunk_index=0,
        raw_text=chunk_text,
        enriched_text="[Document: Miller | Section: Intro]\n\n...",
        math_expressions=["$$W = \\frac{RS^2}{RS^2 + RA^2}$$"],
    )
    formulas = extractor.extract_from_chunk(chunk)
    assert len(formulas) >= 1
    assert any(f.is_valid and f.is_equality for f in formulas)


def test_ast_generator_callable_and_evaluation(
    extractor: FormulaExtractor, code_gen: FormulaCodeGenerator
) -> None:
    raw = r"W = \frac{RS^\gamma}{RS^\gamma + RA^\gamma}"
    formula = extractor.parse_latex_string(raw)
    assert formula.is_valid is True

    # 1. Direct evaluation via evaluate()
    # If RS=700, RA=600, gamma=2.0 -> 700^2 / (700^2 + 600^2) = 490000 / 850000 = ~0.57647
    result_val = code_gen.evaluate(formula, R_S=700.0, R_A=600.0, gamma=2.0)
    expected_val = (700.0**2) / (700.0**2 + 600.0**2)
    assert math.isclose(result_val, expected_val, rel_tol=1e-5)

    # 2. General exponent gamma=1.83 (empirically fitted for MLB)
    fitted_val = code_gen.evaluate(formula, R_S=750.0, R_A=650.0, gamma=1.83)
    exp_fitted = (750.0**1.83) / (750.0**1.83 + 650.0**1.83)
    assert math.isclose(fitted_val, exp_fitted, rel_tol=1e-5)

    # 3. Fast compiled callable
    fn = code_gen.generate_callable(formula)
    # Ordered symbols: R_A, R_S, gamma
    computed = fn(600.0, 700.0, 2.0)
    assert math.isclose(computed, expected_val, rel_tol=1e-5)


def test_ast_generator_python_source(
    extractor: FormulaExtractor, code_gen: FormulaCodeGenerator
) -> None:
    raw = r"\frac{RS^2}{RS^2 + RA^2}"
    formula = extractor.parse_latex_string(raw)
    source = code_gen.generate_python_source(formula, function_name="pythagorean_expectation")

    assert "def pythagorean_expectation(R_A: float, R_S: float) -> float:" in source
    assert "return float(" in source

    # Execute generated python code string
    namespace: dict[str, object] = {}
    exec(source, namespace)  # noqa: S102
    pythag_fn = namespace["pythagorean_expectation"]
    assert callable(pythag_fn)
    computed_ratio = float(pythag_fn(R_A=600.0, R_S=700.0))  # type: ignore[misc]
    assert math.isclose(computed_ratio, 490000 / 850000, rel_tol=1e-5)


def test_extract_math_symbols_and_references() -> None:
    """Verifies extraction of Greek symbols, domain variables, and equation references."""
    from kb.math import (
        extract_equation_references,
        extract_math_symbols,
        extract_variable_glossary,
    )

    sample_derivation = (
        r"Consider the linear model $Y_{i} = \beta_{0} + \beta_{1} X_{i} + \epsilon_{i}$ "
        r"with noise variance $\sigma^2$ and mean $\mu$. "
        r"In sabermetric evaluation, we compare RS and RA using Equation (1). "
        r"As shown in Eq. (2.3), substituting (1) into formula 4 yields optimal weights, "
        r"where $RS$ denotes runs scored, and $RA$ is the runs allowed."
    )

    symbols = extract_math_symbols(sample_derivation)
    assert "epsilon" in symbols
    assert "sigma^2" in symbols
    assert "mu" in symbols
    assert "RS" in symbols
    assert "RA" in symbols
    assert "Y_{i}" in symbols or "X_{i}" in symbols

    refs = extract_equation_references(sample_derivation)
    assert "1" in refs
    assert "2.3" in refs
    assert "4" in refs

    glossary = extract_variable_glossary(sample_derivation)
    assert "RS" in glossary
    assert "runs scored" in glossary["RS"]
    assert "RA" in glossary
    assert "runs allowed" in glossary["RA"]

