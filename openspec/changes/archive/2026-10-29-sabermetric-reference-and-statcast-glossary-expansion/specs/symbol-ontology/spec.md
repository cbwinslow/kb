# Spec Delta: symbol-ontology

## ADDED Requirements

### Requirement: Statcast and Situational Canonical Concepts
The system SHALL maintain canonical concept definitions and aliases for modern Statcast tracking metrics (bat speed, swing length, attack angle, fast swing rate, squared up rate, blast rate) and situational sabermetric metrics (leverage index, run expectancy).

#### Scenario: Resolving Statcast bat tracking metrics
- **WHEN** variables such as $v_{bat}$, $v_{exit}$, or $\text{BatSpeed}$ are resolved
- **THEN** system maps them to canonical concepts 'bat_speed' and 'exit_velocity'

#### Scenario: Resolving situational run expectancy and leverage
- **WHEN** variables such as $\Delta RE$, $RE$, $LI$, or $WPA$ are resolved
- **THEN** system maps them to canonical concepts 'run_expectancy' and 'leverage_index'
