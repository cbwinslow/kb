# Proposal: Large-Scale Corpus Expansion & Multi-Attribute Deduplication

## Why
As the `kb` literature corpus expands toward comprehensive coverage of sabermetrics, statistical modeling, Retrosheet analysis, and Statcast tracking, naive ingestion pipelines suffer from duplicate downloads, wasted network bandwidth, and unnecessary Docling neural OCR cycles on previously processed literature. Additionally, the ingestion system currently limits OpenAlex queries to single-page batches without citation-based ranking or pre-download deduplication, leaving hundreds of foundational and seminal sabermetric research papers undiscovered. This change equips `kb` with an intelligent multi-attribute pre-filtering deduplication engine and high-yield cursor-paged harvesting across targeted baseball modeling disciplines.

## What Changes
- **Multi-Attribute Deduplication Resolver**: Pre-download and pre-ingestion duplicate checking across 5 distinct identifiers: DOI, OpenAlex ID, arXiv ID, citekey, and normalized title.
- **Pre-Download Database Filtering**: OpenAlex and arXiv discoverers query existing `kb_documents` before downloading PDF payloads over HTTP, preserving local disk space and network bandwidth.
- **High-Yield Cursor Pagination & Citation Sorting**: OpenAlex harvest queries support deep cursor-based pagination and popularity-based sorting (`sort=cited_by_count:desc`) to retrieve seminal and foundational sabermetrics literature.
- **Specialized Sabermetric & Modeling Query Presets**: Built-in query presets for MLB statistical modeling, Retrosheet analytics, Statcast pitch/hit tracking, baseball trajectory aerodynamics, and open-source baseball Python libraries.
- **CLI Harvest Controls**: Extended CLI flags for `kb sync harvest` (`--sort [citations|relevance]`, `--preset [mlb-modeling|retrosheet|statcast|popular|all]`, `--max-papers`, `--dry-run-dedup`).

## Capabilities

### Modified Capabilities
- `document-ingestion`: Extends document deduplication with multi-attribute identification (DOI, OpenAlex ID, arXiv ID, citekey, normalized title) and pre-download candidate verification before executing PDF retrieval or neural layout parsing.
- `harvester-daemon`: Adds multi-topic preset harvesting, deep cursor-based pagination, citation-ranked sorting (`cited_by_count:desc`), and batch pre-filtering to prevent duplicate downloads and processing.

## Impact
- `src/kb/ingest/dedup.py`: New module providing canonical multi-attribute deduplication resolution against `kb_documents`.
- `src/kb/ingest/pipeline.py`: Updates `OpenAlexSourceDiscoverer` and `IngestionPipeline` to invoke deduplication before downloading or parsing.
- `src/kb/enrich/openalex.py`: Updates OpenAlex client to support cursor-based paging, sort parameters, and high-impact sabermetric query bundles.
- `src/kb/sync/harvester.py`: Integrates pre-download duplicate checks into `PreprintHarvester`.
- `src/kb/cli.py`: Exposes `--sort`, `--preset`, and `--max-papers` in the `kb sync harvest` command.
- Zero breaking changes to existing database schema or CLI contracts.
