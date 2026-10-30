# Design: Codebase Hardening, OpenSpec Audit, Web Search Integration, and Optimization

## Architecture & Component Design

### 1. Scholarly & Web Search Engine (`src/kb/enrich/web_search.py`)
The search engine coordinates multiple external endpoints without adding bloated external search SDKs:
- **arXiv Query Client**:
  - Uses `httpx.AsyncClient` against `http://export.arxiv.org/api/query`.
  - Parses Atom XML feed (`ElementTree`) extracting entry IDs, publication dates, primary categories, titles, abstracts, authors, and PDF links.
  - Formats results into standard `SearchResult` Pydantic models.
- **OpenAlex Live Search Client**:
  - Queries `https://api.openalex.org/works?search=<query>` with cursor pagination, citation sorting (`sort="cited_by_count:desc"`), and open-access PDF location resolution.
- **Web Fallback (DuckDuckGo Lite / General HTML)**:
  - Supports queries for broader quantitative tutorials, blog posts, and domain glossaries via lightweight HTML parsing or structured results.
- **Unified Interface**:
  ```python
  class ScholarlyWebSearcher:
      async def search(
          self,
          query: str,
          source: Literal["all", "arxiv", "openalex", "web"] = "all",
          limit: int = 10,
      ) -> list[SearchResult]: ...
  ```

### 2. FastMCP Tool Registration (`src/kb/mcp/server.py`)
- Extends the FastMCP server with `kb_web_search_papers`:
  - Parameters: `query: str`, `source: str = "all"`, `max_results: int = 10`.
  - Returns structured markdown summaries with titles, authors, publication years, abstracts, and direct PDF/landing URLs.
  - Seamlessly bridges agent queries from local knowledge base retrieval to live scholarly web discovery.

### 3. OpenSpec Specs Structure
Create formal specifications matching current implementations:
1. `openspec/specs/literature-deduplication/spec.md`:
   - Requirements for canonical DOI resolution, OpenAlex ID normalization, arXiv ID matching, normalized title comparison, and pre-download candidate rejection.
2. `openspec/specs/empirical-accuracy-benchmarking/spec.md`:
   - Requirements for Polars AST expression compilation, column binding, dataset loading, and MAE/RMSE/$R^2$ validation score credits.
3. `openspec/specs/corpus-relational-auditing/spec.md`:
   - Requirements for relational foreign-key integrity, orphaned entity detection, and atomic batch formula quality scoring.
4. `openspec/specs/scholarly-web-search/spec.md`:
   - Requirements for multi-source live paper retrieval, rate limiting, and agent tool execution.

### 4. Deprecation Cleanup
- In `src/kb/ingest/parser.py`:
  - Upgrade `force_full_page_ocr` to `mode=OcrMode.FULL_PAGE` or standard options depending on Docling version.
  - Upgrade table image generation configuration to `generate_page_images=True`.
- In `tests/test_ingest.py`:
  - Refactor synthetic DataFrame manipulation to avoid pandas incompatible dtype insertion.
