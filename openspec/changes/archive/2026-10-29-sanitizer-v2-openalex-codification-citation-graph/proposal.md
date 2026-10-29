# Proposal: Sanitizer 2.0, OpenAlex Codification & Citation Graph

## 1. Problem Statement
1. **Unparsed Formulas (2,366 remaining)**:
   - While the initial sanitizer upgrade recovered 2,481 formulas (+42.1% yield), 2,366 formulas in PostgreSQL remain invalid.
   - Diagnostic auditing revealed the root cause: an execution order inversion in `EquationSanitizer.clean_unicode` where Greek letter macro translation was applied before NFKD alphanumeric decomposition. Consequently, mathematical bold/italic Greek characters in Unicode Plane 1 ($U+1D6A8 - U+1D7CB$, e.g. $\beta, \alpha, \lambda, \tau, \sigma, \mu$) decomposed into standard Unicode Greek letters after the translation loop had already finished, leaving raw Unicode Greek that SymPy ANTLR cannot parse.
   - Furthermore, high-frequency characters identified in our empirical audit (`\u2206` Increment/Delta, `\u2126` Ohm/Omega, `\u2207` Nabla, `\u2020` Dagger, `\u22a4` Transpose, `\u27e8`/`\u27e9` angle brackets, combining accents, and Docling PUA font glyphs `\uf8ec`–`\uf8fb`) remain unhandled.
   - Empirical sampling demonstrates that fixing this order inversion and adding missing character mappings immediately recovers an additional ~620+ formulas, pushing overall corpus yield above 70%.
2. **Missing OpenAlex Entity Codification & Citation Graph**:
   - OpenAlex documents contain rich relational metadata including `referenced_works` (lists of cited OpenAlex IDs), related works, concept hierarchies, and figures/visual assets.
   - Currently, `referenced_works` is stored only as a raw JSON list on `kb_documents`. There is no first-class `CitationLink` entity in PostgreSQL, preventing agents and users from tracing paper-to-paper derivation paths (*Paper A defines formula $F_1$, cited by Paper B which extends it to $F_2$*).
   - Figures, plots, and charts within PDFs are currently not extracted into a dedicated database model, losing visual assets and captions during ingestion.

## 2. Proposed Changes
1. **Universal Equation Sanitizer 2.0 (`src/kb/math/sanitizer.py`)**:
   - Re-architect `EquationSanitizer.clean_unicode`: execute NFKD alphanumeric decomposition first, followed by Unicode operator mapping, Greek letter translation, subscript/superscript conversion, combining accent stripping, and PUA glyph removal.
   - Map missing mathematical symbols: `\u2206` $\to$ `\Delta `, `\u2126` $\to$ `\Omega `, `\u2207` $\to$ `\nabla `, `\u2020` $\to$ `\dagger `, `\u22a4` $\to$ `^T`, `\u27e8`/`\u27e9` $\to$ `\langle `/`\rangle `.
   - Strip combining accents: `\u20d7` (vector arrow), `\u02d9` (dot), `\xaf` (macron), `\u0302` (hat).
   - Strip Docling font-slicing PUA glyphs (`\uf8e0` - `\uf8ff`).
2. **In-Place Corpus Repair Wave 2 (`src/kb/math/repair.py` & CLI)**:
   - Re-run `kb formulas repair` across all remaining invalid formulas in PostgreSQL to recover an estimated 600+ additional formulas.
3. **OpenAlex Citation Graph (`kb_citations`)**:
   - Define `CitationLink` model in `src/kb/storage/models.py` linking `citing_document_id` and `cited_document_id` (or `cited_openalex_id` when external).
   - Implement citation link builder in `src/kb/sync/citations.py` to backfill citation edges across existing stored documents.
   - Expose citation links in GraphQL schema (`DocumentType.cited_by`, `DocumentType.references`) and CLI (`kb sync citations`).
4. **Figure Extraction Entity (`kb_figures`)**:
   - Define `Figure` model in `src/kb/storage/models.py` capturing `caption`, `image_path`, `bounding_box`, `chunk_id`, and `document_id`.

## 3. Success Criteria
- [ ] Sanitizer 2.0 unit tests verify NFKD Greek decomposition, accents, and symbol expansions.
- [ ] Corpus repair Wave 2 recovers an additional 500+ formulas, elevating valid formula yield in PostgreSQL to >68%.
- [ ] `CitationLink` model created and backfilled across existing documents in PostgreSQL.
- [ ] GraphQL queries support citation traversal between papers.
- [ ] All quality gates (`ruff`, `pyright`, `pytest`) pass with zero errors.
