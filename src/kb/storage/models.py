"""SQLAlchemy 2.0 models for document chunks, formulas, benchmarks, and vector storage."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import JSON


class Base(DeclarativeBase):
    """Base class for all KB storage models."""

    pass


class Document(Base):
    """Represents an ingested scientific paper, report, or publication."""

    __tablename__ = "kb_documents"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    citekey: Mapped[str] = mapped_column(String(128), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    authors: Mapped[list[str]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    doi: Mapped[str | None] = mapped_column(String(128), index=True, nullable=True)
    arxiv_id: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)
    abstract: Mapped[str | None] = mapped_column(Text, nullable=True)
    file_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    openalex_id: Mapped[str | None] = mapped_column(String(128), index=True, nullable=True)
    citation_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    topics: Mapped[list[dict[str, Any]]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    referenced_works: Mapped[list[str]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    extra_metadata: Mapped[dict[str, Any]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=dict
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    chunks: Mapped[list[Chunk]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
        order_by="Chunk.chunk_index",
        lazy="selectin",
    )
    formulas: Mapped[list[Formula]] = relationship(
        back_populates="document", cascade="all, delete-orphan", lazy="selectin"
    )
    benchmark_tables: Mapped[list[BenchmarkTable]] = relationship(
        back_populates="document", cascade="all, delete-orphan", lazy="selectin"
    )
    figures: Mapped[list[Figure]] = relationship(
        back_populates="document", cascade="all, delete-orphan", lazy="selectin"
    )
    outgoing_citations: Mapped[list[CitationLink]] = relationship(
        "CitationLink",
        foreign_keys="[CitationLink.citing_document_id]",
        back_populates="citing_document",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    incoming_citations: Mapped[list[CitationLink]] = relationship(
        "CitationLink",
        foreign_keys="[CitationLink.cited_document_id]",
        back_populates="cited_document",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<Document citekey={self.citekey!r} title={self.title[:40]!r}>"


class Chunk(Base):
    """Represents a semantically enriched structural text chunk."""

    __tablename__ = "kb_chunks"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    citekey: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    raw_text: Mapped[str] = mapped_column(Text, nullable=False)
    enriched_text: Mapped[str] = mapped_column(Text, nullable=False)
    section_path: Mapped[list[str]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    parent_section: Mapped[str | None] = mapped_column(String(256), nullable=True)
    previous_chunk_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    next_chunk_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    has_math: Mapped[bool] = mapped_column(Boolean, default=False)
    has_table: Mapped[bool] = mapped_column(Boolean, default=False)

    # BGE-M3 dense embedding dimension is 1024
    embedding: Mapped[list[float] | None] = mapped_column(Vector(1024), nullable=True)

    # PostgreSQL full-text search vector; renders as TEXT on SQLite
    tsv: Mapped[Any] = mapped_column(Text().with_variant(TSVECTOR, "postgresql"), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    document: Mapped[Document] = relationship(back_populates="chunks")
    formulas: Mapped[list[Formula]] = relationship(
        back_populates="chunk", cascade="all, delete-orphan", lazy="selectin"
    )
    benchmark_tables: Mapped[list[BenchmarkTable]] = relationship(
        back_populates="chunk", cascade="all, delete-orphan", lazy="selectin"
    )
    figures: Mapped[list[Figure]] = relationship(
        back_populates="chunk", cascade="all, delete-orphan", lazy="selectin"
    )

    __table_args__ = (
        Index("ix_chunks_document_index", "document_id", "chunk_index"),
        Index("ix_chunks_citekey_index", "citekey", "chunk_index"),
    )

    def __repr__(self) -> str:
        return f"<Chunk id={self.id!r} citekey={self.citekey!r} idx={self.chunk_index}>"


class Formula(Base):
    """Represents a mathematical equation or formula extracted from scientific literature."""

    __tablename__ = "kb_formulas"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_id: Mapped[str | None] = mapped_column(
        ForeignKey("kb_chunks.id", ondelete="SET NULL"), nullable=True, index=True
    )
    citekey: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    raw_latex: Mapped[str] = mapped_column(Text, nullable=False)
    sanitized_latex: Mapped[str] = mapped_column(Text, nullable=False)
    sympy_repr: Mapped[str | None] = mapped_column(Text, nullable=True)
    symbols: Mapped[list[str]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    is_valid: Mapped[bool] = mapped_column(Boolean, default=False)
    is_equality: Mapped[bool] = mapped_column(Boolean, default=False)
    lhs: Mapped[str | None] = mapped_column(Text, nullable=True)
    rhs: Mapped[str | None] = mapped_column(Text, nullable=True)
    validation_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    validation_status: Mapped[str | None] = mapped_column(String(32), nullable=True)
    validation_details: Mapped[dict[str, Any] | None] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    document: Mapped[Document] = relationship(back_populates="formulas")
    chunk: Mapped[Chunk | None] = relationship(back_populates="formulas")

    def __repr__(self) -> str:
        return f"<Formula id={self.id!r} citekey={self.citekey!r} valid={self.is_valid}>"


class BenchmarkTable(Base):
    """Represents an extracted benchmark or empirical table with Parquet/CSV fixtures."""

    __tablename__ = "kb_benchmark_tables"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_id: Mapped[str | None] = mapped_column(
        ForeignKey("kb_chunks.id", ondelete="SET NULL"), nullable=True, index=True
    )
    citekey: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    caption: Mapped[str | None] = mapped_column(Text, nullable=True)
    parquet_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    csv_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    num_rows: Mapped[int] = mapped_column(Integer, default=0)
    num_cols: Mapped[int] = mapped_column(Integer, default=0)
    column_names: Mapped[list[str]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=list
    )
    schema_metadata: Mapped[dict[str, Any]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=dict
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    document: Mapped[Document] = relationship(back_populates="benchmark_tables")
    chunk: Mapped[Chunk | None] = relationship(back_populates="benchmark_tables")

    def __repr__(self) -> str:
        return (
            f"<BenchmarkTable id={self.id!r} citekey={self.citekey!r} "
            f"shape=({self.num_rows}, {self.num_cols})>"
        )


class CitationLink(Base):
    """Represents a citation relationship between academic papers."""

    __tablename__ = "kb_citations"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    citing_document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    cited_document_id: Mapped[str | None] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="SET NULL"), index=True, nullable=True
    )
    cited_openalex_id: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    citing_document: Mapped[Document] = relationship(
        "Document", foreign_keys=[citing_document_id], back_populates="outgoing_citations"
    )
    cited_document: Mapped[Document | None] = relationship(
        "Document", foreign_keys=[cited_document_id], back_populates="incoming_citations"
    )

    def __repr__(self) -> str:
        return (
            f"<CitationLink citing={self.citing_document_id[:8]!r} "
            f"cited_doc={self.cited_document_id[:8] if self.cited_document_id else 'external'!r}>"
        )


class Figure(Base):
    """Represents an extracted figure, chart, or visual asset from scientific literature."""

    __tablename__ = "kb_figures"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_id: Mapped[str | None] = mapped_column(
        ForeignKey("kb_chunks.id", ondelete="SET NULL"), nullable=True, index=True
    )
    citekey: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    caption: Mapped[str | None] = mapped_column(Text, nullable=True)
    figure_index: Mapped[int] = mapped_column(Integer, default=0)
    image_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    structure_metadata: Mapped[dict[str, Any]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=dict
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # Relationships
    document: Mapped[Document] = relationship(back_populates="figures")
    chunk: Mapped[Chunk | None] = relationship(back_populates="figures")

    def __repr__(self) -> str:
        return f"<Figure id={self.id!r} citekey={self.citekey!r} idx={self.figure_index}>"
