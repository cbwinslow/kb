# Spec Delta: document-ingestion

## ADDED Requirements

### Requirement: Portable Pluggable Batch Ingestion Pipeline
The system SHALL provide domain-agnostic pipeline abstractions that decouple document discovery, layout parsing, mathematical formula extraction, table extraction, vector embedding, database persistence, and bibliographic enrichment.

#### Scenario: End-to-end pipeline execution
- **WHEN** a candidate paper source is submitted to `IngestionPipeline`
- **THEN** the pipeline runs parser, extractor, table, chunker, embedder, and persistence stages sequentially without domain-specific hardcoding, returning execution summary statistics.

#### Scenario: Existing document deduplication
- **WHEN** a paper source has a citekey or DOI matching an existing record in `kb_documents`
- **THEN** the pipeline skips parsing and re-embedding unless an explicit overwrite flag is enabled.

#### Scenario: Isolated document failure
- **WHEN** a corrupt or unsupported document fails during parsing or extraction
- **THEN** the runner logs the failure with the document identifier, continues processing remaining documents, and records the error in batch statistics.

### Requirement: Directory and Hierarchical Folder Corpus Discovery
The system SHALL discover candidate scientific papers from flat directories and nested folder structures, extracting citekeys and metadata from filenames or metadata sidecar files when available.

#### Scenario: Nested folder discovery with sidecar metadata
- **WHEN** a source directory contains subdirectories with PDFs and accompanying `SOURCE.md` files
- **THEN** the discoverer extracts the PDF path, citekey, title, authors, year, and canonical URLs from the sidecar without requiring manual parameter entry.

#### Scenario: Flat directory glob discovery
- **WHEN** a directory path is supplied with a glob pattern (e.g., `*.pdf`)
- **THEN** the discoverer yields all matching PDF files with derived citekeys.

### Requirement: High-Yield OpenAlex Batch Ingestion with Polite Paging
The system SHALL support bulk paper discovery from OpenAlex queries using high-yield page sizes (up to 100 works per request) with polite pool authentication, filtering for open-access PDF availability.

#### Scenario: High-yield paper search
- **WHEN** a topic query is executed against OpenAlex with `per_page=50`
- **THEN** up to 50 matching works are retrieved per API call, minimizing network roundtrips and avoiding rate limit throttling.

#### Scenario: Open-access PDF retrieval
- **WHEN** an OpenAlex work includes an open-access PDF URL
- **THEN** the runner downloads the PDF to a staging location and enqueues it into the ingestion pipeline with canonical OpenAlex metadata.
