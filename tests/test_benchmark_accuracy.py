"""Unit tests for EmpiricalAccuracyRunner leaderboard generation and re-exports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from kb.benchmark.accuracy import AccuracyMetrics, EmpiricalAccuracyRunner


def test_accuracy_module_reexport() -> None:
    """Verifies that EmpiricalAccuracyRunner and AccuracyMetrics are cleanly re-exported."""
    assert EmpiricalAccuracyRunner is not None
    assert AccuracyMetrics is not None


def test_leaderboard_generation_markdown(tmp_path: Path) -> None:
    """Verifies markdown leaderboard rendering and ranking logic."""
    runner = EmpiricalAccuracyRunner()

    sample_results: list[dict[str, Any]] = [
        {
            "formula_id": "f_pythagorean_01",
            "citekey": "james_1982",
            "target_column": "w_pct",
            "metrics": {
                "r_squared": 0.9850,
                "rmse": 0.0210,
                "mae": 0.0150,
                "passed": True,
                "throughput_rows_per_sec": 450000.0,
            },
        },
        {
            "formula_id": "f_fip_02",
            "citekey": "tango_2006",
            "target_column": "era",
            "metrics": {
                "r_squared": 0.8920,
                "rmse": 0.3800,
                "mae": 0.2900,
                "passed": False,
                "throughput_rows_per_sec": 380000.0,
            },
        },
        {
            "formula_id": "f_woba_03",
            "citekey": "woolner_2005",
            "target_column": "runs_above_avg",
            "metrics": {
                "r_squared": 0.9910,
                "rmse": 0.0120,
                "mae": 0.0090,
                "passed": True,
                "throughput_rows_per_sec": 520000.0,
            },
        },
    ]

    out_file = tmp_path / "accuracy_leaderboard.md"
    md = runner.generate_leaderboard(sample_results, output_path=out_file)

    assert "# Empirical Accuracy Benchmarking Leaderboard" in md
    assert "Ranked Formula Performance" in md
    assert "| 1 |" in md
    # First ranked should be highest R^2 (f_woba_03 with 0.9910)
    assert "`f_woba_03`" in md
    assert "**0.9910**" in md
    assert "**PASSED**" in md
    assert "FLAGGED" in md

    # Verify file was written
    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert content == md

    # Verify companion JSON was written
    json_file = out_file.with_suffix(".json")
    assert json_file.exists()
    json_data = json.loads(json_file.read_text(encoding="utf-8"))
    assert len(json_data) == 3
    assert json_data[0]["formula_id"] == "f_woba_03"


def test_leaderboard_generation_json_direct(tmp_path: Path) -> None:
    """Verifies direct JSON leaderboard generation when output path ends with .json."""
    runner = EmpiricalAccuracyRunner()

    sample_results: list[dict[str, Any]] = [
        {
            "formula_id": "f_model_1",
            "citekey": "author_2020",
            "metrics": {
                "r_squared": 0.9600,
                "rmse": 0.0500,
                "mae": 0.0400,
                "passed": True,
                "throughput_rows_per_sec": 100000.0,
            },
        }
    ]

    out_json = tmp_path / "benchmarks" / "leaderboard.json"
    md = runner.generate_leaderboard(sample_results, output_path=out_json)
    assert "# Empirical Accuracy Benchmarking Leaderboard" in md

    assert out_json.exists()
    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["formula_id"] == "f_model_1"


def test_leaderboard_empty_results() -> None:
    """Verifies graceful handling of empty or un-evaluated benchmark results."""
    runner = EmpiricalAccuracyRunner()
    md = runner.generate_leaderboard([])
    assert "# Empirical Accuracy Benchmarking Leaderboard" in md
    assert "**Total Formulas Evaluated**: 0" in md
    assert "**Top Model R²**: N/A" in md
