# Spec Delta: empirical-accuracy-benchmarking

## ADDED Requirements

### Requirement: Empirical Accuracy Leaderboard Reporting
The empirical accuracy benchmarking engine SHALL generate structured leaderboard artifacts in Markdown and JSON formats, ranking evaluated formulas by $R^2$, RMSE, and empirical coverage.

#### Scenario: Generating global accuracy leaderboard
- **WHEN** user executes `kb benchmark accuracy --all --output data/benchmarks/accuracy_leaderboard.md`
- **THEN** system evaluates all matching Grade A formulas against Parquet fixtures, writes the formatted leaderboard report, and summarizes top-performing quantitative models

### Requirement: Web UI Empirical Accuracy Score Display
The Web UI dashboard SHALL surface empirical accuracy metrics ($R^2$, MAE, RMSE) and validation badges on formula entity rows and detail drawers.

#### Scenario: Viewing empirical accuracy in formula table
- **WHEN** user inspects a formula in the Web UI Formulas tab that has empirical benchmark results
- **THEN** system displays an empirical fidelity badge ($R^2$ score) alongside symbolic quality grades
