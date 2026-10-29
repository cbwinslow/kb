# Specification: Web Glossary Harvester & Sabermetric Presets

## Scope & Purpose
Enables automated web-based retrieval and ingestion of foundational sabermetric definitions, formulas, and empirical constants from seminal sabermetric research blogs and glossaries (e.g., FanGraphs Sabermetric Library, Tom Tango's blog archive). Transforms remote HTML articles into clean Markdown, preserving mathematical notation, tables, and metadata for seamless document and formula ingestion.

## Requirements
1. **Asynchronous Web Harvester**:
   - `WebGlossaryHarvester` in `kb.sync.web` MUST fetch remote pages via `httpx.AsyncClient` with standard User-Agent headers, timeout management, and retry handling.
   - MUST extract primary content containers using `BeautifulSoup` (filtering headers, sidebars, navigation menus, ads, and footers).
   - MUST convert HTML articles to clean Markdown using `markdownify`, preserving LaTeX/math spans and HTML tables.
2. **Canonical Sabermetric Presets**:
   - MUST provide presets for seminal FanGraphs Sabermetric Library entries:
     - wOBA (Weighted On-Base Average)
     - FIP (Fielding Independent Pitching)
     - wRAA (Weighted Runs Above Average)
     - wRC & wRC+ (Weighted Runs Created Plus)
     - Base Runs (David Smyth / Tango)
     - WAR (Wins Above Replacement) position player components
     - WAR pitcher components
   - MUST provide presets for Tom Tango blog archive definitions and constants (*tangotiger.net*).
3. **Pipeline Ingestion**:
   - `WebGlossaryHarvester.ingest_url(url, citekey, title)` and `ingest_preset(preset_key)` MUST ingest processed Markdown content via `IngestionPipeline.ingest_markdown_source`, generating chunks, extracting mathematical formulas, and saving empirical tables to PostgreSQL.
4. **CLI Interface**:
   - CLI commands `kb ingest web --url <url> [--citekey <key>]` and `kb ingest glossary [--preset <name> | --all]` MUST be provided under `kb.cli`.
