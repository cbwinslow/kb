# Literature Deduplication Specification

## Purpose
Prevent redundant network transfers, duplicated database document records, and repetitive Docling OCR processing by executing multi-attribute deduplication checks prior to downloading external PDFs.

## Requirements

### Requirement 1: Multi-Attribute Candidate Identification
The deduplication engine MUST evaluate incoming paper candidates across five priority tiers:
1. **Canonical DOI**: Exact normalized match ignoring protocol prefixes (`http://`, `https://`, `dx.doi.org/`) and character casing.
2. **OpenAlex Work ID**: Normalized ID matching the canonical format (`W...`).
3. **arXiv ID**: Normalized format (`YYMM.NNNNN` or `math.PR/0501001`), stripping version suffixes when comparing base works.
4. **Citekey Match**: Direct match against BibTeX citekeys in `kb_documents`.
5. **Normalized Title & Authors**: Title comparison ignoring punctuation, whitespace, and capitalization, validated against primary author's surname.

### Requirement 2: Pre-Download Candidate Filtering
Discoverers (e.g., `OpenAlexSourceDiscoverer`, `PreprintHarvester`) MUST verify whether candidates exist in the database BEFORE initiating HTTP file downloads, preserving workstation disk space and network bandwidth.

### Requirement 3: Deduplication Diagnostics
The system MUST provide a `--dry-run-dedup` mode and structured logging detailing why candidates were accepted or rejected.
