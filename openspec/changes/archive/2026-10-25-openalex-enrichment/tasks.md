# Tasks: OpenAlex Citation & Lineage Enrichment

## 1. OpenAlex Client & Data Model

- [x] 1.1 Extend `Document` model in `src/kb/storage/models.py` with `openalex_id`, `citation_count`, `topics`, and `referenced_works` fields
- [x] 1.2 Implement `OpenAlexClient` in `src/kb/enrich/openalex.py` supporting work resolution by DOI, arXiv ID, or title with error handling
- [x] 1.3 Add unit tests in `tests/test_openalex.py` verifying entity parsing, topic extraction, and mock HTTP resolution

## 2. CLI Backfill & Persistence

- [x] 2.1 Implement `async_enrich_openalex` and CLI command `kb enrich openalex` in `src/kb/cli.py` supporting `--citekey` and `--all`
- [x] 2.2 Verify metadata enrichment on test database and homelab PostgreSQL for ingested reference papers (`miller2005`, `jensen2009`)

## 3. FastMCP Citation Graph & Related Literature Tools

- [x] 3.1 Implement FastMCP tool `kb_get_citations` in `src/kb/mcp/server.py` returning forward citations and referenced works
- [x] 3.2 Implement FastMCP tool `kb_get_related_papers` in `src/kb/mcp/server.py` querying OpenAlex for related literature by concept/topic
- [x] 3.3 Add unit tests in `tests/test_mcp.py` asserting tool registration and mock payload return structures

## Workflow follow-up

- Validate all OpenSpec artifacts with `openspec validate openalex-enrichment`.
- Archive the change after implementation and test verification are complete.
