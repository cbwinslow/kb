"""Unit tests for Unicode equation sanitization and macro unwrapping."""

from __future__ import annotations

import pytest
from sympy.parsing.latex import parse_latex

from kb.math.sanitizer import EquationSanitizer


@pytest.fixture
def sanitizer() -> EquationSanitizer:
    return EquationSanitizer()


def test_sanitize_unicode_greek(sanitizer: EquationSanitizer) -> None:
    raw = r"θ = α + β \times γ"
    clean = sanitizer.sanitize(raw)
    assert r"\theta" in clean
    assert r"\alpha" in clean
    assert r"\beta" in clean
    assert r"\gamma" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_unicode_operators(sanitizer: EquationSanitizer) -> None:
    raw = r"∑_{i=1}^{n} x_i ≤ C"
    clean = sanitizer.sanitize(raw)
    assert r"\sum" in clean
    assert r"\le" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_subscripts_and_superscripts(sanitizer: EquationSanitizer) -> None:
    raw = "x₁ + y² = z₃"
    clean = sanitizer.sanitize(raw)
    assert "x_1" in clean
    assert "y^2" in clean
    assert "z_3" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_mathematical_alphanumerics(sanitizer: EquationSanitizer) -> None:
    # U+1D461 is mathematical italic small t, U+1D465 is x, U+1D466 is y
    raw = "𝑡 = 𝑥 + 𝑦"
    clean = sanitizer.sanitize(raw)
    assert "t" in clean
    assert "x" in clean
    assert "y" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_unwrap_macros(sanitizer: EquationSanitizer) -> None:
    raw = r"\boldsymbol{W} = \mathbf{X}^{T} \mathbb{R} + \mathcal{L}"
    clean = sanitizer.sanitize(raw)
    assert r"\boldsymbol" not in clean
    assert r"\mathbf" not in clean
    assert r"\mathbb" not in clean
    assert r"\mathcal" not in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_balance_braces(sanitizer: EquationSanitizer) -> None:
    raw = r"\frac{a + b}{c"
    clean = sanitizer.sanitize(raw)
    assert clean.count("{") == clean.count("}")
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_compound_metrics(sanitizer: EquationSanitizer) -> None:
    raw = r"wOBA = \frac{0.69 \times BB + 0.89 \times 1B}{AB + BB}"
    clean = sanitizer.sanitize(raw)
    assert "w_{OBA}" in clean
    assert "B_{B}" in clean
    assert "A_{B}" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_mathematical_bold_greek(sanitizer: EquationSanitizer) -> None:
    # \U0001D6FD is Mathematical Bold Small Beta, \U0001D6FC is Alpha, \U0001D706 is Lambda
    raw = "\U0001d6fc = \U0001d6fd_1 + \U0001d706_2"
    clean = sanitizer.sanitize(raw)
    assert r"\alpha" in clean
    assert r"\beta" in clean
    assert r"\lambda" in clean
    expr = parse_latex(clean)
    assert expr is not None


def test_sanitize_extended_operators_and_accents(sanitizer: EquationSanitizer) -> None:
    # \u2206 Increment, \u22a4 Transpose, \u27e8/\u27e9 angle brackets, \u20d7 vector arrow, \uf8ec PUA
    raw = "y = \u2206x\u20d7 + A\u22a4 \u27e8v\u27e9 \uf8ec\uf8f4"
    clean = sanitizer.sanitize(raw)
    assert r"\Delta" in clean
    assert "^T" in clean
    assert r"\langle" in clean
    assert r"\rangle" in clean
    assert "\uf8ec" not in clean
    assert "\u20d7" not in clean
    expr = parse_latex(clean)
    assert expr is not None
