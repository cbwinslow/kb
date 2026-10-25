# Design: OpenAlex Citation & Lineage Enrichment

## Context

Scientific papers stored in `kb_documents` currently track local file paths, authors, years, and arXiv IDs, but lack global citation network context. OpenAlex provides a free, comprehensive academic graph connecting works, authors, institutions, topics, and forward/backward citations.

See `proposal.md` for motivation and `specs/` for behavioral requirements.

## Goals / Non-Goals

**Goals:**
- Provide `OpenAlexClient` in `src/kb/enrich/openalex.py` with rate limiting, retries, and User-Agent identification.
- Support resolving papers via DOI, arXiv ID (e.g. `math/0509698`), or fuzzy title search.
- Persist `openalex_id`, `citation_count`, `topics`, and `referenced_works` on `kb_documents` in PostgreSQL on `cbwdellr720`.
- Provide FastMCP tools `kb_get_citations` and `kb_get_related_papers`.
- Provide `kb enrich openalex` CLI command to backfill existing papers.

**Non-Goals:**
- Downloading full-text PDFs from OpenAlex in this change (we already ingest PDFs via Docling).
- Synchronizing the entire OpenAlex database locally (we query on-demand and cache paper-level metadata).

## Decisions

### 1. HTTP Client & Polite Pool Identification
- **Choice**: Async `httpx.AsyncClient` with polite User-Agent header (`ScientificKB/1.0 (mailto:blaine.winslow@gmail.com)`) and optional `OPENALEX_API_KEY`.
- **Rationale**: Clean async integration with our async SQLAlchemy session and FastMCP handlers. OpenAlex polite headers ensure higher rate limits (10 req/s keyless, 30 req/s with key).
- **Alternatives Considered**: Direct urllib/requests (blocking, not async-friendly).

### 2. Schema Evolution: JSON Columns for Bibliographic Graphs
- **Choice**: Extend `kb_documents` with `openalex_id` (String), `citation_count` (Integer), `topics` (JSON array of `{id, name, score}`), and `referenced_works` (JSON array of OpenAlex IDs).
- **Rationale**: Avoids premature normalization of deep foreign graphs while keeping paper-level queries fast and self-contained in PostgreSQL and SQLite.

### 3. Hermetic Testing with Mock OpenAlex Transport
- **Choice**: Injectable transport/protocol allowing unit tests to simulate OpenAlex API responses without network requests or rate limits.
- **Rationale**: Tests remain fast, deterministic, and offline.

## Risks / Trade-offs

- **[Risk] OpenAlex Rate Limiting or Network Outages**:
  - *Mitigation*: Graceful error handling in CLI and MCP tools; cached metadata in PostgreSQL ensures search still functions when offline.
- **[Risk] Title Disambiguation Errors**:
  - *Mitigation*: Prefer exact DOI or arXiv ID matching first; fall back to title match only if identifiers are absent, validating candidate title similarity.
