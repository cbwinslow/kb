# Proposal: Web Glossary Ingestion, Symbolic Equation Chaining & GraphQL Knowledge Graph

## 1. Problem Statement
The scientific knowledge base contains 262 ingested research papers, 5,833 extracted formulas, and 1,256 empirical tables. However, four critical limitations restrict the platform's ability to model complete sabermetric architectures:
1. **Absence of Web Sabermetric Glossaries & Blog Repositories**: Foundational definitions, constants, and derivation narratives (e.g. FanGraphs Library articles on wOBA, wRAA, FIP, and WAR; Tom Tango's Tangotiger blog archive on Base Runs, RE24, and Marcel) are published on web pages rather than academic LaTeX PDFs. The existing ingestion pipeline is PDF-centric.
2. **Disconnected Component Formulas (Lack of Symbolic Chaining)**: Equations are treated as isolated vertices without deep mathematical composition. For example, when high-level metrics like $\text{WAR}$ take intermediate variables ($\text{Batting Runs}, \text{wRAA}, \text{wOBA}$) as inputs, the system cannot automatically discover their definitions and substitute them recursively (`sympy.subs`) to produce closed-form unified equations from raw counting statistics.
3. **Restricted Lineage Visualization**: The existing UI lineage graph was clamped to 150 nodes and used shallow lexical symbol overlap, obscuring true semantic and mathematical derivation hierarchies across the 5,800+ formula corpus.
4. **Lack of a Unified Graph Query Interface**: Developers and downstream research pipelines lack a structured GraphQL API to traverse relationships connecting Documents $\leftrightarrow$ Formulas $\leftrightarrow$ Variables $\leftrightarrow$ Canonical Concepts $\leftrightarrow$ Empirical Tables.

## 2. Proposed Solution
1. **Web & Sabermetric Glossary Ingestion Engine (`src/kb/sync/web.py`)**:
   - Asynchronous web crawler and cleaner using `httpx`, `bs4`, and `markdownify`.
   - Dedicated crawlers for **FanGraphs Sabermetric Glossary / Library** (wOBA, FIP, wRAA, wRC, wRC+, WAR, UBR, wSB, RE24, WPA) and **Tom Tango's blog archive**.
   - Extracts equations, definitions, empirical linear weights, and tables directly into standard Markdown and feeds them through `IngestionPipeline`.
2. **Symbolic Equation Chaining & System Solver (`src/kb/math/chaining.py`)**:
   - `FormulaChainingEngine`: Analyzes formula RHS free symbols, resolves component definitions matching `LHS == symbol`, and performs recursive symbolic substitution (`sympy.subs`).
   - Produces multi-tier derivation trees ($wOBA \to wRAA \to Batting\_Runs \to WAR$), closed-form unified equations, and vectorized Polars expressions.
   - Solves simultaneous systems of equations using SymPy algebraic solvers (`sympy.solve`).
3. **Multi-Tier Mathematical Knowledge Graph & GraphQL API (`src/kb/graphql/`)**:
   - Built with `strawberry-graphql` and integrated into the Starlette application at `/graphql`.
   - Exposes strongly typed schemas for `Formula`, `Variable`, `Concept`, `Document`, `BenchmarkTable`, and `DerivationChain`.
   - Supports upstream and downstream derivation tracing, concept-based filtering, and real-time execution.
4. **Enhanced UI Lineage Graph & Chaining Sandbox (`src/kb/ui/app.py`)**:
   - Interactive derivation tree explorer in the Web UI Playground.
   - High-capacity force-directed/hierarchical graph view linking concepts, formulas, and papers.

## 3. Impact & Portability
- 100% portable across Windows, Linux, and macOS.
- Zero hardcoded credentials or paths; fully integrated with `kb.config.settings`.
- Completely non-breaking: preserves all existing CLI commands, UI tabs, and REST endpoints.
