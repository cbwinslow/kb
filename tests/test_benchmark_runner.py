"""Unit tests for the Performance & Quality Benchmarking Suite."""

from __future__ import annotations

from pathlib import Path

import pytest

from kb.benchmark.runner import (
    BenchmarkSuiteResult,
    FormulaBenchmarkResult,
    PerformanceBenchmarker,
    QualityBenchmarkResult,
)


def test_formula_execution_benchmarks() -> None:
    benchmarker = PerformanceBenchmarker()
    results = benchmarker.benchmark_formula_execution(n_rows=10_000)

    assert len(results) >= 2
    for r in results:
        assert isinstance(r, FormulaBenchmarkResult)
        assert r.n_rows == 10_000
        assert r.scalar_time_ms > 0
        assert r.polars_time_ms > 0
        assert r.speedup_factor > 0
        assert r.polars_throughput_rows_per_sec > 0


def test_suite_result_formatting() -> None:
    suite = BenchmarkSuiteResult(
        timestamp="2026-10-26T00:00:00Z",
        formula_benchmarks=[
            FormulaBenchmarkResult(
                function_name="pythagorean_test",
                n_rows=1000,
                scalar_time_ms=5.0,
                polars_time_ms=1.0,
                scalar_throughput_rows_per_sec=200000.0,
                polars_throughput_rows_per_sec=1000000.0,
                speedup_factor=5.0,
            )
        ],
        embedding_benchmark=None,
        search_benchmark=None,
        quality_benchmark=QualityBenchmarkResult(
            total_formulas=5000,
            verified_valid=1000,
            valid_ratio=0.20,
            equalities_count=300,
            equality_ratio=0.06,
            compilable_count=800,
            compilation_ratio=0.80,
        ),
    )

    md = suite.to_markdown()
    assert "# KB Performance & Quality Benchmark Report" in md
    assert "`pythagorean_test`" in md
    assert "**5.0x**" in md
    assert "Corpus Formula Quality Scorecard" in md
    assert "**Total Formulas**: 5,000" in md

    json_str = suite.to_json()
    assert '"function_name": "pythagorean_test"' in json_str
    assert '"total_formulas": 5000' in json_str


@pytest.mark.asyncio
async def test_corpus_quality_benchmark() -> None:
    benchmarker = PerformanceBenchmarker()
    quality = await benchmarker.benchmark_corpus_quality()

    assert isinstance(quality, QualityBenchmarkResult)
    assert quality.total_formulas >= 0
    assert 0.0 <= quality.valid_ratio <= 1.0


@pytest.fixture
def sample_dataset(tmp_path: Path) -> Path:
    """Create a sample Parquet dataset fixture for testing Pythagorean Expectation."""
    import polars as pl

    df = pl.DataFrame(
        {
            "runs_scored": [800.0, 700.0, 900.0, 650.0],
            "runs_allowed": [600.0, 700.0, 600.0, 750.0],
            "win_pct": [
                0.64,
                0.50,
                810000.0 / 1170000.0,
                (650.0**2) / (650.0**2 + 750.0**2),
            ],
        }
    )
    pq_path = tmp_path / "pythag_sample.parquet"
    df.write_parquet(pq_path)
    return pq_path


def test_bind_formula_to_table() -> None:
    """Verify SymbolOntology binds table columns to formula symbols."""
    from kb.qa.accuracy import EmpiricalAccuracyRunner
    from kb.storage.models import Formula

    runner = EmpiricalAccuracyRunner()
    formula = Formula(
        id="f_test_bind",
        document_id="doc_1",
        citekey="james1980",
        raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        symbols=["R_S", "R_A", "W"],
        lhs="W",
        is_valid=True,
    )
    cols = ["runs_scored", "runs_allowed", "win_pct"]
    res = runner.bind_formula_to_table(formula, columns=cols, target_candidate="win_pct")

    assert res.is_bound
    assert res.target_column == "win_pct"
    assert "R_S" in res.matched_columns
    assert res.matched_columns["R_S"] == "runs_scored"
    assert "R_A" in res.matched_columns
    assert res.matched_columns["R_A"] == "runs_allowed"
    assert len(res.missing_symbols) == 0


def test_evaluate_vectorized(sample_dataset: Path) -> None:
    """Verify vectorized Polars evaluation calculates accurate MAE, RMSE, and R^2."""
    import polars as pl

    from kb.qa.accuracy import EmpiricalAccuracyRunner
    from kb.storage.models import Formula

    runner = EmpiricalAccuracyRunner()
    formula = Formula(
        id="f_test_eval",
        document_id="doc_1",
        citekey="james1980",
        raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
        symbols=["R_S", "R_A", "W"],
        lhs="W",
        is_valid=True,
    )
    df = pl.read_parquet(sample_dataset)
    param_map = {"R_S": "runs_scored", "R_A": "runs_allowed"}

    metrics = runner.evaluate_vectorized(
        df=df,
        formula=formula,
        target_column="win_pct",
        param_mapping=param_map,
    )

    assert metrics.num_samples == 4
    assert metrics.mae < 1e-4
    assert metrics.rmse < 1e-4
    assert metrics.r_squared >= 0.999
    assert metrics.passed is True
    assert metrics.throughput_rows_per_sec > 0


@pytest.mark.asyncio
async def test_benchmark_corpus_against_dataset(sample_dataset: Path) -> None:
    """Verify benchmark_corpus runs across formulas and reports telemetry."""
    import uuid

    from kb.qa.accuracy import EmpiricalAccuracyRunner
    from kb.storage.database import DatabaseManager
    from kb.storage.models import Document, Formula

    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_bench_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.session_factory() as session:
        doc = Document(id=f"doc_{db_id}", citekey="james1980", title="Bill James", year=1980)
        session.add(doc)
        formula = Formula(
            id=f"f_bench_{db_id}",
            document_id=doc.id,
            citekey="james1980",
            raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            symbols=["R_S", "R_A", "W"],
            lhs="W",
            is_valid=True,
            is_equality=True,
            validation_score=95.0,
            validation_status="verified",
        )
        session.add(formula)
        await session.commit()

    runner = EmpiricalAccuracyRunner(db_manager=db)
    results = await runner.benchmark_corpus(
        min_grade="A",
        min_score=88.0,
        dataset_path=sample_dataset,
        target_column="win_pct",
    )

    assert len(results) == 1
    assert results[0]["formula_id"] == f"f_bench_{db_id}"
    assert results[0]["metrics"]["passed"] is True
    assert results[0]["metrics"]["r_squared"] >= 0.99

    await db.close()


def test_cli_benchmark_accuracy_help(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify 'kb benchmark accuracy --help' displays options."""
    from kb.cli import main

    with pytest.raises(SystemExit) as exc:
        main(["benchmark", "--help"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "accuracy" in captured.out
    assert "--grade" in captured.out
    assert "--dataset" in captured.out

