# Tasks: Web Glossary Ingestion, Symbolic Equation Chaining & GraphQL Knowledge Graph

## Phase 1: Web & Sabermetric Glossary Ingestion
- [x] 1.1 Implement `src/kb/sync/web.py` with `WebGlossaryHarvester`:
  - [x] 1.1.1 Fetch web pages using `httpx.AsyncClient` with user-agent and retry handling.
  - [x] 1.1.2 Parse HTML and extract main article containers via `BeautifulSoup`.
  - [x] 1.1.3 Convert HTML to clean markdown using `markdownify`, preserving LaTeX math expressions and table structures.
  - [x] 1.1.4 Ingest generated markdown and tables via `IngestionPipeline` into database.
- [x] 1.2 Add FanGraphs Library and Tom Tango article presets into `WebGlossaryHarvester` (wOBA, wRAA, FIP, WAR components, Base Runs).
- [x] 1.3 Add CLI commands `kb ingest web --url <url>` and `kb ingest glossary --source <fangraphs|tangotiger>` in `src/kb/cli.py`.
- [x] 1.4 Write unit tests in `tests/test_web_ingest.py` covering HTML conversion, LaTeX formula retention, and markdown pipeline ingestion.

## Phase 2: Symbolic Equation Chaining & System Solver
- [x] 2.1 Implement data models in `src/kb/math/chaining.py`:
  - [x] 2.1.1 `SubstitutionStep` (variable name, source formula ID/citekey, original expr, substituted expr).
  - [x] 2.1.2 `ChainedFormulaResult` (target formula, unified closed-form SymPy expr, closed-form LaTeX, trace steps, primitive symbols, compiled Python & Polars code).
- [x] 2.2 Implement `FormulaChainingEngine`:
  - [x] 2.2.1 Free symbol scanner for formula RHS expressions.
  - [x] 2.2.2 Component equation resolver (`LHS == symbol` or canonical symbol alias match).
  - [x] 2.2.3 Recursive symbolic substitution (`sympy.subs`) with depth control and cycle detection.
  - [x] 2.2.4 Closed-form compiler generating unified Python callable and Polars column expression.
  - [x] 2.2.5 System of equations solver (`sympy.solve`) for simultaneous multi-equation relationships.
- [x] 2.3 Add CLI command `kb formulas chain --formula-id <id>` and `kb formulas solve --ids <id1> <id2>`.
- [x] 2.4 Write unit tests in `tests/test_chaining.py` verifying multi-step substitution (e.g. wOBA $\to$ wRAA $\to$ Batting Runs $\to$ WAR), cycle prevention, and system solving.

## Phase 3: Multi-Layer Mathematical Knowledge Graph & GraphQL API
- [x] 3.1 Implement GraphQL Schema in `src/kb/graphql/schema.py` using `strawberry-graphql`:
  - [x] 3.1.1 `FormulaType` (id, citekey, latex, lhs, rhs, symbols, isValid, isEquality, pythonCode, polarsCode).
  - [x] 3.1.2 `VariableType` (name, canonicalConcept, definingFormulas, usingFormulas).
  - [x] 3.1.3 `ConceptType` (name, latexRepr, description, aliases, formulas).
  - [x] 3.1.4 `DocumentType` (id, citekey, title, authors, year, doi, arxivId, formulas, tables).
  - [x] 3.1.5 `BenchmarkTableType` (id, citekey, caption, numRows, numCols, columns, parquetPath).
  - [x] 3.1.6 `DerivationChainType` (targetId, closedFormLatex, steps, primitiveSymbols, pythonCode, polarsCode).
- [x] 3.2 Implement GraphQL Queries in `src/kb/graphql/schema.py`:
  - [x] 3.2.1 `formulas(citekey, isValid, limit)`
  - [x] 3.2.2 `formula(id)`
  - [x] 3.2.3 `concepts()`
  - [x] 3.2.4 `documents(limit)`
  - [x] 3.2.5 `chainFormula(targetId, maxDepth)`
  - [x] 3.2.6 `knowledgeGraph(limit)`
- [x] 3.3 Mount `/graphql` endpoint onto the Starlette application in `src/kb/ui/app.py` with GraphiQL IDE enabled.
- [x] 3.4 Write unit tests in `tests/test_graphql.py` verifying GraphQL schema, queries, and variable traversal.

## Phase 4: UI Lineage Graph & Derivation Chain Explorer
- [x] 4.1 Update `/api/lineage` endpoint in `src/kb/ui/app.py` to support high-capacity node generation and multi-tier relationships.
- [x] 4.2 Add interactive "Equation Chaining" tab / modal in the Formula Playground:
  - [x] 4.2.1 Select any formula with component variables.
  - [x] 4.2.2 Display live derivation tree and step-by-step substitution breakdown.
  - [x] 4.2.3 Render closed-form unified equation with interactive parameters.
- [x] 4.3 Ensure 100% backward compatibility of all existing UI tabs (`lineage`, `formulas`, `playground`, `tables`, `search`).
- [x] 4.4 Update UI test suite in `tests/test_ui.py` to cover GraphQL endpoint and chaining API.

## Phase 5: Verification, Quality Gates & Spec Synchronization
- [x] 5.1 Record formal ADR-021 (Web Glossary Ingestion), ADR-022 (Symbolic Equation Chaining), and ADR-023 (GraphQL Mathematical Knowledge Graph) in `docs/DECISIONS.md`.
- [x] 5.2 Run `uv run ruff check` and `uv run ruff format` across the codebase.
- [x] 5.3 Run `uv run pyright` ensuring zero errors.
- [x] 5.4 Run `uv run pytest` ensuring all tests pass.
- [x] 5.5 Sync delta specs into `openspec/specs/` and archive the change.
- [x] 5.6 Commit and push clean working tree to GitHub repository.
