# Spec Delta: numerical-accuracy

## ADDED Requirements

### Requirement: Vectorized Corpus Benchmark Evaluation
The system SHALL evaluate compiled vectorized formula expressions against large-scale empirical Parquet datasets, calculating statistical agreement metrics including MAE, RMSE, and coefficient of determination $R^2$.

#### Scenario: Batch verification against Parquet benchmark datasets
- **WHEN** evaluating a compiled Grade A formula against a multi-row empirical Parquet dataset
- **THEN** system executes vectorized Polars evaluation and confirms calculated values match expected outputs within tolerance $\epsilon \le 10^{-4}$

#### Scenario: Statistical accuracy metric computation
- **WHEN** an empirical benchmark evaluation finishes
- **THEN** system records MAE, RMSE, max relative error, and $R^2$ into the formula's validation details payload in PostgreSQL
