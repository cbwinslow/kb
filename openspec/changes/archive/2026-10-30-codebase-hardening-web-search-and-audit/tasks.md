# Tasks: Codebase Hardening, OpenSpec Audit, Web Search Integration, and Optimization

## Phase 1: OpenSpec & Architecture Audit
- [x] 1.1 Create `openspec/specs/literature-deduplication/spec.md` <!-- id: 1.1 -->
- [x] 1.2 Create `openspec/specs/empirical-accuracy-benchmarking/spec.md` <!-- id: 1.2 -->
- [x] 1.3 Create `openspec/specs/corpus-relational-auditing/spec.md` <!-- id: 1.3 -->
- [x] 1.4 Create `openspec/specs/scholarly-web-search/spec.md` <!-- id: 1.4 -->
- [x] 1.5 Update `docs/DECISIONS.md` with ADR-035 (Scholarly Web Search Engine & MCP Discovery Integration) <!-- id: 1.5 -->
- [x] 1.6 Audit docstrings and `from __future__ import annotations` across all modules <!-- id: 1.6 -->

## Phase 2: Web Search Tooling & Dependency Integration
- [x] 2.1 Implement `src/kb/enrich/web_search.py` (`ScholarlyWebSearcher`, arXiv API parser, OpenAlex search, DuckDuckGo web fallback) <!-- id: 2.1 -->
- [x] 2.2 Add unit and integration tests in `tests/test_web_search.py` <!-- id: 2.2 -->
- [x] 2.3 Expose `kb_web_search_papers` in `src/kb/mcp/server.py` <!-- id: 2.3 -->
- [x] 2.4 Add `kb search web` command to `src/kb/cli.py` <!-- id: 2.4 -->
- [x] 2.5 Verify and audit dependencies in `pyproject.toml` <!-- id: 2.5 -->

## Phase 3: Code Optimization & Deprecation Cleanup
- [x] 3.1 Fix Docling and Pandas deprecation warnings in `src/kb/ingest/parser.py` and `tests/test_ingest.py` <!-- id: 3.1 -->
- [x] 3.2 Audit async database session contexts across `src/kb/storage/`, `src/kb/enrich/`, and `src/kb/ui/` <!-- id: 3.2 -->
- [x] 3.3 Verify Polars vectorized expressions in `src/kb/codegen/` and `src/kb/qa/accuracy.py` <!-- id: 3.3 -->

## Phase 4: Manual Subsystem & End-to-End Testing Matrix
- [x] 4.1 Run `kb corpus audit` and `kb corpus audit --json` <!-- id: 4.1 -->
- [x] 4.2 Run `kb corpus repair-all --dry-run` <!-- id: 4.2 -->
- [x] 4.3 Run `kb benchmark accuracy` <!-- id: 4.3 -->
- [x] 4.4 Run `kb search web` and test arXiv/OpenAlex live queries <!-- id: 4.4 -->
- [x] 4.5 Test MCP tool definitions and execution <!-- id: 4.5 -->
- [x] 4.6 Verify homelab SSH vault sync status (`kb sync ssh-check`) <!-- id: 4.6 -->

## Phase 5: Verification & GitHub Synchronization
- [x] 5.1 Run `pytest tests/` (all tests passing) <!-- id: 5.1 -->
- [x] 5.2 Run `ruff check src/ tests/ packages/` (0 errors) <!-- id: 5.2 -->
- [x] 5.3 Run `pyright src/ tests/ packages/` (0 errors) <!-- id: 5.3 -->
- [x] 5.4 Commit changes and push to `origin/master` <!-- id: 5.4 -->
- [x] 5.5 Archive OpenSpec change <!-- id: 5.5 -->
