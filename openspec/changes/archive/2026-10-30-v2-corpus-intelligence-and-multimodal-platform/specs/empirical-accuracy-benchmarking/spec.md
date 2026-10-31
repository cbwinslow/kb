# Spec Delta: Empirical Accuracy Benchmarking

## ADDED Requirements

### Requirement: Heuristic Fuzzy Column Matching
The `EmpiricalAccuracyRunner` MUST employ fuzzy string matching and domain symbol synonym dictionaries to resolve naming discrepancies between mathematical AST symbols and tabular tracking columns.

#### Scenario: Auto-binding abbreviated trajectory columns
- **WHEN** a formula uses mathematical symbol `v_0` and a dataset contains column `exit_velocity`
- **THEN** the fuzzy matcher maps the symbol to the column based on the registered ontology alias without manual user intervention

### Requirement: Golden Tracking Fixture Auto-Registration
The benchmarking suite SHALL automatically register and discover real-world tracking datasets in `data/fixtures/` and evaluate all matching Grade A formulas without requiring explicit CLI dataset path flags.

#### Scenario: Running batch empirical benchmark across all fixtures
- **WHEN** user executes `kb benchmark accuracy --all`
- **THEN** the runner discovers available Parquet fixtures, matches relevant formulas, and produces comprehensive MAE, RMSE, and $R^2$ scorecards
