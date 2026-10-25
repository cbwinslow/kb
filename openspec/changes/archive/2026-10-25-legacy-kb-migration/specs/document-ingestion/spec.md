# Spec Delta: document-ingestion

## ADDED Requirements

### Requirement: Adapted Ingestion of Legacy Document Chunks
The system SHALL accept pre-parsed legacy documents and chunk structures for direct ingestion into `kb_documents` and `kb_chunks` alongside fresh PDF ingestion.

#### Scenario: Ingesting adapted legacy document structures
- **WHEN** an adapted legacy document bundle containing document metadata, chunks with pre-computed embeddings, and formulas is supplied
- **THEN** system validates structural schema integrity and commits the bundle into `kb_` tables without requiring raw PDF parsing or neural layout extraction
