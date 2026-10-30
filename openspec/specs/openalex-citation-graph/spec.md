# openalex-citation-graph Specification

## Purpose
Codifies citation links between academic papers in the knowledge base, enabling bidirectional citation traversal and paper-to-paper derivation path exploration.

## Requirements

1. **Citation Link Data Model (`kb_citations`)**:
   - `CitationLink` entity MUST store:
     - `citing_document_id`: Foreign key to `kb_documents.id` (initiating paper).
     - `cited_document_id`: Foreign key to `kb_documents.id` (nullable, resolved when cited paper exists in local corpus).
     - `cited_openalex_id`: Canonical OpenAlex work URI/ID of the cited paper.
2. **Citation Graph Builder**:
   - `CitationGraphBuilder.build_citation_graph()` MUST scan documents containing `referenced_works`, link matching local documents by `openalex_id` or `doi`, and persist edges in `kb_citations`.
3. **Interfaces**:
   - CLI command `kb sync citations [--backfill]` to build or refresh the citation graph.
   - GraphQL schema traversal on `DocumentType`: `cited_by` and `references`.

### Requirement: Autonomous Citation Graph Expansion
The system SHALL automatically discover and resolve citation relationships for newly ingested documents against existing corpus works.

#### Scenario: Linking new document to existing corpus works
- **WHEN** a newly harvested paper containing `referenced_works` is ingested into PostgreSQL
- **THEN** system automatically matches cited OpenAlex IDs and DOIs against existing documents and inserts directed citation edges in `kb_citations`

#### Scenario: Re-indexing corpus citation network
- **WHEN** user executes `kb sync citations --backfill`
- **THEN** system scans all unresolved citation references in the corpus and updates `cited_document_id` links for newly available works
