# Design: Portable Batch Ingestion & Corpus Pipeline

## Context

The `kb` repository currently provides parsing, chunking, math/table extraction, and vector embedding across isolated components (`DoclingParser`, `DocumentChunker`, `FormulaExtractor`, `TableExtractor`, `LocalEmbeddingGenerator`, `DatabaseManager`, `OpenAlexClient`). Previously, single-file CLI ingestion (`async_ingest`) hardcoded the sequence of steps and required manual parameter inputs. To ingest large scientific corpora (e.g., our 91-paper baseball collection) or stream high-yield OpenAlex batches without hardcoding domain-specific rules, we need clean abstractions and modular batch orchestration.

## Goals / Non-Goals

**Goals:**
- Provide clean, extensible protocols (`SourceDiscovererProtocol`, `ParserProtocol`, `IngestionPipelineProtocol`) completely free of domain-specific logic.
- Support recursive directory and nested folder discovery (e.g. `sources/<citekey>/*.pdf` with optional `SOURCE.md` metadata extraction).
- Support high-yield OpenAlex query discovery (`per_page=50` or `100`), filtering for Open Access PDFs and polite pool headers.
- Support deduplication against `kb_documents` so re-running batch discovery skips already-ingested papers.
- Provide isolated error handling so single corrupt PDFs do not halt a 100-paper batch.
- Support modular script execution (e.g. running a dedicated runner for `sabermetricspy-research` sources).

**Non-Goals:**
- Circumventing paywalled scientific publications (only local files or legal Open Access PDFs are fetched).
- Real-time parallel cluster distributed computing (asynchronous local concurrency is sufficient).

## Decisions

### 1. Unified `PaperSource` Dataclass
- **Decision**: Define `PaperSource` in `src/kb/ingest/pipeline.py` with `pdf_path: Path`, `citekey: str`, `title: str | None`, `authors: list[str] | None`, `year: int | None`, `doi: str | None`, and `metadata: dict[str, Any]`.
- **Rationale**: Decouples how a paper is discovered from how it is processed. Discoverers produce `Iterable[PaperSource]` or `AsyncIterable[PaperSource]`.
- **Alternatives**: Passing raw tuples or paths directly (inflexible, loses metadata).

### 2. Composition-based `IngestionPipeline`
- **Decision**: `IngestionPipeline` receives injected instances of `DoclingParser`, `DocumentChunker`, `FormulaExtractor`, `TableExtractor`, `EmbeddingProtocol`, `DatabaseManager`, and optional `OpenAlexClient`.
- **Rationale**: Facilitates full dependency injection, unit testing with mocks, and swapping embedding or parser backends without modifying pipeline logic.
- **Alternatives**: Monolithic procedural function with module-level globals.

### 3. Deduplication via Citekey & DOI
- **Decision**: Prior to running intensive layout parsing or vector embedding, `BatchIngestionRunner` checks if `citekey` or `doi` exists in `kb_documents`. If present and `force=False`, it marks the item as `skipped` and proceeds to the next document.
- **Rationale**: Prevents re-computing 1024-d embeddings or re-parsing documents already residing in PostgreSQL.
- **Alternatives**: Ingesting everything and relying on DB unique constraint collisions (wastes heavy CPU/GPU time).

### 4. High-Yield OpenAlex Paging
- **Decision**: When querying OpenAlex, request `per_page=50` or `100` and `filter=has_oa_accepted_or_published_version:true`.
- **Rationale**: Satisfies the user requirement to return large result sets per request, maximizing yield while minimizing API roundtrips and staying well within rate limits.
- **Alternatives**: Individual 1-by-1 searches (slow, prone to hitting rate limits).

## Risks / Trade-offs

- **[Risk]** Heavy Docling layout parsing is CPU/memory intensive when running on 90+ large PDFs.
  - **Mitigation**: Run ingestion sequentially or with bounded concurrency (default 1 worker) to prevent out-of-memory errors on Windows machines.
- **[Risk]** Some legacy or scan-based PDFs may fail Docling AST parsing.
  - **Mitigation**: Wrap per-document pipeline processing in `try...except Exception`, record failure metrics in `BatchStats`, and continue the batch.
