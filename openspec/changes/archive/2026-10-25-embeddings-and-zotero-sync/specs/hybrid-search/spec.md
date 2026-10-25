# Spec Delta: hybrid-search

## ADDED Requirements

### Requirement: Local Dense Embedding Generation and Query Vectorization
The system SHALL compute 1024-dimensional dense semantic embeddings using local GPU-accelerated inference for all document chunks and search query strings.

#### Scenario: Generating chunk embeddings during ingestion
- **WHEN** document chunks are prepared for database persistence
- **THEN** system computes 1024-dimensional float vectors locally using GPU acceleration and populates the chunk vector column

#### Scenario: Vectorizing search query for cosine retrieval
- **WHEN** an agent or user submits a semantic search query
- **THEN** system vectorizes the query text into a 1024-dimensional dense vector and executes cosine similarity retrieval against chunk embeddings
