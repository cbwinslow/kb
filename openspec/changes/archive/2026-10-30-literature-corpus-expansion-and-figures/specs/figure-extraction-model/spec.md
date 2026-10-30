# Spec Delta: figure-extraction-model

## ADDED Requirements

### Requirement: Layout-Aware Figure Image Extraction
The system SHALL extract figure elements from document layout analysis, persist image files to vault storage via SFTP, and index figure captions and bounding box coordinates in `kb_figures`.

#### Scenario: Extracting figures during document ingestion
- **WHEN** a document containing figures or diagrams is processed by Docling
- **THEN** system crops the figure image, uploads the image binary to homelab vault storage via `SSHStorageSync`, and creates a `Figure` record linked to the parent document and caption chunk

#### Scenario: Preserving figure layout metadata
- **WHEN** a figure record is saved
- **THEN** system records the page number, bounding box coordinates, and resolution in `structure_metadata` JSON

### Requirement: Figure Retrieval Interface
The system SHALL provide REST and GraphQL query interfaces to retrieve figures, captions, and vault image URLs for a given document.

#### Scenario: Retrieving document figures
- **WHEN** user or client requests `/api/documents/{id}/figures` or queries `document(id: $id) { figures { id caption imagePath } }`
- **THEN** system returns the ordered list of figure records with captions and image URLs
