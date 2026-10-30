# document-ingestion Specification

## Purpose
Provides automated parsing of academic research PDFs into structured Markdown with preserved LaTeX mathematical equations and table data.

## Requirements

### Requirement: Document Ingestion from Local and Remote Sources
The system SHALL ingest academic research documents from local PDF file paths, valid DOIs, and arXiv identifiers.

#### Scenario: Ingest from local PDF path
- **WHEN** user or caller provides a path to a valid PDF document on disk
- **THEN** system validates file integrity, assigns a deterministic document ID, and schedules parsing

#### Scenario: Ingest from DOI or arXiv ID
- **WHEN** user provides an arXiv ID (e.g., `2206.09654`) or DOI
- **THEN** system resolves metadata and downloads the corresponding PDF asset into the document vault

### Requirement: Multimodal Layout Parsing with Equation Preservation
The system SHALL parse PDF documents using layout-aware neural extraction, converting text into Markdown while preserving LaTeX math blocks and tabular layouts.

#### Scenario: Preserving inline and display LaTeX equations
- **WHEN** a document containing mathematical equations is parsed
- **THEN** equations are rendered as valid LaTeX math enclosed in `$...$` or `$$...$$` blocks without loss of mathematical symbols

#### Scenario: Handling multi-column academic layouts
- **WHEN** a two-column IEEE, ACM, or arXiv paper is processed
- **THEN** text flow follows the true reading order rather than interleaving columns across page coordinates

### Requirement: Structural and Equation-Preserving Document Chunking
The system SHALL chunk parsed scientific documents into semantic retrieval units using document-native AST boundaries rather than naive character/token sliding windows.

#### Scenario: Atomic preservation of mathematical blocks
- **WHEN** text containing inline math (`$...$`) or display math (`$$...$$`, `\begin{equation}...\end{equation}`, `\begin{align}...\end{align}`) is chunked
- **THEN** mathematical expressions are preserved atomically within a single chunk without delimiter slicing or syntax truncation

#### Scenario: Atomic preservation of tabular matrices
- **WHEN** tabular baseline data or matrices are chunked
- **THEN** tables remain unified with column headers, row keys, and units preserved intact rather than fragmented across chunk boundaries

#### Scenario: Heading breadcrumb context enrichment
- **WHEN** a chunk is generated from a nested subsection
- **THEN** the chunk is enriched with a prepended breadcrumb header containing document title, citekey, and hierarchical section lineage (e.g. `[Document: ... | Citekey: ... | Section: H1 > H2 > H3]`)

#### Scenario: Parent-child and relational chunk linkage
- **WHEN** chunks are created from a document
- **THEN** each chunk stores its `chunk_index`, `parent_section_id`, `section_path`, `previous_chunk_id`, and `next_chunk_id` for relational provenance

### Requirement: Ingestion Validation and Invariant Verification Harness
The system SHALL enforce rigorous post-chunking invariant assertions before persisting or indexing chunks.

#### Scenario: Math delimiter balance invariant
- **WHEN** a chunk set is produced
- **THEN** validator asserts no chunk contains unclosed math environments (`\begin{...}` without matching `\end{...}`) or unmatched LaTeX delimiters

#### Scenario: Token budget adherence without AST truncation
- **WHEN** a section exceeds target embedding token boundaries
- **THEN** chunker splits only at paragraph or sentence boundaries while preserving equations and tables as unbreakable atomic nodes

### Requirement: OpenAlex Bibliometric Document Enrichment
The system SHALL persist OpenAlex bibliometric fields, topic tags, and citation counts on ingested document records.

#### Scenario: Storing OpenAlex identifiers and metrics
- **WHEN** a document is enriched with OpenAlex metadata
- **THEN** document record in the database stores `openalex_id`, `citation_count`, and a structured JSON list of topics and referenced work IDs

### Requirement: Adapted Ingestion of Legacy Document Chunks
The system SHALL accept pre-parsed legacy documents and chunk structures for direct ingestion into `kb_documents` and `kb_chunks` alongside fresh PDF ingestion.

#### Scenario: Ingesting adapted legacy document structures
- **WHEN** an adapted legacy document bundle containing document metadata, chunks with pre-computed embeddings, and formulas is supplied
- **THEN** system validates structural schema integrity and commits the bundle into `kb_` tables without requiring raw PDF parsing or neural layout extraction

### Requirement: Equation Derivation Co-occurrence and Window Clustering
The system SHALL detect sequential and coupled mathematical equations within a derivation section and cluster them into unified semantic chunks within the target token budget.

#### Scenario: Clustering coupled equations into atomic retrieval units
- **WHEN** multiple equations appear sequentially in a mathematical derivation or model definition
- **THEN** chunker preserves the equations within the same retrieval chunk when their combined token length adheres to the chunk size limit

#### Scenario: Binding preceding premise and trailing variable definitions
- **WHEN** a display equation is preceded by an explanatory sentence or followed by a variable definition clause (e.g. "where $X$ denotes...")
- **THEN** system keeps the framing sentences and variable definitions unified with the equation rather than splitting them into separate chunks

### Requirement: Mathematical Symbol and Variable Context Enrichment
The system SHALL extract mathematical symbols and variable definitions present in a chunk and enrich the chunk context header with a structured symbol index.

#### Scenario: Emitting symbol index context header
- **WHEN** a chunk contains mathematical equations with free variables or parameter symbols
- **THEN** system prepends a structured descriptor `[Symbols: ...]` to the chunk's enriched text for dense and sparse indexing

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

### Requirement: Pre-Download Multi-Attribute Candidate Filtering
The system SHALL verify whether a candidate paper exists in the local database or storage vault across multiple attributes before initiating remote HTTP payload downloads.

#### Scenario: Pre-download duplicate avoidance for OpenAlex and arXiv works
- **WHEN** a candidate work from OpenAlex or arXiv is evaluated for harvesting
- **THEN** system queries existing database records for matching DOI, OpenAlex ID, arXiv ID, citekey, or normalized title and skips HTTP PDF retrieval if already present.

#### Scenario: Candidate resolution with partial metadata
- **WHEN** a candidate paper only has a title and author list without DOI or external ID
- **THEN** system performs normalized title comparison (case-insensitive, punctuation-stripped) against indexed documents and reports candidate match before downloading.
