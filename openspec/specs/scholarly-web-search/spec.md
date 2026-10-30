# Scholarly Web Search Specification

## Purpose
Provide autonomous agents and researchers with live web search capabilities across scientific literature repositories (arXiv API, OpenAlex API) and general quantitative web resources to discover and query research papers beyond local database holdings.

## Requirements

### Requirement 1: Multi-Source Literature Discovery
`ScholarlyWebSearcher` MUST support searching across multiple academic and web endpoints:
1. **arXiv Query API**: Atom XML search supporting author, title, abstract, and category filters.
2. **OpenAlex Search API**: Entity and works discovery with cursor pagination, citation counts, and open-access PDF links.
3. **Web Search Fallback**: Lightweight HTML search for quantitative blogs, technical articles, and online glossaries.

### Requirement 2: Unified Output Schema
All search results MUST normalize into a structured `SearchResult` model containing:
- `title`: Sanitized paper or article title.
- `authors`: List of author names.
- `year`: Publication year.
- `abstract`: Truncated summary or snippet.
- `source`: Originating endpoint (`arxiv`, `openalex`, `web`).
- `url`: Direct landing page or preprint URL.
- `pdf_url`: Direct open-access PDF URL when available.
- `citation_count`: Bibliographic citation count when provided by the source.

### Requirement 3: FastMCP Agent Tool Integration
The FastMCP server MUST expose `kb_web_search_papers(query: str, source: str = "all", max_results: int = 10)` allowing LLM agents to retrieve live papers seamlessly.

### Requirement 4: CLI Search Command
The CLI MUST provide `kb search web "<query>"` with options `--source`, `--limit`, and `--json`.
