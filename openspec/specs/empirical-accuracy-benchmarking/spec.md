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
