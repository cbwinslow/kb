# numerical-accuracy Specification

## Purpose
Validates mathematical calculations of compiled formula functions against established empirical and theoretical benchmark values.

## Requirements

### Requirement: Reference Benchmark Validation
The system SHALL verify compiled formula functions against canonical sports science and sabermetric benchmarks within a strict relative numerical tolerance ($\le 10^{-4}$).

#### Scenario: Validating Pythagorean Expectation
- **WHEN** Pythagorean formula is evaluated with 750 runs scored, 650 runs allowed, and exponent 1.83
- **THEN** calculated win percentage equals $0.5647 \pm 10^{-4}$

#### Scenario: Validating FIP Calculation
- **WHEN** FIP formula is evaluated with 20 HR, 50 BB, 5 HBP, 180 K, 200 IP, and FIP constant 3.10
- **THEN** calculated value matches expected defense-independent ERA within $10^{-4}$ tolerance

### Requirement: Vectorized Corpus Benchmark Evaluation
The system SHALL evaluate compiled vectorized formula expressions against large-scale empirical Parquet datasets, calculating statistical agreement metrics including MAE, RMSE, and coefficient of determination $R^2$.

#### Scenario: Batch verification against Parquet benchmark datasets
- **WHEN** evaluating a compiled Grade A formula against a multi-row empirical Parquet dataset
- **THEN** system executes vectorized Polars evaluation and confirms calculated values match expected outputs within tolerance $\epsilon \le 10^{-4}$

#### Scenario: Statistical accuracy metric computation
- **WHEN** an empirical benchmark evaluation finishes
- **THEN** system records MAE, RMSE, max relative error, and $R^2$ into the formula's validation details payload in PostgreSQL
