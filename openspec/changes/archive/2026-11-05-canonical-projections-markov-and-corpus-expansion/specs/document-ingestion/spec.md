# Spec Delta: document-ingestion

## ADDED Requirements

### Requirement: Quantitative Methodology Document Ingestion
The ingestion engine SHALL support direct ingestion of structured Markdown technical methodologies, specifications, and quantitative papers, indexing mathematical ASTs and table fixtures into PostgreSQL.

#### Scenario: Ingesting structured quantitative methodology document
- **WHEN** user or pipeline ingests a Markdown methodology document containing LaTeX equations and formulas
- **THEN** system assigns citekey, generates structural chunks with BGE-M3 embeddings, extracts formulas into `kb_formulas`, and preserves raw text in the homelab storage vault

### Requirement: Homelab Storage Preservation and Workstation Disk Hygiene
During batch paper downloads and ingestion sweeps, the ingestion pipeline SHALL push original PDF assets to remote homelab storage via SFTP and unlink temporary staging files, maintaining $\ge 1.5$ GB workstation disk space.

#### Scenario: Ingesting batch preprints with SFTP vaulting
- **WHEN** batch literature ingestion processes multiple remote PDF documents
- **THEN** system vaults each PDF to `cbwdellr720` via SSH/SFTP and removes local temporary files once chunking and embedding are complete
