"""Unit tests for FormulaCompiler and FormulaVerifier."""

from __future__ import annotations

from pathlib import Path

import polars as pl

from kb.codegen.compiler import FormulaCompiler
from kb.codegen.verifier import FormulaVerifier


def test_formula_compiler_simple() -> None:
    compiler = FormulaCompiler()
    # Pythagorean Expectation: W = RS^2 / (RS^2 + RA^2)
    latex = r"W = \frac{RS^2}{RS^2 + RA^2}"
    result = compiler.compile(
        formula_id="test_pythag",
        citekey="james1980",
        raw_latex=latex,
        function_name="calc_pythagorean_wp",
    )

    assert result.is_valid
    assert "calc_pythagorean_wp" in result.python_source
    assert any("RS" in p.replace("_", "") for p in result.parameters)
    assert any("RA" in p.replace("_", "") for p in result.parameters)
    assert result.polars_expression is not None
    assert 'pl.col("R_S")' in result.polars_expression or 'pl.col("RS")' in result.polars_expression
    assert 'pl.col("R_A")' in result.polars_expression or 'pl.col("RA")' in result.polars_expression


def test_formula_verifier_with_inputs() -> None:
    compiler = FormulaCompiler()
    verifier = FormulaVerifier(compiler=compiler)

    latex = r"W = \frac{RS^2}{RS^2 + RA^2}"
    codegen = compiler.compile(
        formula_id="test_pythag",
        citekey="james1980",
        raw_latex=latex,
        function_name="calc_pythagorean_wp",
    )

    # 800 RS, 700 RA -> 800^2 / (800^2 + 700^2) = 640000 / (640000 + 490000) = 64 / 113 ≈ 0.56637
    inputs = {"RS": [800.0, 750.0], "RA": [700.0, 750.0]}
    expected = [640000.0 / 1130000.0, 0.5]

    res = verifier.verify_with_inputs(codegen, input_data=inputs, expected_outputs=expected)
    assert res.passed
    assert res.num_samples == 2
    assert res.mean_absolute_error is not None
    assert res.mean_absolute_error < 1e-4


def test_formula_verifier_against_parquet(tmp_path: Path) -> None:
    compiler = FormulaCompiler()
    verifier = FormulaVerifier(compiler=compiler)

    # Create dummy parquet fixture
    df = pl.DataFrame({
        "RS": [700.0, 800.0, 900.0],
        "RA": [700.0, 600.0, 500.0],
        "ActualWP": [0.5, 64.0 / 100.0, 81.0 / 106.0],  # 800^2 / (800^2+600^2) = 6400/(6400+3600) = 0.64
    })
    parquet_file = tmp_path / "benchmark_pythag.parquet"
    df.write_parquet(parquet_file)

    latex = r"W = \frac{RS^2}{RS^2 + RA^2}"
    codegen = compiler.compile(
        formula_id="test_pythag",
        citekey="james1980",
        raw_latex=latex,
        function_name="calc_pythagorean_wp",
    )

    res = verifier.verify_against_parquet(
        codegen,
        parquet_path=parquet_file,
        target_column="ActualWP",
    )

    assert res.passed
    assert res.num_samples == 3
    assert res.mean_absolute_error is not None
    assert res.mean_absolute_error < 1e-4
