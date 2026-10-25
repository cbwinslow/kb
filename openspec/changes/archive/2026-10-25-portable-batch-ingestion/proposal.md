# Proposal: Portable Batch Ingestion & Corpus Pipeline

## Why

Currently, document ingestion in `kb` is invoked on single PDF files via CLI (`kb ingest <pdf> <citekey>`) without a reusable, domain-agnostic batch orchestration abstraction. To scale `kb` across both curated research directories (such as our 91 baseball and physics papers) and high-yield online discovery (such as OpenAlex bulk queries) without tight coupling or rate limit penalties, the system needs clean, abstract pipeline protocols that decouple discovery, parsing, extraction, embedding, and storage.

## What Changes

- Introduce domain-agnostic ingestion abstractions in `src/kb/ingest/pipeline.py`:
  - `PaperSource`: Standard metadata container for candidate papers (local PDF path, citekey, title, authors, year, DOI, source metadata).
  - `SourceDiscovererProtocol`: Abstract interface for paper discovery.
  - `DirectorySourceDiscoverer`: Discovers documents from folder trees (e.g. nested `sources/<citekey>/*.pdf` or flat PDF directories) and reads metadata sidecars (`SOURCE.md`, `.bib`, `.json`) when present.
  - `OpenAlexSourceDiscoverer`: High-yield online discovery querying OpenAlex with polite pool batching (`per_page=50` or `100`), filtering for Open Access PDFs, and streaming candidate PDFs.
  - `IngestionPipeline`: Domain-agnostic orchestrator executing `DoclingParser` $\to$ `FormulaExtractor` $\to$ `TableExtractor` $\to$ `DocumentChunker` $\to$ `LocalEmbeddingGenerator` $\to$ `DatabaseManager` $\to$ `OpenAlexClient`.
- Implement `BatchIngestionRunner`:
  - Deduplication against existing `kb_documents` records.
  - Resilient error handling (isolated failures per paper with structured error reporting).
  - Execution metrics (total papers scanned, skipped, ingested, formulas extracted, tables exported, chunks created).
- Add CLI commands in `src/kb/cli.py`:
  - `kb ingest batch --dir <path> [--pattern <glob>] [--limit <n>]`
  - `kb ingest search-openalex --query <terms> [--limit <n>] [--per-page 50]`
- Provide clean script/runner demonstrating end-to-end ingestion of the curated 91-paper baseball research corpus using the portable abstractions.

## Capabilities

### Modified Capabilities

- `document-ingestion`: Add requirements for pluggable batch pipeline abstractions, directory/folder discovery, deduplication against existing records, and high-yield OpenAlex batch ingestion.

## Impact

- `src/kb/ingest/pipeline.py`: New module defining portable pipeline protocols, discoverers, and batch runner.
- `src/kb/cli.py`: New subcommands for `ingest batch` and `ingest search-openalex`.
- `tests/test_pipeline.py`: Comprehensive unit tests for discovery, pipeline execution, deduplication, and error isolation.
- Zero breaking changes to existing single-file `kb ingest` or database models.
