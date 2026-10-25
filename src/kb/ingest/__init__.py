"""Ingestion, parsing, and tabular extraction engine."""

from kb.ingest.chunker import DocumentChunker, EnrichedChunk
from kb.ingest.parser import DoclingParser, ParsedDocument
from kb.ingest.pipeline import (
    BatchIngestionRunner,
    BatchStats,
    DirectorySourceDiscoverer,
    IngestionPipeline,
    IngestionResult,
    OpenAlexSourceDiscoverer,
    PaperSource,
    SourceDiscovererProtocol,
)
from kb.ingest.tables import ExtractedTable, TableExtractor

__all__ = [
    "BatchIngestionRunner",
    "BatchStats",
    "DirectorySourceDiscoverer",
    "DoclingParser",
    "DocumentChunker",
    "EnrichedChunk",
    "ExtractedTable",
    "IngestionPipeline",
    "IngestionResult",
    "OpenAlexSourceDiscoverer",
    "PaperSource",
    "ParsedDocument",
    "SourceDiscovererProtocol",
    "TableExtractor",
]
