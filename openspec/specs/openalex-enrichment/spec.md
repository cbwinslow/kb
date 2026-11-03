# openalex-enrichment Specification

## Purpose
Enriches scientific documents with OpenAlex bibliometric data, citation networks, author concepts, and related research lineages.

## Requirements

### Requirement: OpenAlex Work Entity Resolution
The system SHALL resolve scientific documents to canonical OpenAlex work entities using DOI, arXiv ID, or title search queries.

#### Scenario: Resolve document by DOI or arXiv ID
- **WHEN** user or caller provides a DOI or arXiv ID for an ingested paper
- **THEN** system queries the OpenAlex API and returns the canonical Work entity with OpenAlex ID, citation count, and primary topic

#### Scenario: Fallback resolution by paper title
- **WHEN** document has no DOI or arXiv ID
- **THEN** system queries OpenAlex work search by title and matches candidates using string similarity thresholds

### Requirement: Bibliometric Metadata and Lineage Extraction
The system SHALL extract forward citations, referenced works, concepts/topics, and citation metrics from OpenAlex for persistent storage.

#### Scenario: Extracting referenced works and citation metrics
- **WHEN** an OpenAlex work entity is retrieved
- **THEN** system extracts the list of referenced work IDs, cited-by counts, publication year, and associated topic classifications

### Requirement: OpenAlex Metadata CLI Backfill
The system SHALL provide a CLI command to query OpenAlex and backfill metadata for ingested papers.

#### Scenario: Running batch enrichment via CLI
- **WHEN** user executes `kb enrich openalex --all` or `kb enrich openalex --citekey <key>`
- **THEN** system queries OpenAlex for the target papers and persists resolved work IDs, topics, and citation metrics in the database

### Requirement: Multi-Domain Research Taxonomy Presets
The system SHALL provide curated multi-domain research presets in OpenAlex discovery for automated literature harvesting beyond single-domain sports analytics.

#### Scenario: Querying multi-domain preset harvesters
- **WHEN** user executes `kb sync harvest` with `--preset` set to `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, or `kinematics-tracking`
- **THEN** the system resolves the domain query parameters, searches OpenAlex works with citation ranking and cursor pagination, and filters results against the duplicate resolver

#### Scenario: Validating supported preset names
- **WHEN** user requests available presets or provides an unknown preset name
- **THEN** the system provides the complete list of valid multi-domain presets and rejects unrecognized presets with informative usage guidance
