# Design: Sanitizer 2.0, OpenAlex Codification & Citation Graph

## 1. Universal Equation Sanitizer 2.0 (`src/kb/math/sanitizer.py`)

### Execution Pipeline Reordering
The current `clean_unicode` method runs:
`Operators Map -> Greek Map -> Subscripts -> Superscripts -> NFKD Alphanumerics`

This causes characters in the range $U+1D6A8 - U+1D7CB$ (Mathematical Greek, Bold, Italic) to be decomposed into standard Greek characters (`\u03b1`, `\u03b2`, `\u03bb`, etc.) *after* the Greek replacement map has already executed.

The new pipeline will be structured in explicit stages:
1. **Stage 1 (Decomposition)**:
   - Apply `unicodedata.normalize('NFKD', c)` for all characters in $U+1D400 - U+1D7FF$.
2. **Stage 2 (PUA & Accent Stripping)**:
   - Strip Docling font-slicing PUA characters (`\uf8e0` - `\uf8ff`).
   - Strip combining accents: `\u20d7` (vector arrow), `\u02d9` (dot), `\xaf` (macron), `\u0302` (hat).
3. **Stage 3 (Operator & Symbol Translation)**:
   - Map `\u2206` $\to$ `\Delta `, `\u2126` $\to$ `\Omega `, `\u2207` $\to$ `\nabla `, `\u2020` $\to$ `\dagger `, `\u22a4` $\to$ `^T`, `\u27e8` $\to$ `\langle `, `\u27e9` $\to$ `\rangle `.
   - Apply full `UNICODE_OPERATORS_MAP`.
4. **Stage 4 (Greek Letter Translation)**:
   - Apply full `UNICODE_GREEK_MAP` across all decomposed Greek characters.
5. **Stage 5 (Subscripts & Superscripts)**:
   - Apply `UNICODE_SUBSCRIPTS` and `UNICODE_SUPERSCRIPTS`.

---

## 2. OpenAlex Citation Graph (`src/kb/storage/models.py`, `src/kb/sync/citations.py`)

### Data Model
```python
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

    citing_document: Mapped[Document] = relationship(
        "Document", foreign_keys=[citing_document_id], back_populates="outgoing_citations"
    )
    cited_document: Mapped[Document | None] = relationship(
        "Document", foreign_keys=[cited_document_id], back_populates="incoming_citations"
    )
```

### Backfill & Ingestion Logic (`CitationGraphBuilder`)
- For each document with `referenced_works`:
  - Iterates over referenced OpenAlex IDs.
  - Queries local database for documents where `openalex_id == ref_id` or `doi == ref_doi`.
  - Creates `CitationLink` resolving `cited_document_id` if present in corpus, or keeping `cited_openalex_id` for external references.

---

## 3. Figure Extraction Entity (`kb_figures`)

```python
class Figure(Base):
    """Represents an extracted figure, chart, or visualization from scientific literature."""

    __tablename__ = "kb_figures"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id: Mapped[str] = mapped_column(
        ForeignKey("kb_documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_id: Mapped[str | None] = mapped_column(
        ForeignKey("kb_chunks.id", ondelete="SET NULL"), nullable=True, index=True
    )
    caption: Mapped[str | None] = mapped_column(Text, nullable=True)
    figure_index: Mapped[int] = mapped_column(Integer, default=0)
    image_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    structure_metadata: Mapped[dict[str, Any]] = mapped_column(
        JSON().with_variant(JSONB, "postgresql"), default=dict
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    document: Mapped[Document] = relationship(back_populates="figures")
    chunk: Mapped[Chunk | None] = relationship(back_populates="figures")
```

---

## 4. GraphQL Schema Traversal

Add fields to `DocumentType`:
- `incoming_citation_count: int`
- `outgoing_citation_count: int`
- `cited_by_documents: list[DocumentType]`
- `references_documents: list[DocumentType]`
- `figures: list[FigureType]`
