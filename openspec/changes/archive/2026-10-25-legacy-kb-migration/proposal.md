# Proposal: Homelab Legacy Knowledge Base Migration

## Why

The homelab PostgreSQL database on `cbwdellr720` already holds 105,627 chunks, 5,209 documents, and 3,790 formulas in the un-typed `public` schema, all with pre-computed 1024-dimensional `bge-m3` vector embeddings. Migrating high-value research papers into our typed `kb_` schema immediately expands the knowledge base by hundreds of foundational sports analytics and sabermetric works without re-downloading PDFs or performing expensive GPU re-embedding, while strictly enforcing quality gates and source table immutability.

## What Changes

- Add `LegacyMigrationAdapter` in `src/kb/storage/legacy_adapter.py` that queries `public` tables in read-only mode and filters for verified, high-quality research documents.
- Synthesize deterministic citation keys (author-year-slug) and structured breadcrumb headers (`[Document: ... | Citekey: ... | Section: ...]`).
- Map pre-existing 1024-d `emb_bgem3` vectors directly into `kb_chunks.embedding` to preserve vector precision and eliminate GPU backfill latency.
- Sanitize and validate LaTeX expressions from `public.formulas` into `kb_formulas` using `FormulaSanitizer` and `FormulaASTGenerator`.
- Add CLI command `kb migrate legacy` with `--dry-run`, `--min-quality`, `--min-relevance`, `--sources`, and `--limit` options.

## Capabilities

### New Capabilities
- `legacy-migration`: Audits, filters, and migrates legacy documents, chunks, and mathematical formulas from `public` schema into typed `kb_` tables with strict quality invariants.

### Modified Capabilities
- `document-ingestion`: Extends ingestion pipelines to accept adapted legacy document records and chunk structures alongside raw PDF ingestion.

## Impact

- **Database**: Strictly read-only against `public.documents`, `public.chunks`, `public.formulas`. Writes only to `kb_documents`, `kb_chunks`, `kb_formulas`.
- **CLI**: Adds `kb migrate legacy` subcommand with dry-run support.
- **Search**: Instantly scales hybrid search retrieval coverage across hundreds of validated research papers.
