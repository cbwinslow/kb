# Design: Literature Corpus Expansion & Figure Harvester

## Overview
This change expands the scholarly literature corpus into 2024–2026 baseball biomechanics and aerodynamics, while codifying visual figures into first-class database entities. By extending the Docling parser pipeline, figure crops (`PictureItem`) are saved remotely onto `cbwdellr720` via SFTP and indexed in `kb_figures`.

## Architecture & Data Flow

```
[OpenAlex / arXiv API Query] (Years: 2024-2026, Keywords: Bat Tracking, Biomechanics, Aerodynamics)
       │
       ▼ [PDF Download]
[Docling Layout & Multimodal Ingestion on cbwwin]
  ├── Text Chunks ────────► kb_chunks (PostgreSQL 16)
  ├── Formulas ($$...$$) ──► kb_formulas (PostgreSQL 16)
  └── PictureItem (Figures) 
         │
         ├── Image Binary ──► SFTP Upload to cbwdellr720 (/storage/figures/<doc_id>_fig_<idx>.png)
         └── Metadata ──────► kb_figures (id, caption, bbox, path)
       │
       ▼ [Citation Traversal]
[CitationGraphBuilder] ────► kb_citations (Linking citing_doc -> cited_doc)
```

## Key Components

### 1. 2024–2026 Targeted Literature Harvester
- Queries OpenAlex with filters:
  - `publication_year:2024-2026`
  - Concepts / Keywords: `baseball`, `biomechanics`, `bat tracking`, `seam-shifted wake`, `spin axis`.
- Integrates arXiv API query for physics/biomechanics preprints.
- Automates download of Open Access PDFs to temporary workspace storage.

### 2. Docling Figure Extraction Pipeline (`src/kb/ingest/parser.py`)
- Configures Docling `PipelineOptions` with `generate_page_images=True`.
- Iterates over document `pictures` or `PictureItem` elements.
- Extracts bounding box coordinates `[x0, y0, x1, y1]` and associated captions.
- Generates unique figure filename: `<citekey>_fig_<index>.png`.

### 3. Remote Vault Archival (`src/kb/sync/ssh.py`)
- Employs `SSHStorageSync` to stream figure images directly to homelab vault storage on `cbwdellr720`.
- Deletes local temporary figure files immediately to adhere to the workstation $\ge 1.5$ GB disk preservation rule (ADR-011).

### 4. Citation Graph Synchronization (`src/kb/sync/citations.py`)
- As papers are inserted, executes `CitationGraphBuilder.link_document(doc_id)`.
- Updates `in_degree` and `out_degree` counts on `kb_documents`.
