# Design: Large-Scale Corpus Expansion & Multi-Attribute Deduplication

## Context
Currently, `kb` processes scientific literature through `IngestionPipeline`, `OpenAlexSourceDiscoverer`, and `PreprintHarvester`. However, deduplication is constrained:
1. `pipeline.py` checks solely for matching `Document.citekey == source.citekey` after the PDF has already been downloaded to the local workstation.
2. `OpenAlexSourceDiscoverer` downloads candidate PDFs over HTTP prior to verifying whether the document already exists in PostgreSQL.
3. Papers ingested from arXiv or directory scans carry citekeys distinct from OpenAlex-derived citekeys, causing identical research works (sharing DOI or title) to be downloaded, parsed with Docling neural OCR, and re-indexed.
4. OpenAlex queries are limited to a single page (up to 50-100 works) without cursor pagination or impact-based sorting (`cited_by_count:desc`), leaving foundational sabermetric papers unharvested.

See `proposal.md` for background and user goals.

## Goals / Non-Goals

**Goals:**
- Provide a unified, high-performance `DuplicateResolver` in `src/kb/ingest/dedup.py` supporting 5 match tiers:
  1. Canonical DOI matching (protocol/case-insensitive: `10.xxxx/...`)
  2. OpenAlex identifier (`W...`)
  3. arXiv identifier (`YYMM.NNNNN`)
  4. Exact citekey match
  5. Normalized title match (lowercased, alphanumeric tokens, length threshold)
- Implement pre-download duplicate checking in both `OpenAlexSourceDiscoverer` and `PreprintHarvester` before issuing HTTP GET requests for PDFs.
- Enable deep cursor-based pagination and impact-based ranking (`sort=cited_by_count:desc`) in OpenAlex client and discoverer to harvest 200+ high-value papers.
- Add curated domain presets for sabermetrics:
  - `mlb-modeling`: Win probability, run expectancy, defensive metrics, WAR.
  - `retrosheet`: Retrosheet event modeling, play-by-play Markov chains, park factors.
  - `statcast`: Hawk-Eye bat tracking, exit velocity, launch angle, seam-shifted wake aerodynamics.
  - `popular`: Highest cited papers across baseball analytics and physics.
  - `baseball-python`: Computational modeling in Python/scientific libraries.
- Maintain homelab storage preservation: upload PDFs to `cbwdellr720` via SFTP and enforce $\ge 1.5$ GB disk space threshold on workstation `cbwwin`.

**Non-Goals:**
- No changes to external `baseballpy` repository.
- No schema changes or table drops in `kb_documents`.
- No removal of existing single-file ingestion CLI commands.

## Decisions

### 1. Multi-Attribute Deduplication Resolver Architecture
We introduce `DuplicateResolver` (`src/kb/ingest/dedup.py`), which accepts candidate metadata (`doi`, `openalex_id`, `arxiv_id`, `citekey`, `title`, `authors`) and queries PostgreSQL with an optimized `OR` query against indexed columns (`doi`, `openalex_id`, `arxiv_id`, `citekey`). If no primary key/ID matches, it tests normalized title similarity against existing documents:
- Title normalization strips punctuation, collapses whitespace, converts to lowercase, and strips common stop words.
- Short titles ($\le 15$ characters) additionally require matching at least one author's surname to prevent false positive collisions.

*Alternative Considered*: Relying strictly on DOI. Rejected because many historical sabermetrics papers, Retrosheet studies, and preprints lack formal DOIs.

### 2. Pre-Download Verification in Discoverers
`OpenAlexSourceDiscoverer` and `PreprintHarvester` are refactored to receive a `DuplicateResolver` (or database session factory). During search/discovery, candidate records are filtered in-memory against database existence *before* calling `http_client.get(pdf_url)`.
- Candidate items already present in the database are immediately logged as `skipped (duplicate)` and excluded from the download queue.
- Saves gigabytes of local workstation disk writes, bandwidth, and Docling OCR execution time.

*Alternative Considered*: Post-download check only. Rejected because downloading 200+ multi-megabyte PDFs over HTTP only to discard them after writing to disk wastes time and risks filling the local disk below the 1.5 GB guardrail.

### 3. Cursor Pagination and Citation-Ranked Harvesting in OpenAlex
We enhance `OpenAlexClient` and `OpenAlexSourceDiscoverer` with `search_works_cursor()`:
- Supports `cursor="*"` and iterative token fetching for arbitrary limits (e.g., 200-500 papers).
- Adds `sort="cited_by_count:desc"` option to prioritize canonical, widely-cited papers over obscure or unvetted articles.
- Includes rate-limiting politeness headers (`mailto:blaine.winslow@gmail.com`) and small delays between cursor pages.

*Alternative Considered*: Offset pagination (`page=1, page=2`). Rejected because OpenAlex limits offset paging to 10,000 results and strongly recommends cursor paging for consistency and deep result sets.

### 4. Preset-Driven CLI Harvesting
`kb sync harvest` is enhanced with:
- `--preset`: Selects from curated preset topic groups (`mlb-modeling`, `retrosheet`, `statcast`, `popular`, `baseball-python`, or `all`).
- `--sort`: Supports `citations` (highest cited first) and `relevance` (search score).
- `--max-papers`: Configurable limit per harvest run (defaulting to 50, expandable to 200+).
- `--dry-run-dedup`: Scans candidate papers and reports duplicates vs. new acquisitions without downloading or modifying the database.

## Risks / Trade-offs

- **[Risk: OpenAlex rate limit during continuous multi-page cursor traversal]**
  → *Mitigation*: Respect OpenAlex polite pool headers, enforce 0.5s pause between page fetches, and handle HTTP 429 with exponential backoff.
- **[Risk: Title normalization false positives across generic titles like "Baseball Analytics"]**
  → *Mitigation*: For titles under 25 characters, require at least one author surname match or publication year alignment before declaring a duplicate.
- **[Risk: Local workstation disk space exhaustion during 200+ paper ingestion]**
  → *Mitigation*: Pipeline processes documents in streaming batches, uploading completed PDFs and figure crops to homelab `cbwdellr720` via `SSHStorageSync` and unlinking local files immediately while keeping free disk space $\ge 1.5$ GB.
