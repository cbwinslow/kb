# Proposal: Codebase Hardening, OpenSpec Audit, Web Search Integration, and Optimization

## Problem Statement
While `kb` has evolved into a high-capacity research engine with 311+ documents, 6,199 formulas, and 1,395 benchmark tables across workstation (`cbwwin`) and homelab (`cbwdellr720`) infrastructure, several areas require structural hardening, completeness, and optimization:
1. **OpenSpec Documentation Gaps**: Architectural advancements introduced in ADR-032, ADR-033, and ADR-034 (empirical accuracy benchmarking, multi-attribute deduplication, and corpus relational health auditing) lack formal main specs in `openspec/specs/`.
2. **Web Discovery Tooling**: Agents currently rely on local vector search (`kb_search_literature`) or pre-harvested document collections. They lack live multi-source web search capabilities to discover newly published arXiv preprints, OpenAlex scholarly publications, and web articles on the fly.
3. **Deprecation Warnings**: Ingestion and test logs surface deprecation notices from `docling` (`OcrMode.FULL_PAGE`, `generate_page_images=True`) and `pandas` (`Pandas4Warning`).
4. **End-to-End Subsystem Validation**: All CLI commands, MCP tools, GraphQL schemas, and synchronization protocols require structured manual verification alongside automated tests.

## Proposed Changes
1. **OpenSpec Main Spec Alignment**:
   - Add `openspec/specs/literature-deduplication/spec.md`.
   - Add `openspec/specs/empirical-accuracy-benchmarking/spec.md`.
   - Add `openspec/specs/corpus-relational-auditing/spec.md`.
   - Add `openspec/specs/scholarly-web-search/spec.md`.
   - Update `docs/DECISIONS.md` with ADR-035 (Scholarly Web Search Engine & MCP Discovery Integration).
2. **Scholarly & Web Search Integration**:
   - Implement `src/kb/enrich/web_search.py` (`ScholarlyWebSearcher`) with arXiv API search, OpenAlex live search, and DuckDuckGo/Tavily web discovery.
   - Expose `kb_web_search_papers` in FastMCP (`src/kb/mcp/server.py`).
   - Add `kb search web` to CLI (`src/kb/cli.py`).
3. **Deprecation Cleanup & Code Hardening**:
   - Resolve Docling OCR and table image generation deprecation warnings in `src/kb/ingest/parser.py` and `src/kb/ingest/pipeline.py`.
   - Fix pandas dataframe column/index assignment deprecation warnings.
4. **Comprehensive Subsystem Testing & Verification**:
   - Run full test suite, linting, and strict type checking.
   - Execute manual CLI operations (corpus audit, repair-all dry run, accuracy benchmarking, MCP tool calls, UI verification).
   - Commit and push all changes to GitHub.

## Impact
- Delivers a unified scholarly search tool for agents.
- Ensures 100% compliance with OpenSpec standards and zero test deprecations.
- Guarantees seamless agent discovery and quantitative empirical workflow execution.
