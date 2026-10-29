# Specification: Figure & Visualization Entity Codification

## Scope & Purpose
Preserves and indexes figures, charts, and plots extracted from scientific literature within PostgreSQL.

## Requirements
1. **Figure Entity Data Model (`kb_figures`)**:
   - `Figure` entity MUST capture:
     - `id`: Unique identifier.
     - `document_id`: Foreign key to `kb_documents.id`.
     - `chunk_id`: Foreign key to `kb_chunks.id` (associated text chunk).
     - `caption`: Full text caption extracted by layout parser.
     - `figure_index`: 0-indexed position within parent document.
     - `image_path`: Path to saved image file in homelab storage.
     - `structure_metadata`: JSON dictionary containing bounding box coordinates and layout attributes.
