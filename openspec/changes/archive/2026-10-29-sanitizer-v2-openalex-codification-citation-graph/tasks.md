# Tasks: Sanitizer 2.0, OpenAlex Codification & Citation Graph

## Phase 1: Universal Equation Sanitizer 2.0
- [x] 1.1 Refactor Unicode sanitization pipeline in `src/kb/math/sanitizer.py`:
  - [x] 1.1.1 Execute NFKD decomposition first across $U+1D400 - U+1D7FF$ before any symbol translation.
  - [x] 1.1.2 Strip Docling PUA font glyphs in range `\uf8e0` through `\uf8ff`.
  - [x] 1.1.3 Strip combining accents: `\u20d7` (vector arrow), `\u02d9` (dot), `\xaf` (macron), `\u0302` (hat).
  - [x] 1.1.4 Map missing symbols: `\u2206` $\to$ `\Delta `, `\u2126` $\to$ `\Omega `, `\u2207` $\to$ `\nabla `, `\u2020` $\to$ `\dagger `, `\u22a4` $\to$ `^T`, `\u27e8` $\to$ `\langle `, `\u27e9` $\to$ `\rangle `.
  - [x] 1.1.5 Apply `UNICODE_GREEK_MAP` after NFKD decomposition so mathematical bold/italic Greek characters convert to LaTeX commands.
- [x] 1.2 Write unit tests in `tests/test_sanitizer_coverage.py`:
  - [x] 1.2.1 Test Mathematical Bold Greek (`\U0001D6FD` $\to$ `\beta`).
  - [x] 1.2.2 Test Increment, Ohm, Nabla, Dagger, Transpose, and angle brackets.
  - [x] 1.2.3 Test combining accent and PUA font stripping.

## Phase 2: In-Place Corpus Repair Wave 2
- [x] 2.1 Re-run `kb formulas repair` across remaining invalid formulas in PostgreSQL.
- [x] 2.2 Verify newly recovered formula count and update `FormulaCoverageReport`.
- [x] 2.3 Verify AST validity and free symbol extraction on newly recovered formulas.

## Phase 3: OpenAlex Citation Graph & Entity Codification
- [x] 3.1 Define `CitationLink` model in `src/kb/storage/models.py`:
  - [x] 3.1.1 Add `kb_citations` table with `citing_document_id`, `cited_document_id`, `cited_openalex_id`.
  - [x] 3.1.2 Add relationships to `Document`: `incoming_citations` and `outgoing_citations`.
- [x] 3.2 Define `Figure` model in `src/kb/storage/models.py`:
  - [x] 3.2.1 Add `kb_figures` table with `document_id`, `chunk_id`, `caption`, `figure_index`, `image_path`, `structure_metadata`.
  - [x] 3.2.2 Add relationship to `Document`: `figures`.
- [x] 3.3 Implement `CitationGraphBuilder` in `src/kb/sync/citations.py`:
  - [x] 3.3.1 Scan documents with `referenced_works`.
  - [x] 3.3.2 Resolve internal cited documents and external OpenAlex IDs.
  - [x] 3.3.3 Backfill citation links into `kb_citations`.
- [x] 3.4 Add CLI command `kb sync citations [--backfill]` in `src/kb/cli.py`.
- [x] 3.5 Write unit tests in `tests/test_citations.py`.

## Phase 4: GraphQL & Web UI Integration
- [x] 4.1 Update `DocumentType` in `src/kb/graphql/schema.py`:
  - [x] 4.1.1 Add `cited_by` and `references` relationships.
  - [x] 4.1.2 Add `citation_network` query resolving multi-hop paper citations.
- [x] 4.2 Expose citation counts on UI Document badges in `src/kb/ui/app.py`.

## Phase 5: Verification & Quality Gates
- [x] 5.1 Record formal ADR-025 in `docs/DECISIONS.md`.
- [x] 5.2 Run `uv run ruff check` and `uv run ruff format`.
- [x] 5.3 Run `uv run pyright` ensuring zero type errors.
- [x] 5.4 Run `uv run pytest` ensuring complete test suite passes.
- [x] 5.5 Sync delta specs to `openspec/specs/` and archive the change.
- [x] 5.6 Commit and push clean working tree to GitHub repository.
