# Spec Delta: web-glossary-harvester

## ADDED Requirements

### Requirement: Advanced Sabermetric and Statcast 2.0 Presets
The system SHALL provide canonical presets covering Tom Tango's 24-state Run Expectancy (RE24) matrices, Leverage Index (LI), Baseball Prospectus DRC+/DRA, Baseball-Reference WAR components, and Statcast 2.0 bat tracking collision mechanics.

#### Scenario: Ingesting Tom Tango RE24 and Leverage Index presets
- **WHEN** preset 'tangotiger_re24' or 'tangotiger_leverage_index' is ingested
- **THEN** system successfully extracts and symbolically validates run expectancy transition formulas and leverage index calculations

#### Scenario: Ingesting Statcast 2.0 bat tracking mechanics preset
- **WHEN** preset 'statcast_bat_tracking' is ingested
- **THEN** system extracts exit velocity collision physics, squared-up rate, and blast percentage equations into SymPy ASTs
