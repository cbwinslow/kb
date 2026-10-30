"""Unit tests for FormulaCompiler and FormulaVerifier."""

from __future__ import annotations

from pathlib import Path

import polars as pl
import pytest

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
    df = pl.DataFrame(
        {
            "RS": [700.0, 800.0, 900.0],
            "RA": [700.0, 600.0, 500.0],
            "ActualWP": [
                0.5,
                64.0 / 100.0,
                81.0 / 106.0,
            ],  # 800^2 / (800^2+600^2) = 6400/(6400+3600) = 0.64
        }
    )
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


def test_formula_library_generator_polars_expr() -> None:
    """Verify FormulaLibraryGenerator generates parameterized Polars expression signatures."""
    from kb.library.generator import FormulaLibraryGenerator
    from kb.storage.models import Document, Formula

    gen = FormulaLibraryGenerator()
    formula = Formula(
        id="f_test_polars",
        document_id="doc_test",
        citekey="james1982",
        raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sympy_repr="Eq(W, R_S**2/(R_A**2 + R_S**2))",
        symbols=["R_S", "R_A", "W"],
        is_valid=True,
        is_equality=True,
        lhs="W",
        rhs=r"\frac{R_S^2}{R_S^2 + R_A^2}",
    )
    doc = Document(id="doc_test", citekey="james1982", title="Bill James Abstract", year=1982)

    compiled = gen.compile_formula(formula, doc=doc)
    assert compiled is not None
    assert "def expr_" in compiled.polars_code
    assert '-> pl.Expr:' in compiled.polars_code
    assert 'pl.col(' in compiled.polars_code


@pytest.mark.asyncio
async def test_formula_library_generator_grade_a_export(tmp_path: Path) -> None:
    """Verify export_to_file respects min_grade='A' filter."""
    import uuid

    from kb.library.generator import FormulaLibraryGenerator
    from kb.storage.database import DatabaseManager
    from kb.storage.models import Document, Formula

    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_codegen_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.session_factory() as session:
        doc = Document(id=f"doc_{db_id}", citekey="james1982", title="Doc", year=1982)
        session.add(doc)

        # Grade A formula (score 92.0)
        f_a = Formula(
            id=f"fa_{db_id}",
            document_id=doc.id,
            citekey="james1982",
            raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            sympy_repr="Eq(W, R_S**2/(R_A**2 + R_S**2))",
            symbols=["R_S", "R_A", "W"],
            is_valid=True,
            is_equality=True,
            validation_score=92.0,
            validation_status="verified",
            lhs="W",
        )
        # Grade F formula (score 20.0)
        f_f = Formula(
            id=f"ff_{db_id}",
            document_id=doc.id,
            citekey="james1982",
            raw_latex=r"X = Y + Z",
            sanitized_latex=r"X = Y + Z",
            sympy_repr="Eq(X, Y + Z)",
            symbols=["X", "Y", "Z"],
            is_valid=True,
            is_equality=True,
            validation_score=20.0,
            validation_status="failed",
            lhs="X",
        )
        session.add(f_a)
        session.add(f_f)
        await session.commit()

    gen = FormulaLibraryGenerator(db_manager=db)
    out_file = tmp_path / "grade_a_formulas.py"
    count = await gen.export_to_file(out_file, min_grade="A")

    assert count == 1
    content = out_file.read_text(encoding="utf-8")
    assert f"calc_w_{f_a.id.replace('-', '')[:6]}" in content
    assert f"calc_x_{f_f.id.replace('-', '')[:6]}" not in content

    await db.close()
