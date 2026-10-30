# Tasks: Literature Corpus Expansion & Figure Harvester

## 1. Targeted 2024–2026 Academic Harvester
- [x] 1.1 Add 2024–2026 query filters and keyword sets in `src/kb/enrich/openalex.py` (Bat tracking, seam-shifted wake, biomechanics).
- [x] 1.2 Implement automated PDF retrieval and temporary spooling with disk space threshold guards.

## 2. Docling Figure Extraction Pipeline
- [x] 2.1 Update Docling parser in `src/kb/ingest/parser.py` to extract `PictureItem` bounding boxes and images.
- [x] 2.2 Implement image upload to homelab vault storage via `SSHStorageSync` and local file unlinking.
- [x] 2.3 Persist figure entities to `kb_figures` with foreign keys to document and chunk.

## 3. Autonomous Citation Graph Backfill
- [x] 3.1 Hook `CitationGraphBuilder` into the document ingestion pipeline to resolve citations automatically upon insert.
- [x] 3.2 Update `kb sync citations` CLI command with a `--years 2024-2026` filter.

## 4. REST & GraphQL Integration
- [x] 4.1 Expose `/api/documents/{id}/figures` endpoint in `src/kb/ui/app.py`.
- [x] 4.2 Add `figures` field resolver to `DocumentType` in `src/kb/graphql/schema.py`.

## 5. Verification & Testing
- [x] 5.1 Implement unit and integration tests in `tests/test_parser.py` and `tests/test_citations.py`.
- [x] 5.2 Validate quality gates: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
