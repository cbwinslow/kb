# Design: Advanced Context-Aware Chunking & Equation Co-occurrence

## Context

See `proposal.md` for motivation.
Currently, `DocumentChunker` in `src/kb/ingest/chunker.py` uses Docling's AST `HierarchicalChunker` or `HybridChunker` to segment documents. While it attaches document and section breadcrumbs (`[Document: ... | Citekey: ... | Section: ...]`), it does not detect when an equation is split from its explanatory "where $x$ denotes..." definitions, nor does it cluster multi-equation derivations that belong together. Additionally, symbols and variable definitions are not surfaced in the context header, causing vector and keyword searches for variable names to miss their parent equations.

## Goals / Non-Goals

**Goals:**
- Provide derivation window clustering that unites sequential coupled equations and their trailing explanatory clauses ("where...", "in which...", "let...") into atomic retrieval chunks within token limits.
- Extract mathematical symbols, Greek parameters, and domain variables, embedding a structured `[Symbols: ...]` context header into `enriched_text`.
- Detect inter-equation cross-references ("by Equation (1)", "substituting (2) into (3)") and record them in chunk metadata.
- Maintain backward compatibility with existing `EnrichedChunk` fields and callers.

**Non-Goals:**
- Modifying underlying PDF OCR layout models.
- Exceeding the 8,192-token context window of `BAAI/bge-m3` (target chunk size remains ~400-800 tokens).

## Decisions

### 1. Post-Processing Derivation Clustering Filter
- **Decision**: Implement derivation clustering as a refinement pass over AST-generated chunks. After initial Docling AST chunking, scan for adjacent chunks within the same subsection where chunk $N$ contains display math or ends with an equation premise, and chunk $N+1$ begins with variable definitions ("where", "in which", "with parameter") or continues the derivation. Merge them if the combined token count remains under `max_derivation_tokens` (default: 800 tokens).
- **Alternative Considered**: Modifying Docling's internal `HierarchicalChunker` rules directly. *Rejected*: Docling's internals are external library code; implementing clustering in our pipeline ensures deterministic behavior and testability without library monkey-patching.

### 2. Structured Symbol Index Context Header
- **Decision**: Prepend extracted symbols to the chunk's enriched header:
  `[Document: "..." | Citekey: ... | Section: ... | Symbols: \mu, \sigma^2, RS]`
- **Rationale**: Both PostgreSQL full-text search (`tsvector`) and `BAAI/bge-m3` dense embeddings weight the beginning of text heavily. Having explicit symbol markers ensures that queries for mathematical parameters ("sigma squared", "mu", "runs scored") match the chunk with high similarity.

### 3. Regex and Variable Clause Extraction
- **Decision**: Extract variable definitions using regex patterns for common scientific conventions:
  - `(?:where|in which|let|with)\s+(\$?[a-zA-Z_\\{}^]+\$?)\s+(?:denotes|represents|is the|being)\s+([^,\n\.]+)`
- **Rationale**: Captures natural language explanations of math symbols and pairs them directly with equation nodes.

## Risks / Trade-offs

- **[Risk] Oversized chunks exceeding embedding token budget** → Enforce hard token limit (`max_tokens=1000`). If merging two derivation chunks would exceed the budget, retain them as separate chunks and link them via `previous_chunk_id` and `next_chunk_id`.
- **[Risk] False positives in "where" clause detection** → Restrict clause binding to chunks that immediately follow an equation (`has_math=True`).
