# Spec Delta: openalex-enrichment

## Purpose

Enriches scientific documents with OpenAlex bibliometric data, citation networks, author concepts, and related research lineages.

## ADDED Requirements

### Requirement: OpenAlex Work Entity Resolution
The system SHALL resolve scientific documents to canonical OpenAlex work entities using DOI, arXiv ID, or title search queries.

#### Scenario: Resolve document by DOI or arXiv ID
- **WHEN** user or caller provides a DOI or arXiv ID for an ingested paper
- **THEN** system queries the OpenAlex API and returns the canonical Work entity with OpenAlex ID, citation count, and primary topic

#### Scenario: Fallback resolution by paper title
- **WHEN** document has no DOI or arXiv ID
- **THEN** system queries OpenAlex work search by title and matches candidates using string similarity thresholds

### Requirement: Bibliometric Metadata and Lineage Extraction
The system SHALL extract forward citations, referenced works, concepts/topics, and citation metrics from OpenAlex for persistent storage.

#### Scenario: Extracting referenced works and citation metrics
- **WHEN** an OpenAlex work entity is retrieved
- **THEN** system extracts the list of referenced work IDs, cited-by counts, publication year, and associated topic classifications

### Requirement: OpenAlex Metadata CLI Backfill
The system SHALL provide a CLI command to query OpenAlex and backfill metadata for ingested papers.

#### Scenario: Running batch enrichment via CLI
- **WHEN** user executes `kb enrich openalex --all` or `kb enrich openalex --citekey <key>`
- **THEN** system queries OpenAlex for the target papers and persists resolved work IDs, topics, and citation metrics in the database
