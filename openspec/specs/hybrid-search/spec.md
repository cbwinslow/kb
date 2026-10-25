# hybrid-search Specification

## Purpose
Provides hybrid semantic vector search and keyword full-text search across indexed scientific papers and extracted components in PostgreSQL.

## Requirements

### Requirement: Vector and Full-Text Document Indexing
The system SHALL generate dense vector embeddings for document chunks and maintain full-text search indices in PostgreSQL.

#### Scenario: Indexing parsed document chunks
- **WHEN** a document's Markdown sections are persisted to the database
- **THEN** system generates dense vector embeddings and updates the PostgreSQL full-text search tsvector column

### Requirement: Hybrid Retrieval with Reciprocal Rank Fusion
The system SHALL combine vector similarity scores and BM25/trigram text rankings using Reciprocal Rank Fusion (RRF).

#### Scenario: Executing a hybrid semantic query
- **WHEN** a user or agent issues a query containing both domain concepts and exact formula names
- **THEN** system computes both vector distance and keyword match scores, merging them via RRF into a ranked result set

### Requirement: Local Dense Embedding Generation and Query Vectorization
The system SHALL compute 1024-dimensional dense semantic embeddings using local GPU-accelerated inference for all document chunks and search query strings.

#### Scenario: Generating chunk embeddings during ingestion
- **WHEN** document chunks are prepared for database persistence
- **THEN** system computes 1024-dimensional float vectors locally using GPU acceleration and populates the chunk vector column

#### Scenario: Vectorizing search query for cosine retrieval
- **WHEN** an agent or user submits a semantic search query
- **THEN** system vectorizes the query text into a 1024-dimensional dense vector and executes cosine similarity retrieval against chunk embeddings
