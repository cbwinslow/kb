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
