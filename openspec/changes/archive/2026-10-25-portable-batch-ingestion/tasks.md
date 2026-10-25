# Tasks: Portable Batch Ingestion & Corpus Pipeline

## 1. Domain-Agnostic Ingestion Abstractions & Discovery

- [x] 1.1 Implement `PaperSource`, `SourceDiscovererProtocol`, `DirectorySourceDiscoverer`, and `OpenAlexSourceDiscoverer` in `src/kb/ingest/pipeline.py`. Verify with unit tests in `tests/test_pipeline.py`.
- [x] 1.2 Implement `IngestionPipeline` and `BatchIngestionRunner` in `src/kb/ingest/pipeline.py` with dependency injection, existing record deduplication, and isolated failure handling. Verify with unit tests in `tests/test_pipeline.py`.

## 2. CLI Integration & Dedicated Corpus Runner

- [x] 2.1 Add `kb ingest batch` and `kb ingest search-openalex` subcommands to `src/kb/cli.py` delegating to `BatchIngestionRunner`. Verify via CLI `--help` invocation.
- [x] 2.2 Create a reusable runner script in `scripts/ingest_baseball_corpus.py` utilizing `DirectorySourceDiscoverer` and `BatchIngestionRunner` to ingest the curated 91-paper baseball collection. Verify execution with dry-run mode.

## 3. Verification & Code Quality

- [x] 3.1 Run unit tests in `tests/test_pipeline.py` covering directory discovery, sidecar metadata parsing, deduplication, and error isolation. Verify with `uv run pytest tests/test_pipeline.py`.
- [x] 3.2 Run full linting, static type checking, and fast test suite: `uv run ruff check src tests scripts`, `uv run pyright src tests scripts`, and `uv run pytest -m "not slow"`.

## Workflow follow-up

- Archive the change after review requirements are satisfied.
- Commit changes to git tracking.
