# Specification: Multi-Layer Mathematical Knowledge Graph & GraphQL API

## Scope & Purpose
Defines a comprehensive GraphQL API (`/graphql`) powered by Strawberry GraphQL that provides deep relational traversal across the multi-layer mathematical knowledge graph connecting Documents $\leftrightarrow$ Formulas $\leftrightarrow$ Variables $\leftrightarrow$ Canonical Concepts $\leftrightarrow$ Empirical Tables $\leftrightarrow$ Derivation Chains.

## Requirements
1. **Strawberry GraphQL Schema**:
   - `FormulaType`: Exposes `id`, `citekey`, `latex`, `lhs`, `rhs`, `symbols`, `isValid`, `isEquality`, `pythonCode`, `polarsCode`, and parent `document`.
   - `VariableType`: Exposes `name`, `canonicalConcept`, `definingFormulas`, and `usingFormulas`.
   - `ConceptType`: Exposes `name`, `latexRepr`, `description`, `aliases`, and associated `formulas`.
   - `DocumentType`: Exposes `id`, `citekey`, `title`, `authors`, `year`, `doi`, `arxivId`, `formulas`, and `tables`.
   - `BenchmarkTableType`: Exposes `id`, `citekey`, `caption`, `numRows`, `numCols`, `columns`, and `parquetPath`.
   - `DerivationChainType`: Exposes `targetId`, `closedFormLatex`, `steps`, `primitiveSymbols`, `pythonCode`, and `polarsCode`.
2. **GraphQL Queries**:
   - `formulas(citekey: Optional[str], isValid: Optional[bool], limit: int)`
   - `formula(id: str)`
   - `concepts()`
   - `documents(limit: int)`
   - `chainFormula(targetId: str, maxDepth: int)`
   - `knowledgeGraph(limit: int)`: Returns nodes and edges across all layers for network visualization.
3. **Server Integration**:
   - MUST be mounted onto the FastAPI / Starlette UI app at `/graphql`.
   - MUST serve the interactive GraphiQL development interface in browser environments.
