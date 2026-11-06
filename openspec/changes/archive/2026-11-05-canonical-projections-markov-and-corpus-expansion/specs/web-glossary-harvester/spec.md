# Spec Delta: web-glossary-harvester

## ADDED Requirements

### Requirement: Forecasting Systems and Markov Presets
The system SHALL provide canonical presets covering PECOTA (Nate Silver / BP), ZiPS (Dan Szymborski), Marcel the Monkey (Tom Tango), and 24-state discrete Markov chain transitions (Bukiet et al. 1997).

#### Scenario: Ingesting forecasting and Markov modeling presets
- **WHEN** user or pipeline executes `kb ingest glossary --preset <name>` for 'pecota_projections', 'zips_projections', 'marcel_projections', or 'markov_chain_baseball'
- **THEN** system ingests structured methodology specifications, extracts verified LaTeX formulas into `kb_formulas`, and preserves mathematical provenance
