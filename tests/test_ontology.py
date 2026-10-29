"""Tests for semantic symbol ontology and DataFrame column binding."""

from __future__ import annotations

import polars as pl
import pytest

from kb.math.ontology import (
    CanonicalConcept,
    ConceptDefinition,
    SymbolOntology,
    get_symbol_ontology,
    map_dataframe_columns,
    resolve_canonical,
)


def test_symbol_normalization() -> None:
    """Verify robust LaTeX and string symbol normalization."""
    ont = SymbolOntology()

    assert ont.normalize_symbol(r"\text{RS}") == "rs"
    assert ont.normalize_symbol(r"\mathrm{HR}") == "hr"
    assert ont.normalize_symbol(r"R_{S}") == "r_s"
    assert ont.normalize_symbol(r"$H_R$") == "h_r"
    assert ont.normalize_symbol("runs_scored") == "runs_scored"
    assert ont.normalize_symbol("") == ""


def test_canonical_resolution() -> None:
    """Verify resolution of heterogeneous author notations to CanonicalConcept."""
    ont = get_symbol_ontology()

    # Runs Scored
    assert ont.resolve_canonical("R_S") == CanonicalConcept.RUNS_SCORED
    assert ont.resolve_canonical("RS") == CanonicalConcept.RUNS_SCORED
    assert ont.resolve_canonical(r"\text{RS}") == CanonicalConcept.RUNS_SCORED
    assert ont.resolve_canonical("runs_scored") == CanonicalConcept.RUNS_SCORED
    assert resolve_canonical("runs") == CanonicalConcept.RUNS_SCORED

    # Runs Allowed
    assert ont.resolve_canonical("R_A") == CanonicalConcept.RUNS_ALLOWED
    assert ont.resolve_canonical("RA") == CanonicalConcept.RUNS_ALLOWED
    assert ont.resolve_canonical("runs_allowed") == CanonicalConcept.RUNS_ALLOWED

    # Home Runs, Walks, Strikeouts, Innings Pitched
    assert ont.resolve_canonical("H_R") == CanonicalConcept.HOME_RUNS
    assert ont.resolve_canonical(r"\text{HR}") == CanonicalConcept.HOME_RUNS
    assert ont.resolve_canonical("B_B") == CanonicalConcept.WALKS
    assert ont.resolve_canonical("BB") == CanonicalConcept.WALKS
    assert ont.resolve_canonical("K") == CanonicalConcept.STRIKEOUTS
    assert ont.resolve_canonical("SO") == CanonicalConcept.STRIKEOUTS
    assert ont.resolve_canonical("I_P") == CanonicalConcept.INNINGS_PITCHED
    assert ont.resolve_canonical("IP") == CanonicalConcept.INNINGS_PITCHED
    assert ont.resolve_canonical(r"\gamma") == CanonicalConcept.GAMMA
    assert ont.resolve_canonical("gamma") == CanonicalConcept.GAMMA

    # Non-existent symbol returns None
    assert ont.resolve_canonical("xyz_completely_unknown_symbol_123") is None


def test_resolve_column_mapping() -> None:
    """Verify formula symbol to available DataFrame column resolution."""
    ont = get_symbol_ontology()

    # Empirical dataset columns from a database or Retrosheet
    df_cols = ["runs_scored", "runs_allowed", "team_id", "year"]
    formula_symbols = ["R_S", "R_A"]

    mapping = ont.resolve_column_mapping(formula_symbols, df_cols)
    assert mapping == {"R_S": "runs_scored", "R_A": "runs_allowed"}

    # Mixed abbreviations
    df_cols_pitching = ["hr", "bb", "so", "ip", "pitcher_name"]
    pitching_symbols = ["H_R", "B_B", "K", "I_P"]
    mapping_pitching = ont.resolve_column_mapping(pitching_symbols, df_cols_pitching)
    assert mapping_pitching == {"H_R": "hr", "B_B": "bb", "K": "so", "I_P": "ip"}


def test_polars_dataframe_binding_and_evaluation() -> None:
    """Verify Polars DataFrame automatic binding and subsequent expression evaluation."""
    # Create raw DataFrame with standard data warehouse column names
    raw_df = pl.DataFrame(
        {
            "team": ["NYY", "BOS", "LAD"],
            "runs_scored": [800.0, 750.0, 840.0],
            "runs_allowed": [650.0, 720.0, 610.0],
        }
    )

    # Expected formula symbols generated from LaTeX: W = R_S^2 / (R_S^2 + R_A^2)
    formula_symbols = ["R_S", "R_A"]

    # Bind DataFrame using ontology
    bound_df = map_dataframe_columns(raw_df, formula_symbols)

    assert "R_S" in bound_df.columns
    assert "R_A" in bound_df.columns
    assert "runs_scored" in bound_df.columns

    # Evaluate formula directly against bound DataFrame without errors
    pythag_expr = (pl.col("R_S") ** 2) / (pl.col("R_S") ** 2 + pl.col("R_A") ** 2)
    result_df = bound_df.with_columns(pythag_expr.alias("win_expectancy"))

    win_exp = result_df["win_expectancy"].to_list()
    assert len(win_exp) == 3
    # NYY: 800^2 / (800^2 + 650^2) = 640000 / (640000 + 422500) = 0.60235
    assert pytest.approx(win_exp[0], rel=1e-3) == 0.60235


def test_custom_concept_registration() -> None:
    """Verify custom user concept can be registered into ontology."""
    ont = SymbolOntology()
    custom = ConceptDefinition(
        canonical_name=CanonicalConcept.ERRORS,
        latex_repr="E",
        aliases=["E", "errors", "fielding_errors", "errs"],
        description="Fielding errors.",
    )
    ont.register(custom)

    assert ont.resolve_canonical("fielding_errors") == CanonicalConcept.ERRORS
    assert ont.resolve_canonical("errs") == CanonicalConcept.ERRORS


def test_statcast_and_situational_resolution() -> None:
    """Verify resolution of modern Statcast 2.0 and situational sabermetric metrics."""
    ont = get_symbol_ontology()

    # Bat Tracking & Physics
    assert ont.resolve_canonical("v_bat") == CanonicalConcept.BAT_SPEED
    assert ont.resolve_canonical("bat_speed") == CanonicalConcept.BAT_SPEED
    assert ont.resolve_canonical("swing_length") == CanonicalConcept.SWING_LENGTH
    assert ont.resolve_canonical("attack_angle") == CanonicalConcept.ATTACK_ANGLE
    assert ont.resolve_canonical("fast_swing_rate") == CanonicalConcept.FAST_SWING_RATE
    assert ont.resolve_canonical("blast_rate") == CanonicalConcept.BLAST_RATE
    assert ont.resolve_canonical("squared_up") == CanonicalConcept.SQUARED_UP_RATE
    assert ont.resolve_canonical("exit_velocity") == CanonicalConcept.EXIT_VELOCITY
    assert ont.resolve_canonical("launch_speed") == CanonicalConcept.EXIT_VELOCITY

    # Situational Metrics
    assert ont.resolve_canonical("LI") == CanonicalConcept.LEVERAGE_INDEX
    assert ont.resolve_canonical("leverage_index") == CanonicalConcept.LEVERAGE_INDEX
    assert ont.resolve_canonical("RE") == CanonicalConcept.RUN_EXPECTANCY
    assert ont.resolve_canonical("run_expectancy") == CanonicalConcept.RUN_EXPECTANCY
