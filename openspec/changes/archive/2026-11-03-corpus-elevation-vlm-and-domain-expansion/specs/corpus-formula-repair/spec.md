# Spec Delta: corpus-formula-repair

## ADDED Requirements

### Requirement: Targeted Grade-F Formula AST Recovery
The system SHALL provide targeted AST recovery for Grade-F formulas by applying advanced Sanitizer V3 piecewise rules, stack-based delimiter repair, acronym protection, and equation array unwrapping.

#### Scenario: Recovering piecewise and delimited LaTeX equations
- **WHEN** a Grade-F formula containing unclosed delimiters or piecewise `cases` environments is processed by the repair engine
- **THEN** the system rebalances delimiters, extracts valid SymPy representations, updates the formula AST, and elevates the formula validation score and letter grade above Grade F

#### Scenario: Standalone library synchronization after repair
- **WHEN** batch formula repair recovers new Grade A equations
- **THEN** the system allows recompiling the standalone formula distribution library to include all newly verified formulas
