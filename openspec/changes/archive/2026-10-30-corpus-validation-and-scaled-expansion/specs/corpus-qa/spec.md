# Spec Delta: corpus-qa

## ADDED Requirements

### Requirement: Corpus Relational and Storage Invariant Auditing
The system SHALL provide an automated corpus audit harness validating document, chunk, formula, and figure relational integrity across PostgreSQL and remote homelab storage.

#### Scenario: Auditing orphaned entities and vault paths
- **WHEN** user executes `kb corpus audit`
- **THEN** system checks for chunks or formulas without parent documents, documents without chunks, missing remote figure vault files, and unvalidated formulas, returning an invariant health report.

#### Scenario: Emitting structured audit health scorecard
- **WHEN** audit command is executed with `--json` flag
- **THEN** system emits a machine-readable JSON summary reporting total documents, chunks, formulas, figures, benchmark tables, and any identified integrity violations.
