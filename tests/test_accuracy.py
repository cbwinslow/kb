"""Ground-truth numerical accuracy and benchmark verification tests."""

from __future__ import annotations

import math

import polars as pl
import sympy as sp
from sympy.parsing.latex import parse_latex


def test_pythagorean_expectation_accuracy() -> None:
    """Verifies that mathematical formula evaluation for Pythagorean expectation matches canonical ground truth."""
    latex_eq = r"W = \frac{R_S^\gamma}{R_S^\gamma + R_A^\gamma}"
    expr = parse_latex(latex_eq)
    assert expr is not None

    target = getattr(expr, "rhs", expr)
    symbols = {str(s): s for s in target.free_symbols}
    R_S = symbols["R_{S}"]
    R_A = symbols["R_{A}"]
    gamma = symbols["gamma"]

    # Lambdify expression
    func = sp.lambdify((R_S, R_A, gamma), target, "math")

    # Benchmark test 1: RS=750, RA=650, gamma=1.83 (Pythagenpat standard)
    rs, ra, g = 750.0, 650.0, 1.83
    expected_w_pct = (rs**g) / (rs**g + ra**g)
    calculated = func(rs, ra, g)
    assert math.isclose(calculated, expected_w_pct, rel_tol=1e-6)
    assert math.isclose(calculated, 0.56510, abs_tol=1e-4)

    # Benchmark test 2: RS=800, RA=700, gamma=2.0 (Bill James original)
    rs2, ra2, g2 = 800.0, 700.0, 2.0
    expected_w_pct2 = (800.0**2) / (800.0**2 + 700.0**2)  # 640000 / 1130000 = 0.566371...
    calculated2 = func(rs2, ra2, g2)
    assert math.isclose(calculated2, expected_w_pct2, rel_tol=1e-6)
    assert math.isclose(calculated2, 0.56637, abs_tol=1e-4)


def test_fip_accuracy() -> None:
    """Verifies Fielding Independent Pitching (FIP) canonical benchmark calculation."""
    latex_eq = r"F = \frac{13 \cdot H_R + 3 \cdot (B_B + H_B) - 2 \cdot K}{I_P} + C"
    expr = parse_latex(latex_eq)
    assert expr is not None

    target = getattr(expr, "rhs", expr)
    symbols = {str(s): s for s in target.free_symbols}
    H_R = symbols["H_{R}"]
    B_B = symbols["B_{B}"]
    H_B = symbols["H_{B}"]
    K = symbols["K"]
    I_P = symbols["I_{P}"]
    C = symbols["C"]

    fip_func = sp.lambdify((H_R, B_B, H_B, K, I_P, C), target, "math")

    # Ground truth scenario: 20 HR, 50 BB, 5 HBP, 180 K, 200 IP, C=3.10
    # Numerator = 13*20 + 3*(50+5) - 2*180 = 260 + 165 - 360 = 65
    # FIP = 65/200 + 3.10 = 0.325 + 3.10 = 3.425
    result = fip_func(20.0, 50.0, 5.0, 180.0, 200.0, 3.10)
    assert math.isclose(result, 3.425, abs_tol=1e-5)


def test_polars_vectorized_numerical_parity() -> None:
    """Verifies that vectorised Polars expressions produce identical numerical results to scalar functions."""
    # Create sample DataFrame
    df = pl.DataFrame({
        "R": [700.0, 750.0, 800.0, 650.0],
        "RA": [650.0, 650.0, 700.0, 750.0],
        "gamma": [1.83, 1.83, 2.0, 1.83],
    })

    # Scalar computation
    scalar_results = [
        (r**g) / (r**g + ra**g)
        for r, ra, g in zip(df["R"], df["RA"], df["gamma"], strict=True)
    ]

    # Polars expression computation
    pyth_expr = pl.col("R") ** pl.col("gamma") / (
        pl.col("R") ** pl.col("gamma") + pl.col("RA") ** pl.col("gamma")
    )
    df_result = df.with_columns(pyth_expr.alias("W_pct"))
    polars_results = df_result["W_pct"].to_list()

    for scalar_val, polars_val in zip(scalar_results, polars_results, strict=True):
        assert math.isclose(scalar_val, polars_val, rel_tol=1e-6)
