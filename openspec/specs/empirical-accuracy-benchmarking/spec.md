# Empirical Accuracy Benchmarking Specification

## Purpose
Quantify the mathematical accuracy and empirical predictive fidelity of extracted formulas against real-world tabular data fixtures (Parquet/CSV) using vectorized Polars evaluation.

## Requirements

### Requirement 1: Dataset Dynamic Column Binding
`EmpiricalAccuracyRunner` MUST dynamically map formula symbols to dataset column names and resolve standard physical/mathematical constants without manual user coding.

### Requirement 2: Vectorized Expression Compilation
Formula ASTs MUST compile directly into native Polars expression trees (`polars.Expr`), executing calculations across millions of rows in C++/Rust without Python per-row iteration loops.

### Requirement 3: Empirical Error Metrics
The runner MUST calculate:
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **Max Relative Error**
- **Coefficient of Determination ($R^2$)**

### Requirement 4: Quality Gate Credit Scoring
High empirical fidelity ($R^2 \ge 0.85$ or low relative error) MUST award Tier 4 score credits to formulas in `kb_formulas.validation_details`, raising their quality score toward Grade A.

### Requirement 5: Heuristic Fuzzy Column Matching
The `EmpiricalAccuracyRunner` MUST employ fuzzy string matching and domain symbol synonym dictionaries to resolve naming discrepancies between mathematical AST symbols and tabular tracking columns.

#### Scenario: Auto-binding abbreviated trajectory columns
- **WHEN** a formula uses mathematical symbol `v_0` and a dataset contains column `exit_velocity`
- **THEN** the fuzzy matcher maps the symbol to the column based on the registered ontology alias without manual user intervention

### Requirement 6: Golden Tracking Fixture Auto-Registration
The benchmarking suite SHALL automatically register and discover real-world tracking datasets in `data/fixtures/` and evaluate all matching Grade A formulas without requiring explicit CLI dataset path flags.

#### Scenario: Running batch empirical benchmark across all fixtures
- **WHEN** user executes `kb benchmark accuracy --all`
- **THEN** the runner discovers available Parquet fixtures, matches relevant formulas, and produces comprehensive MAE, RMSE, and $R^2$ scorecards

