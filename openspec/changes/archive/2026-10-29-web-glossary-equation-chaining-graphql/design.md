# Design: Web Glossary Ingestion, Symbolic Equation Chaining & GraphQL Knowledge Graph

## Architecture Overview

```
                                  +---------------------------------------+
                                  |     Web Sabermetric Sources           |
                                  |  - FanGraphs Library / Glossary       |
                                  |  - Tom Tango Blog / Tangotiger.net    |
                                  +-------------------+-------------------+
                                                      |
                                                      v
                                        +---------------------------+
                                        |  Web Ingestion Engine     |
                                        |  (src/kb/sync/web.py)     |
                                        +-------------+-------------+
                                                      |
                                                      v
+-----------------------------------------------------+----------------------------------+
|                                    Core Engine (kb)                                    |
|                                                                                        |
|  +-------------------------------+                 +--------------------------------+  |
|  |   Symbolic Chaining Engine    |                 |   GraphQL & Knowledge Graph    |  |
|  |   (src/kb/math/chaining.py)   |                 |   (src/kb/graphql/schema.py)   |  |
|  |                               |                 |                                |  |
|  | - Component Formula Discovery |                 | - Document, Formula, Variable  |  |
|  | - Recursive AST Substitution  |                 | - Canonical Concept & Table    |  |
|  |   (sympy.subs)                |                 | - Derivation Path Queries      |  |
|  | - Closed-Form Unification     |                 | - Integrated Starlette Route   |  |
|  | - Multi-Equation System Solve |                 |   (/graphql & GraphiQL IDE)    |  |
|  +---------------+---------------+                 +---------------+----------------+  |
|                  |                                                 |                   |
|                  +-----------------------+-------------------------+                   |
|                                          |                                             |
|                                          v                                             |
|                          +-------------------------------+                             |
|                          |   Interactive Web UI & AST    |                             |
|                          |   - Derivation Chain Explorer |                             |
|                          |   - Multi-layer Concept DAG   |                             |
|                          +-------------------------------+                             |
+----------------------------------------------------------------------------------------+
```

## Detailed Component Specifications

### 1. Web & Sabermetric Glossary Ingestion (`src/kb/sync/web.py`)
- **Scraper / Harvester**:
  - `WebGlossaryHarvester`: Downloads HTML from configured URLs (FanGraphs Library, TangoTiger blog posts), extracts the main article content container, converts to Markdown preserving headings, mathematical expressions, formulas, and HTML tables.
  - Generates synthetic document records with citekeys (`fangraphs_woba`, `fangraphs_war_position`, `tangotiger_baseruns_d_factor`) and stores them via `IngestionPipeline`.
  - CLI integration: `kb ingest web --url <url>` and `kb ingest glossary --source fangraphs`.

### 2. Symbolic Equation Chaining & System Solver (`src/kb/math/chaining.py`)
- **Data Models**:
  - `SubstitutionStep`: Tracks substituted variable name, source formula ID/citekey, original expression, and substituted expression.
  - `ChainedFormulaResult`: Contains target formula ID, closed-form unified SymPy expression, closed-form LaTeX string, list of substitution steps, set of required primitive input symbols, and compiled Python / Polars expressions.
- **Engine Logic**:
  - `FormulaChainingEngine.chain(target_formula_id: str, max_depth: int = 5) -> ChainedFormulaResult`:
    1. Loads target formula from database and inspects free symbols of the RHS.
    2. For each free symbol (e.g. `Batting_Runs`), searches for formulas where `LHS == symbol` or normalized symbol matches.
    3. Recursively substitutes component expressions into the main expression.
    4. Tracks substitution lineage and safeguards against circular dependencies.
    5. Returns both the detailed multi-step derivation trace and the compiled unified function.
  - `FormulaChainingEngine.solve_system(formula_ids: list[str], target_symbols: list[str]) -> dict[str, str]`: Solves simultaneous systems of equations using SymPy algebraic solvers (`sympy.solve`).

### 3. Multi-Layer Knowledge Graph & GraphQL API (`src/kb/graphql/schema.py`)
- **GraphQL Schema (Strawberry GraphQL)**:
  - `Query.formulas(citekey, isValid, limit)`: Returns list of formulas with expressions and parameters.
  - `Query.formula(id)`: Returns specific formula with upstream substitutions and downstream dependents.
  - `Query.concepts()`: Returns registered concepts from `SymbolOntology`.
  - `Query.documents(limit)`: Returns ingested research documents.
  - `Query.chainedFormula(targetFormulaId, maxDepth)`: Runs equation chaining on the fly and returns the full derivation tree and closed-form unified expression.
  - `Query.lineageGraph(limit, minOverlap)`: Returns the rich multi-entity graph nodes and edges.
- **Routing**:
  - Mounted on Starlette app at `/graphql` via `GraphQL(schema)`.
  - Includes built-in interactive GraphiQL IDE in the browser.

### 4. Web UI Dashboard Enhancements (`src/kb/ui/app.py`)
- Add an interactive **"Equation Chaining"** explorer into the Formula Playground.
- Update `/api/lineage` to return multi-type nodes (`Formula`, `Concept`, `Document`).
