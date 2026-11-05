# figure-vlm-gallery Specification

## Purpose
TBD - created by archiving change vlm-figure-gallery-and-math-recovery. Update Purpose after archive.

## Requirements

### Requirement: Figure REST API Endpoints
The Starlette web server SHALL provide endpoints to query and retrieve grounded figures and their associated formula entities.

#### Scenario: Listing figures with filters
- **WHEN** client sends `GET /api/figures` with optional `citekey`, `diagram_type`, `q`, or `limit` parameters
- **THEN** system returns a JSON list of matching figures with VLM summaries, detected curves, axes, and linked formula IDs

#### Scenario: Retrieving figure details with resolved formula ASTs
- **WHEN** client sends `GET /api/figures/{id}`
- **THEN** system returns the figure record along with resolved formula metadata (raw LaTeX, sanitized LaTeX, grade, and sympy representation) for all linked formulas

### Requirement: Interactive Figures Gallery Tab
The web UI dashboard SHALL include a dedicated "Figures & Multimodal" navigation tab allowing researchers to browse and inspect figures.

#### Scenario: Browsing figures in dashboard
- **WHEN** user selects the "Figures & Multimodal" tab in the dashboard
- **THEN** system renders a card grid displaying diagram type badges, VLM summaries, axes, and interactive linked formula chips
