# Empirical Accuracy Benchmarking Specification

## Purpose
Quantify the mathematical accuracy and empirical predictive fidelity of extracted formulas against real-world tabular data fixtures (Parquet/CSV) using vectorized Polars evaluation.

## Requirements

### Requirement: Dataset Dynamic Column Binding
`EmpiricalAccuracyRunner` MUST dynamically map formula symbols to dataset column names and resolve standard physical/mathematical constants without manual user coding.

#### Scenario: Auto-binding formula symbols to dataset columns
- **WHEN** runner evaluates a formula against a dataset fixture
- **THEN** runner dynamically binds formula parameters to matching columns and constants

### Requirement: Vectorized Expression Compilation
Formula ASTs MUST compile directly into native Polars expression trees (`polars.Expr`), executing calculations across millions of rows in C++/Rust without Python per-row iteration loops.

#### Scenario: Compiling formula AST to Polars expression
- **WHEN** formula expression is compiled for tabular evaluation
- **THEN** system produces a native Polars expression tree executing across all rows in Rust

### Requirement: Empirical Error Metrics
The runner MUST calculate Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Max Relative Error, and Coefficient of Determination ($R^2$).

#### Scenario: Computing regression error metrics
- **WHEN** formula predictions are evaluated against ground-truth target columns
- **THEN** system computes MAE, RMSE, max relative error, and R² scores

### Requirement: Quality Gate Credit Scoring
High empirical fidelity ($R^2 \ge 0.85$ or low relative error) MUST award Tier 4 score credits to formulas in `kb_formulas.validation_details`, raising their quality score toward Grade A.

#### Scenario: Awarding quality gate score credits
- **WHEN** a formula achieves an R² score >= 0.85 on empirical data
- **THEN** formula quality gate awards Tier 4 accuracy score credits

### Requirement: Heuristic Fuzzy Column Matching
The `EmpiricalAccuracyRunner` MUST employ fuzzy string matching and domain symbol synonym dictionaries to resolve naming discrepancies between mathematical AST symbols and tabular tracking columns.

#### Scenario: Auto-binding abbreviated trajectory columns
- **WHEN** a formula uses mathematical symbol `v_0` and a dataset contains column `exit_velocity`
- **THEN** the fuzzy matcher maps the symbol to the column based on the registered ontology alias without manual user intervention

### Requirement 6: Golden Tracking Fixture Auto-Registration
The benchmarking suite SHALL automatically register and discover real-world tracking datasets in `data/fixtures/` and evaluate all matching Grade A formulas without requiring explicit CLI dataset path flags.

#### Scenario: Running batch empirical benchmark across all fixtures
- **WHEN** user executes `kb benchmark accuracy --all`
- **THEN** the runner discovers available Parquet fixtures, matches relevant formulas, and produces comprehensive MAE, RMSE, and $R^2$ scorecards

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
