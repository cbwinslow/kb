# Spec Delta: document-ingestion

## MODIFIED Requirements

### Requirement: Portable Pluggable Batch Ingestion Pipeline
The system SHALL provide domain-agnostic pipeline abstractions that decouple document discovery, layout parsing, mathematical formula extraction, table extraction, vector embedding, database persistence, and bibliographic enrichment.

#### Scenario: End-to-end pipeline execution
- **WHEN** a candidate paper source is submitted to `IngestionPipeline`
- **THEN** the pipeline runs parser, extractor, table, chunker, embedder, and persistence stages sequentially without domain-specific hardcoding, returning execution summary statistics.

#### Scenario: Existing document deduplication
- **WHEN** a paper source has a citekey, DOI, OpenAlex ID, arXiv ID, or normalized title matching an existing record in `kb_documents`
- **THEN** the pipeline skips parsing and re-embedding unless an explicit overwrite flag is enabled.

#### Scenario: Isolated document failure
- **WHEN** a corrupt or unsupported document fails during parsing or extraction
- **THEN** the runner logs the failure with the document identifier, continues processing remaining documents, and records the error in batch statistics.

## ADDED Requirements

### Requirement: Pre-Download Multi-Attribute Candidate Filtering
The system SHALL verify whether a candidate paper exists in the local database or storage vault across multiple attributes before initiating remote HTTP payload downloads.

#### Scenario: Pre-download duplicate avoidance for OpenAlex and arXiv works
- **WHEN** a candidate work from OpenAlex or arXiv is evaluated for harvesting
- **THEN** system queries existing database records for matching DOI, OpenAlex ID, arXiv ID, citekey, or normalized title and skips HTTP PDF retrieval if already present.

#### Scenario: Candidate resolution with partial metadata
- **WHEN** a candidate paper only has a title and author list without DOI or external ID
- **THEN** system performs normalized title comparison (case-insensitive, punctuation-stripped) against indexed documents and reports candidate match before downloading.
