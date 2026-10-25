"""Database models and hybrid search storage layer."""

from kb.storage.database import DEFAULT_DATABASE_URL, DatabaseManager
from kb.storage.embeddings import (
    DEFAULT_EMBEDDING_MODEL,
    EMBEDDING_DIMENSION,
    EmbeddingProtocol,
    LocalEmbeddingGenerator,
    MockEmbeddingGenerator,
)
from kb.storage.legacy_adapter import (
    DEFAULT_RESEARCH_SOURCES,
    LegacyMigrationAdapter,
    MigrationDocCandidate,
    MigrationStats,
    parse_vector,
)
from kb.storage.models import Base, BenchmarkTable, Chunk, Document, Formula
from kb.storage.search import HybridSearchEngine, SearchResult, reciprocal_rank_fusion

__all__ = [
    "DEFAULT_DATABASE_URL",
    "DEFAULT_EMBEDDING_MODEL",
    "DEFAULT_RESEARCH_SOURCES",
    "EMBEDDING_DIMENSION",
    "Base",
    "BenchmarkTable",
    "Chunk",
    "DatabaseManager",
    "Document",
    "EmbeddingProtocol",
    "Formula",
    "HybridSearchEngine",
    "LegacyMigrationAdapter",
    "LocalEmbeddingGenerator",
    "MigrationDocCandidate",
    "MigrationStats",
    "MockEmbeddingGenerator",
    "SearchResult",
    "parse_vector",
    "reciprocal_rank_fusion",
]
