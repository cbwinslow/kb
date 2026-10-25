# Spec Delta: document-ingestion

## ADDED Requirements

### Requirement: OpenAlex Bibliometric Document Enrichment
The system SHALL persist OpenAlex bibliometric fields, topic tags, and citation counts on ingested document records.

#### Scenario: Storing OpenAlex identifiers and metrics
- **WHEN** a document is enriched with OpenAlex metadata
- **THEN** document record in the database stores `openalex_id`, `citation_count`, and a structured JSON list of topics and referenced work IDs
