# Proposal: OpenAlex Citation & Lineage Enrichment

## Why

Scientific papers in the knowledge base currently store internal section chunks, formulas, and benchmark tables, but lack bibliographic context—such as forward citations, seminal reference lineages, concepts/topics, and citation counts. Integrating OpenAlex allows automated discovery of seminal papers, tracking of methodological evolutions (e.g., how subsequent sabermetric research refined Miller's 2005 Pythagorean expectation exponent), and exposes rich citation graph exploration directly to AI agents via FastMCP tools.

## What Changes

- Add `OpenAlexClient` in `src/kb/enrich/openalex.py` to resolve paper metadata (DOI, arXiv ID, or title) to OpenAlex Work entities.
- Store OpenAlex entity IDs, topic tags, citation counts, and referenced works in PostgreSQL (`kb_documents` or relational lineage tables).
- Expose new FastMCP tools:
  - `kb_get_citations`: Retrieve papers citing or cited by a given paper.
  - `kb_get_related_papers`: Retrieve topically and structurally related literature from OpenAlex for deeper research context.
- Add CLI command `kb enrich openalex [--citekey <key> | --all]` to query OpenAlex and backfill metadata for ingested papers.

## Capabilities

### New Capabilities
- `openalex-enrichment`: Resolves scientific papers to OpenAlex works, extracts bibliometric metadata, topics, citation counts, and traverses citation/reference graphs.

### Modified Capabilities
- `mcp-server`: Adds `kb_get_citations` and `kb_get_related_papers` query tools for literature lineage exploration.
- `document-ingestion`: Extends document records with OpenAlex work IDs, citation metrics, and topic concepts.

## Impact

- **Database**: Extends `kb_documents` with `openalex_id`, `citation_count`, `topics`, `referenced_works` fields, or creates relational link table.
- **MCP Server**: Exposes new FastMCP citation graph and related paper tools.
- **Dependencies**: Uses `httpx` (already installed or standard async HTTP) or OpenAlex API client.
- **CLI**: Adds `kb enrich openalex` subcommand.
