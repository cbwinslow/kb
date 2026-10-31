"""Unit tests for HeuristicColumnMatcher, fixture discovery, and auto-binding empirical accuracy."""

from __future__ import annotations

import tempfile
from pathlib import Path

import polars as pl
import pytest

from kb.qa.accuracy import (
    EmpiricalAccuracyRunner,
    HeuristicColumnMatcher,
    discover_fixtures,
)
from kb.storage.models import Formula


@pytest.fixture
def matcher() -> HeuristicColumnMatcher:
    """Fixture providing a HeuristicColumnMatcher instance."""
    return HeuristicColumnMatcher()


@pytest.fixture
def runner() -> EmpiricalAccuracyRunner:
    """Fixture providing an EmpiricalAccuracyRunner instance."""
    return EmpiricalAccuracyRunner()


def test_heuristic_matcher_direct_and_normalized(matcher: HeuristicColumnMatcher) -> None:
    """Verify direct and case-insensitive column matching."""
    cols = ["Exit_Velocity", "Launch_Angle", "Distance"]
    assert matcher.match_column("exit_velocity", cols) == "Exit_Velocity"
    assert matcher.match_column("Launch_Angle", cols) == "Launch_Angle"


def test_heuristic_matcher_domain_synonyms(matcher: HeuristicColumnMatcher) -> None:
    """Verify domain symbol synonyms resolve to empirical column headers."""
    cols = ["pitch_id", "exit_velocity", "launch_angle", "hit_distance_sc", "spin_rate"]

    # Trajectory speed v_0 -> exit_velocity
    assert matcher.match_column("v_0", cols) == "exit_velocity"
    assert matcher.match_column("v0", cols) == "exit_velocity"
    assert matcher.match_column("launch_speed", cols) == "exit_velocity"

    # Angle theta -> launch_angle
    assert matcher.match_column("theta", cols) == "launch_angle"

    # Distance x -> hit_distance_sc
    assert matcher.match_column("x", cols) == "hit_distance_sc"
    assert matcher.match_column("dist", cols) == "hit_distance_sc"

    # Spin rate omega -> spin_rate
    assert matcher.match_column("omega", cols) == "spin_rate"


def test_heuristic_matcher_fuzzy_levenshtein(matcher: HeuristicColumnMatcher) -> None:
    """Verify fuzzy matching resolves minor typographic variations."""
    cols = ["exit_velocity_mph", "horizontal_break_in", "plate_loc_x"]
    # Close token match for velocity
    matched = matcher.match_column("exit_velocity", cols, threshold=0.7)
    assert matched == "exit_velocity_mph"


def test_discover_fixtures_temporary_directory() -> None:
    """Verify that discover_fixtures scans parquet files and extracts schemas lazily."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        sub_dir = tmp_path / "sample_paper"
        sub_dir.mkdir(parents=True)

        pq_file = sub_dir / "tracking_table_01.parquet"
        df = pl.DataFrame({
            "exit_velocity": [95.0, 102.5, 88.0],
            "launch_angle": [22.0, 18.0, 31.0],
            "hit_distance_sc": [380.0, 410.0, 320.0],
        })
        df.write_parquet(pq_file)

        fixtures = discover_fixtures(tmp_path)
        assert len(fixtures) == 1
        assert fixtures[0]["name"] == "tracking_table_01"
        assert fixtures[0]["format"] == "parquet"
        assert "exit_velocity" in fixtures[0]["columns"]
        assert "launch_angle" in fixtures[0]["columns"]


def test_bind_formula_to_table_with_heuristics(runner: EmpiricalAccuracyRunner) -> None:
    """Verify auto-binding of mathematical formula to empirical tracking table."""
    formula = Formula(
        id="f_test_trajectory",
        citekey="nathan2008",
        raw_latex=r"d = v_0 \cdot \cos(\theta) \cdot t",
        sanitized_latex=r"d = v_0 \cdot \cos(\theta) \cdot t",
        symbols=["v_0", "theta", "t"],
        lhs="d",
        rhs=r"v_0 \cdot \cos(\theta) \cdot t",
        is_valid=True,
    )

    columns = ["exit_velocity", "launch_angle", "t", "hit_distance_sc"]
    binding = runner.bind_formula_to_table(formula, columns)

    assert binding.is_bound is True
    assert binding.target_column == "hit_distance_sc"
    assert binding.matched_columns.get("v_0") == "exit_velocity"
    assert binding.matched_columns.get("theta") == "launch_angle"
    assert binding.matched_columns.get("t") == "t"


def test_evaluate_vectorized_metrics(runner: EmpiricalAccuracyRunner) -> None:
    """Verify vectorized Polars expression evaluation and accuracy metrics computation."""
    formula = Formula(
        id="f_test_linear",
        citekey="test2024",
        raw_latex=r"y = 2 \cdot x + 1",
        sanitized_latex=r"y = 2 \cdot x + 1",
        symbols=["x"],
        lhs="y",
        rhs="2*x + 1",
        is_valid=True,
    )

    df = pl.DataFrame({
        "input_x": [1.0, 2.0, 3.0, 4.0, 5.0],
        "ground_truth_y": [3.0, 5.0, 7.0, 9.0, 11.0],
    })

    metrics = runner.evaluate_vectorized(
        df=df,
        formula=formula,
        target_column="ground_truth_y",
        param_mapping={"x": "input_x"},
    )

    assert metrics.passed is True
    assert metrics.mae == pytest.approx(0.0, abs=1e-5)
    assert metrics.rmse == pytest.approx(0.0, abs=1e-5)
    assert metrics.r_squared == pytest.approx(1.0, abs=1e-5)
    assert metrics.num_samples == 5
    assert metrics.throughput_rows_per_sec > 0
