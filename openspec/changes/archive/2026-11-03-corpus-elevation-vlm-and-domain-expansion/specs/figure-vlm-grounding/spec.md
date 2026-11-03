# Spec Delta: figure-vlm-grounding

## ADDED Requirements

### Requirement: Batch Figure VLM Grounding Pipeline and CLI Indexer
The system SHALL provide a batch figure grounding pipeline and CLI command to process ungrounded figure records across the corpus, extracting visual summaries, curves, and formula entity links.

#### Scenario: Running batch figure indexing via CLI
- **WHEN** user executes `kb figures index-all` with optional `--batch-size` and `--limit`
- **THEN** the system identifies ungrounded figures, invokes the VLM processor to extract visual summaries and curve descriptors, links nearby formula IDs, and persists the updates in PostgreSQL

#### Scenario: Dry-run and force re-indexing options
- **WHEN** user specifies `--dry-run` or `--force` during batch figure indexing
- **THEN** the system previews grounding actions without database mutations in dry-run mode, or re-processes previously grounded figures when force is enabled
