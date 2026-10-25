# Spec Delta: legacy-migration

## Purpose

Enables non-destructive, quality-gated migration of legacy scientific documents, pre-computed vector embeddings, and mathematical formulas from homelab database tables into the typed `kb_` schema.

## ADDED Requirements

### Requirement: Read-Only Legacy Candidate Audit and Filtering
The system SHALL query legacy `public` database tables in read-only mode and filter document candidates by quality threshold, relevance threshold, and verified scientific source domains.

#### Scenario: Filtering candidate documents by quality and source
- **WHEN** migration scans the legacy database with a minimum quality threshold (e.g. 7) and allowed source list (e.g. arxiv, retrosheet-research, sabr-journal)
- **THEN** system returns only document records meeting both the score thresholds and source filters, leaving legacy source tables unaltered

#### Scenario: Skipping low-quality or abstract-only records
- **WHEN** legacy document records originate from unverified sources, abstract snippets, or have quality scores below the threshold
- **THEN** system omits them from the migration candidate list

### Requirement: Deterministic Citekey Synthesis and Metadata Mapping
The system SHALL map legacy document metadata into `kb_documents` records, generating deterministic citation keys from authors, publication year, and title slugs.

#### Scenario: Synthesizing citekey from author and year
- **WHEN** a legacy document has author and publication year metadata
- **THEN** system synthesizes a clean lowercase alphanumeric citekey (e.g. `miller2005` or `tango2006book`) with collision deduplication

#### Scenario: Fallback citekey generation
- **WHEN** a legacy document lacks explicit author or year metadata
- **THEN** system generates a fallback citekey prefixed with `legacy_doc_<doc_id>`

### Requirement: Direct Vector Embedding Transfer
The system SHALL transfer pre-computed 1024-dimensional `emb_bgem3` vectors from `public.chunks` directly into `kb_chunks.embedding` without re-embedding.

#### Scenario: Preserving pre-computed chunk embeddings
- **WHEN** migrating chunks that have existing 1024-dimensional `emb_bgem3` vector arrays
- **THEN** system copies the embedding values directly into `kb_chunks.embedding`, preserving vector precision and bypassing GPU inference

#### Scenario: Formatting chunk breadcrumb headers
- **WHEN** chunks are migrated from legacy tables
- **THEN** chunk content retains or is formatted with structured context breadcrumbs `[Document: ... | Citekey: ... | Section: ...]`

### Requirement: Mathematical Formula Migration and Sanitization
The system SHALL migrate LaTeX mathematical expressions from `public.formulas` into `kb_formulas`, validating syntax with the formula sanitizer.

#### Scenario: Validating and persisting legacy formulas
- **WHEN** legacy formula records associated with migrated documents are processed
- **THEN** system sanitizes the LaTeX string, associates it with the migrated document and corresponding chunk ID, and persists it into `kb_formulas`

#### Scenario: Handling malformed legacy LaTeX
- **WHEN** a legacy formula contains invalid LaTeX syntax that cannot be sanitized
- **THEN** system logs a warning, skips the invalid formula without failing the document migration, and proceeds with valid formulas

### Requirement: Dry-Run and Migration CLI Safety Harness
The system SHALL provide a CLI command `kb migrate legacy` supporting dry-run inspection, batch limits, and transactional safety.

#### Scenario: Executing migration in dry-run mode
- **WHEN** user executes `kb migrate legacy --dry-run`
- **THEN** system reports candidate counts, source distribution, and would-be migrated chunk counts without committing any database writes

#### Scenario: Applying migration with batch limit
- **WHEN** user executes `kb migrate legacy --limit <N>`
- **THEN** system migrates at most `<N>` candidate documents and their associated chunks within managed database transactions
