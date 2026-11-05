# openalex-citation-graph Specification

## Purpose
Codifies citation links between academic papers in the knowledge base, enabling bidirectional citation traversal and paper-to-paper derivation path exploration.

## Requirements

### Requirement: Citation Link Data Model (`kb_citations`)
The system SHALL persist citation relationships in `kb_citations` storing `citing_document_id`, `cited_document_id`, and canonical `cited_openalex_id`.

#### Scenario: Storing citation link
- **WHEN** a paper cites another work
- **THEN** system persists directed edge record with foreign keys and OpenAlex identifiers

### Requirement: Citation Graph Builder
`CitationGraphBuilder.build_citation_graph()` MUST scan documents containing `referenced_works`, link matching local documents by `openalex_id` or `doi`, and persist edges in `kb_citations`.

#### Scenario: Building citation graph from referenced works
- **WHEN** builder executes graph synthesis
- **THEN** system resolves referenced works to local documents and updates citation edges

### Requirement: Citation Interfaces
The system SHALL expose citation graph traversal through the CLI (`kb sync citations`) and schema models (`cited_by` and `references`).

#### Scenario: Traversing paper citations via CLI
- **WHEN** user executes `kb sync citations`
- **THEN** system refreshes the citation network and reports newly created citation links

### Requirement: Autonomous Citation Graph Expansion
The system SHALL automatically discover and resolve citation relationships for newly ingested documents against existing corpus works.

#### Scenario: Linking new document to existing corpus works
- **WHEN** a newly harvested paper containing `referenced_works` is ingested into PostgreSQL
- **THEN** system automatically matches cited OpenAlex IDs and DOIs against existing documents and inserts directed citation edges in `kb_citations`

#### Scenario: Re-indexing corpus citation network
- **WHEN** user executes `kb sync citations --backfill`
- **THEN** system scans all unresolved citation references in the corpus and updates `cited_document_id` links for newly available works

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
