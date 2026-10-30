# Specification: Semantic Symbol Ontology & Column Mapping

## Purpose
Provides an authoritative semantic mapping layer bridging academic literature mathematical notations (heterogeneous author LaTeX variables like $R_S, \text{RS}, R, r, H_R, \text{HR}, I_P, \text{IP}$) with standard data engineering columns found in empirical sabermetric datasets (such as Retrosheet, Statcast, Chadwick, and `baseballpy`).

## Requirements

1. **Canonical Concept Registry**:
   - MUST maintain definitions for canonical baseball concepts including `runs_scored`, `runs_allowed`, `home_runs`, `innings_pitched`, `strikeouts`, `walks`, `hits`, `at_bats`, `plate_appearances`, `singles`, `doubles`, `triples`, `win_pct`, and `gamma`.
   - Each concept MUST include canonical identifiers, typical LaTeX display forms, aliases, descriptions, and value domains.
2. **Robust Symbol Resolution**:
   - `SymbolOntology.resolve_canonical(symbol: str)` MUST resolve variations including LaTeX formatted strings (`R_S`, `\text{RS}`, `\mathrm{HR}`), subscripts, and case variations.
   - Ambiguous or unknown symbols MUST fall back gracefully without raising unexpected unhandled exceptions.
3. **DataFrame Binding**:
   - `SymbolOntology.bind_dataframe(df, formula_symbols)` MUST automatically inspect incoming DataFrame columns (supporting Polars `pl.DataFrame` and Pandas `pd.DataFrame`) and map matching canonical columns to the formula's parameter names.
   - If a column already matches, it MUST be preserved.
   - If an alias exists in the DataFrame, it MUST be made accessible under the formula parameter name via alias column creation or renaming.
4. **Integration**:
   - MUST be exposed for programmatic use in `kb.math.ontology` and available for formula evaluation pipelines.

### Requirement: Statcast and Situational Canonical Concepts
The system SHALL maintain canonical concept definitions and aliases for modern Statcast tracking metrics (bat speed, swing length, attack angle, fast swing rate, squared up rate, blast rate) and situational sabermetric metrics (leverage index, run expectancy).

#### Scenario: Resolving Statcast bat tracking metrics
- **WHEN** variables such as $v_{bat}$, $v_{exit}$, or $\text{BatSpeed}$ are resolved
- **THEN** system maps them to canonical concepts 'bat_speed' and 'exit_velocity'

#### Scenario: Resolving situational run expectancy and leverage
- **WHEN** variables such as $\Delta RE$, $RE$, $LI$, or $WPA$ are resolved
- **THEN** system maps them to canonical concepts 'run_expectancy' and 'leverage_index'

### Requirement: Universal Physical and Statistical Scientific Concepts
The system SHALL maintain canonical concept definitions and extensive aliases for foundational physical, aerodynamic, and statistical variables in addition to sabermetric metrics.

#### Scenario: Resolving foundational physical symbols
- **WHEN** variables such as $v, a, t, m, F, \rho, C_d, \omega, r, d$ are resolved
- **THEN** the system maps them to canonical concepts 'velocity', 'acceleration', 'time', 'mass', 'force', 'air_density', 'drag_coefficient', 'angular_velocity', 'radius_distance'

#### Scenario: Resolving foundational statistical symbols
- **WHEN** variables such as $P, p, \mu, \sigma, N, n$ are resolved
- **THEN** the system maps them to canonical concepts 'probability', 'mean', 'variance_stddev', 'sample_size'
