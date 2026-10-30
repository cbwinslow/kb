# Proposal: Literature Corpus Expansion & Figure Harvester

## Why
The current corpus in `kb` holds foundational papers up through 2023, but lacks recent 2024–2026 tracking, biomechanics, and aerodynamics literature (such as Hawk-Eye bat tracking, seam-shifted wake aerodynamics, and modern bat-ball impact mechanics). Furthermore, while mathematical formulas and text chunks are ingested with high fidelity, visual figures, diagrams, and trajectory charts are currently omitted from active storage, depriving researchers of critical visual evidence referenced directly in formulas.

## What Changes
- **Targeted Academic Harvester**: Queries OpenAlex and arXiv APIs for 2024–2026 literature focusing on baseball tracking, biomechanics, bat-ball impact elasticity, and wake aerodynamics.
- **Figure Extraction Pipeline**: Enhances the Docling ingestion pipeline to extract `PictureItem` elements, crop high-resolution figure images, persist them to permanent homelab storage via encrypted SFTP (`SSHStorageSync`), and index metadata into `kb_figures`.
- **Automatic Citation Graph Backfilling**: Integrates `CitationGraphBuilder` (`kb sync citations`) into the ingestion daemon, automatically establishing inter-paper citation links (`kb_citations`) as new papers arrive.
- **Figure API & GraphQL Traversal**: Exposes figure queries `/api/documents/{id}/figures` and GraphQL `DocumentType.figures` resolver for frontend visualization.

## Capabilities

### Modified Capabilities
- `figure-extraction-model`: Ingests and stores visual figures, captions, and bounding box layouts from Docling into PostgreSQL and homelab vault.
- `openalex-citation-graph`: Automatically expands the scholarly citation graph for newly ingested 2024–2026 preprints and papers.

## Impact
- **Database**: Populates `kb_figures` table and connects records to `kb_documents` and `kb_chunks`.
- **Storage**: SFTP persistence of cropped images to `cbwdellr720` vault under `/storage/figures/`.
- **Ingestion**: Extends `src/kb/ingest/parser.py` and `src/kb/harvester/daemon.py`.
- **Dependencies**: Uses existing `docling`, `pillow`, `paramiko`. No new third-party dependencies required.
