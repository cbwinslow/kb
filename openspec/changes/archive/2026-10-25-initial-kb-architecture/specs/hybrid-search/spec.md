# Spec Delta: hybrid-search

## Purpose
Provides hybrid semantic vector search and keyword full-text search across indexed scientific papers and extracted components in PostgreSQL.

## ADDED Requirements

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
