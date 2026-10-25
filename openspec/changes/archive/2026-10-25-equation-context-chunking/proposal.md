# Proposal: Advanced Context-Aware Chunking & Equation Co-occurrence

## Why

In academic papers across mathematics, physics, and sabermetrics, mathematical equations rarely appear in isolation. Equations are introduced as multi-step derivations where premise, formulation, and variable definitions span multiple sentences or paragraphs. Naive token or paragraph chunking frequently fractures derivations across chunk boundaries, severing an equation from its variable definitions ("where $\mu$ denotes...") or splitting coupled equations (e.g. objective function and constraint equations). Enhancing the chunker to detect equation co-occurrence clusters and enrich chunks with extracted mathematical symbols and cross-references dramatically improves hybrid search recall and retrieval precision for scientific reasoning.

## What Changes

- Implement `EquationContextChunker` (or enhance `DocumentChunker`) with derivation window clustering to keep co-occurring equations and their explanatory "where..." definitions united in a single chunk within token limits.
- Extract and index mathematical symbols and variable definitions from equations and nearby text, embedding a `[Symbols: ...]` context header into `enriched_text`.
- Detect inter-equation cross-references (e.g. "by Equation (1)", "substituting (2) into (3)") and link related equation IDs and chunk IDs.
- Ensure pre-equation and post-equation framing sentences are atomically bound with display math blocks (`$$...$$` and `\begin{equation}...\end{equation}`).

## Capabilities

### Modified Capabilities
- `document-ingestion`: Extends structural chunking requirements to support equation derivation clustering, variable definition window binding, and mathematical context header enrichment.
- `formula-verification`: Extends formula processing to extract free symbols and inter-equation cross-references for relational indexing.

## Impact

- **Ingestion Pipeline**: `src/kb/ingest/chunker.py` adds clustering logic for equation derivation sequences and symbol context enrichment.
- **Formula Extraction**: `src/kb/math/extractor.py` and `sanitizer.py` provide helper methods to extract variable definition clauses and equation label cross-references.
- **Search & Retrieval**: Greatly improves semantic similarity and sparse keyword hits when users search for specific mathematical variables, parameter names, or coupled systems of equations.
