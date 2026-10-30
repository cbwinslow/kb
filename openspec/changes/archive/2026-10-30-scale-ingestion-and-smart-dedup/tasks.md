# Tasks

## 1. Multi-Attribute Deduplication Engine

- [x] 1.1 Implement `DuplicateResolver` in `src/kb/ingest/dedup.py` with multi-attribute matching (DOI, OpenAlex ID, arXiv ID, citekey, normalized title) and verify with unit tests in `tests/test_dedup.py`
- [x] 1.2 Integrate `DuplicateResolver` into `IngestionPipeline.ingest_source()` in `src/kb/ingest/pipeline.py` and verify duplicate sources are skipped before Docling neural parsing in `tests/test_pipeline.py`

## 2. Pre-Download Verification in Discoverers

- [x] 2.1 Refactor `OpenAlexSourceDiscoverer` in `src/kb/ingest/pipeline.py` to evaluate candidates against `DuplicateResolver` prior to executing HTTP PDF downloads, and verify with tests in `tests/test_pipeline.py`
- [x] 2.2 Refactor `PreprintHarvester.filter_existing()` in `src/kb/sync/harvester.py` to check DOIs and normalized titles in addition to arXiv IDs, and verify with tests in `tests/test_harvester.py`

## 3. Cursor Pagination, Citation Ranking & Domain Presets

- [x] 3.1 Implement cursor-based pagination and `sort="cited_by_count:desc"` in `OpenAlexClient.search_works_cursor()` within `src/kb/enrich/openalex.py` and verify in `tests/test_openalex.py`
- [x] 3.2 Implement curated sabermetric presets (`mlb-modeling`, `retrosheet`, `statcast`, `popular`, `baseball-python`) in `src/kb/enrich/openalex.py` and verify query generation

## 4. CLI Extension & Production Ingestion

- [x] 4.1 Extend `kb sync harvest` CLI command in `src/kb/cli.py` with `--preset`, `--sort`, `--max-papers`, and `--dry-run-dedup`, verifying CLI execution in `tests/test_cli.py`
- [x] 4.2 Execute the full quality gate (`ruff check`, `pyright`, `pytest`) ensuring 100% passing tests and zero warnings
- [x] 4.3 Run a live harvest of popular and modeling papers against PostgreSQL on `cbwdellr720` and verify multi-attribute deduplication suppresses duplicate entries
- [x] 4.4 Record ADR-033 in `docs/DECISIONS.md` documenting the deduplication resolver and cursor harvesting architecture

## Workflow follow-up

- Sync delta specs to main specs with `npx openspec sync specs`.
- Archive the completed change with `npx openspec archive scale-ingestion-and-smart-dedup --yes`.
