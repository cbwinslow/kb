"""Unit tests for the Performance & Quality Benchmarking Suite."""

from __future__ import annotations

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
