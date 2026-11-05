# Spec Delta: openalex-citation-graph

## ADDED Requirements

### Requirement: High-Throughput Column Projection Citation Graph Builder
`CitationGraphBuilder` SHALL execute citation graph traversal and linkage queries using explicit column projections (`id`, `openalex_id`, `referenced_works`, `year`) rather than full entity loading, preventing ORM eager `selectin` loading of chunk vector embeddings and formula ASTs.

#### Scenario: Sub-second citation graph construction
- **WHEN** user executes `kb sync citations` across the entire document corpus
- **THEN** the builder queries only document identification and reference columns, completing corpus citation resolution in under 2.0 seconds without hydrating chunks or formulas into memory

### Requirement: Batch Bibliometric Reference Enrichment
The system SHALL support batch resolution of external OpenAlex bibliometric records across all stored documents bearing a DOI or title, updating `openalex_id`, `citation_count`, `topics`, and `referenced_works` in the database.

#### Scenario: Corpus-wide OpenAlex enrichment
- **WHEN** user executes `kb enrich openalex --all`
- **THEN** system queries OpenAlex for each document missing `referenced_works`, persists the resolved work metadata, and commits changes in batched transactions
