# Spec Delta: openalex-citation-graph

## ADDED Requirements

### Requirement: Autonomous Citation Graph Expansion
The system SHALL automatically discover and resolve citation relationships for newly ingested documents against existing corpus works.

#### Scenario: Linking new document to existing corpus works
- **WHEN** a newly harvested paper containing `referenced_works` is ingested into PostgreSQL
- **THEN** system automatically matches cited OpenAlex IDs and DOIs against existing documents and inserts directed citation edges in `kb_citations`

#### Scenario: Re-indexing corpus citation network
- **WHEN** user executes `kb sync citations --backfill`
- **THEN** system scans all unresolved citation references in the corpus and updates `cited_document_id` links for newly available works
