# corpus-qa Specification

## Purpose
Provides evidence-grounded question answering over the scientific literature corpus by synthesizing retrieved text chunks, equations, and bibliographic citations.

## Requirements

### Requirement: Evidence-Grounded Answer Synthesis
The system SHALL answer research queries by combining dense BGE-M3 and sparse lexical search results, attributing claims directly to cited paper sections.

#### Scenario: Answering a research query via CLI
- **WHEN** user executes `kb ask "How is park-adjusted win probability calculated?" --top-k 5`
- **THEN** system retrieves relevant chunks, generates a synthesis with citekeys, chunk IDs, and page references, and prints the grounded answer

### Requirement: Structured JSON Response
The system SHALL support structured machine-readable JSON output for AI assistant integration.

#### Scenario: Querying question answering with --json flag
- **WHEN** user or script invokes `kb ask "<question>" --json`
- **THEN** system returns JSON containing question, synthesized answer, list of sources (citekey, title, authors, chunk_id), and confidence scores

### Requirement: Corpus Relational and Storage Invariant Auditing
The system SHALL provide an automated corpus audit harness validating document, chunk, formula, and figure relational integrity across PostgreSQL and remote homelab storage.

#### Scenario: Auditing orphaned entities and vault paths
- **WHEN** user executes `kb corpus audit`
- **THEN** system checks for chunks or formulas without parent documents, documents without chunks, missing remote figure vault files, and unvalidated formulas, returning an invariant health report.

#### Scenario: Emitting structured audit health scorecard
- **WHEN** audit command is executed with `--json` flag
- **THEN** system emits a machine-readable JSON summary reporting total documents, chunks, formulas, figures, benchmark tables, and any identified integrity violations.
