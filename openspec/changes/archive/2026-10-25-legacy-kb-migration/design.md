# Design: Legacy Knowledge Base Migration

## Context

See `proposal.md` for background and motivation.
The homelab PostgreSQL database on `cbwdellr720` has an existing untyped schema in `public` with 5,209 documents, 105,627 chunks, and 3,790 formulas. Chunks in `public.chunks` already store pre-computed 1024-dimensional `emb_bgem3` embeddings. We have a target typed schema `kb_` (`kb_documents`, `kb_chunks`, `kb_formulas`, `kb_benchmark_tables`) with HNSW indexing and pgvector support.

## Goals / Non-Goals

**Goals:**
- Provide a `LegacyMigrationAdapter` that extracts candidate documents, chunks, and formulas via strictly read-only queries against `public.*`.
- Apply strict quality filters (`quality >= 7`, `relevance >= 7`, verified source list) to harvest only high-value scientific and analytics papers.
- Directly copy the 1024-dimensional `emb_bgem3` vector floats into `kb_chunks.embedding` without re-running neural embedding models.
- Sanitize and link LaTeX formulas from `public.formulas` into `kb_formulas`.
- Implement CLI command `kb migrate legacy` with `--dry-run`, `--limit`, `--min-quality`, `--min-relevance`, and `--sources`.
- Ensure idempotency: skip documents already present in `kb_documents`.

**Non-Goals:**
- Modifying, dropping, or updating any tables, columns, or rows in `public` (100% read-only).
- Migrating uncurated web scrape residue or abstract-only snippets (`harvest-abstract`).
- Re-generating PDF parses or calling Docling on legacy records.

## Decisions

### 1. Read-Only Schema Separation
- **Decision**: All migration queries querying `public.documents`, `public.chunks`, `public.formulas` use explicit schema prefixes (`public.<table_name>`) and exclusively execute `SELECT` queries.
- **Alternative Considered**: Dumping `public` tables to CSV and importing. *Rejected*: PostgreSQL is on the local LAN network; direct in-database migration via `INSERT INTO kb_... SELECT ...` or streaming adapter batches is orders of magnitude faster and preserves vector byte precision.

### 2. Direct Vector Float Array Mapping
- **Decision**: In `public.chunks`, `emb_bgem3` is stored as `vector(1024)`. When reading, `asyncpg`/SQLAlchemy reads this as an array of floats. When inserting into `kb_chunks`, we pass the vector array directly into `embedding`.
- **Rationale**: Re-embedding 11,000+ chunks with `BAAI/bge-m3` on the RTX 3060 would take ~15-30 minutes. Direct transfer takes under 30 seconds and preserves exact numerical equivalence with original embeddings.

### 3. Deterministic Citekey Synthesis
- **Decision**: Synthesize citekeys using author first last name, publication year, and short title slug (e.g. `albert2017pitchfx`), with fallback to `legacy_doc_<doc_id>` if author/year is unavailable. Deduplicate with `_2`, `_3` suffix if collision occurs.
- **Rationale**: `kb_` enforces citekey uniqueness and uses citekeys in search breadcrumbs (`[Document: ... | Citekey: ... | Section: ...]`).

### 4. Formula Sanitization Pipeline
- **Decision**: Run legacy LaTeX strings through `FormulaSanitizer` before inserting into `kb_formulas`. If a formula is unparseable or completely invalid, log a warning and skip the formula record without aborting the chunk or document migration.
- **Rationale**: Legacy scrapers may contain malformed LaTeX fragments. Resilient error handling prevents one broken equation from blocking a high-value research paper.

## Risks / Trade-offs

- **[Risk] High memory usage during large batch migration** → Stream candidate documents in batches of 50-100 rather than fetching all 11,000+ chunks into memory simultaneously.
- **[Risk] Citekey collisions between legacy documents and existing `kb_documents`** → Query existing citekeys in `kb_documents` prior to insertion and append sequential suffixes on collision.
- **[Risk] Missing section paths or breadcrumb structure in legacy chunks** → Synthesize standard breadcrumbs from document title and chunk header/section metadata (`[Document: {title} | Citekey: {citekey} | Section: {section}]`).

## Migration Plan

1. Verify connection to `cbwdellr720` and confirm read-only access to `public`.
2. Run test migration with `--dry-run` to inspect document candidate counts and source distribution.
3. Migrate batch with `--limit 10` and inspect database rows in `kb_documents`, `kb_chunks`, and `kb_formulas`.
4. Validate vector cosine search retrieval across newly migrated documents.
5. Run full migration for verified research sources.
