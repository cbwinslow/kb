"""Document chunker module providing structural AST chunking and context enrichment."""

from __future__ import annotations

import hashlib
import logging
import re
from pathlib import Path
from typing import Any

from docling_core.transforms.chunker.base import BaseChunk
from docling_core.transforms.chunker.doc_chunk import DocChunk
from docling_core.transforms.chunker.hierarchical_chunker import HierarchicalChunker
from docling_core.transforms.chunker.hybrid_chunker import HybridChunker
from docling_core.types.doc.document import DoclingDocument
from docling_core.types.doc.items.table.table import TableItem
from docling_core.types.doc.items.text import FormulaItem
from pydantic import BaseModel, ConfigDict, Field

from kb.ingest.parser import ParsedDocument

logger = logging.getLogger(__name__)

# Regular expressions for LaTeX equations
MATH_DISPLAY_RE = re.compile(r"\$\$([\s\S]*?)\$\$")
MATH_INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)([^\n$]+?)(?<!\$)\$(?!\$)")
MATH_ENV_RE = re.compile(
    r"\\begin\{(equation|align|aligned|gather|matrix|bmatrix|pmatrix)\*?\}[\s\S]*?\\end\{\1\*?\}"
)
TABLE_LINE_RE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)


class EnrichedChunk(BaseModel):
    """Pristine structural chunk enriched with hierarchical provenance."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    chunk_id: str = Field(description="Deterministic unique ID for the chunk")
    document_id: str = Field(description="Parent document identifier")
    citekey: str = Field(default="", description="BibTeX citation key of the document")
    chunk_index: int = Field(description="Zero-based sequence index within document")
    raw_text: str = Field(description="Raw markdown / content of the chunk")
    enriched_text: str = Field(
        description="Text prepended with full heading breadcrumbs and metadata for indexing"
    )
    section_path: list[str] = Field(
        default_factory=list, description="Ordered ancestry of section headings"
    )
    parent_section: str = Field(default="", description="Immediate parent heading name")
    previous_chunk_id: str | None = Field(
        default=None, description="Pointer to preceding chunk ID"
    )
    next_chunk_id: str | None = Field(default=None, description="Pointer to subsequent chunk ID")
    has_math: bool = Field(
        default=False, description="Whether this chunk contains LaTeX mathematical expressions"
    )
    has_table: bool = Field(
        default=False, description="Whether this chunk contains tabular matrices"
    )
    math_expressions: list[str] = Field(
        default_factory=list, description="Extracted mathematical expressions in this chunk"
    )
    num_tokens: int = Field(default=0, description="Estimated token count of enriched text")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional chunk metadata")


class DocumentChunker:
    """Structural document chunker respecting AST node boundaries and section hierarchies."""

    def __init__(
        self,
        mode: str = "hierarchical",
        repeat_table_header: bool = True,
        always_emit_headings: bool = True,
    ) -> None:
        """Initialize DocumentChunker.

        Args:
            mode: 'hierarchical' for pure AST boundary chunks, or 'hybrid' for token-budget chunks.
            repeat_table_header: Whether to repeat table column headers across split tables.
            always_emit_headings: Whether to always include section headers in chunk text.
        """
        self.mode = mode.lower()
        self.repeat_table_header = repeat_table_header
        self.always_emit_headings = always_emit_headings

        if self.mode == "hybrid":
            self._chunker = HybridChunker(
                repeat_table_header=self.repeat_table_header,
                always_emit_headings=self.always_emit_headings,
            )
        else:
            self._chunker = HierarchicalChunker()

    def chunk_document(
        self,
        document_input: ParsedDocument | DoclingDocument,
        citekey: str = "",
        document_id: str = "",
    ) -> list[EnrichedChunk]:
        """Chunk a parsed document into structurally sound and enriched semantic chunks.

        Args:
            document_input: ParsedDocument instance or DoclingDocument AST.
            citekey: BibTeX citation key (e.g. 'miller2008').
            document_id: Unique document ID. If empty, derived deterministically.

        Returns:
            List of EnrichedChunk instances with context breadcrumbs and relational pointers.
        """
        if isinstance(document_input, ParsedDocument):
            docling_doc = document_input.document
            doc_name = document_input.metadata.get("name") or Path(document_input.file_path).stem
        else:
            docling_doc = document_input
            doc_name = docling_doc.name or "untitled"

        if not document_id:
            raw_hash = hashlib.sha256((citekey or doc_name).encode("utf-8")).hexdigest()[:12]
            document_id = f"doc_{raw_hash}"

        raw_chunks = list(self._chunker.chunk(docling_doc))
        enriched_chunks: list[EnrichedChunk] = []

        total_chunks = len(raw_chunks)
        for idx, base_chunk in enumerate(raw_chunks):
            chunk_id = f"{document_id}_chunk_{idx:04d}"
            raw_text = base_chunk.text.strip()

            headings = self._extract_headings(base_chunk)
            parent_section = headings[-1] if headings else ""

            # Detect math expressions from AST items and text patterns
            math_exprs = self._extract_math_expressions(base_chunk, raw_text)
            has_math = len(math_exprs) > 0

            # Detect tabular data from AST items and markdown formatting
            has_table = self._detect_tables(base_chunk, raw_text)

            # Build enriched breadcrumb header
            breadcrumb_str = " > ".join(headings) if headings else "Root"
            header_parts: list[str] = [f'Document: "{doc_name}"']
            if citekey:
                header_parts.append(f"Citekey: {citekey}")
            header_parts.append(f"Section: {breadcrumb_str}")

            breadcrumb_header = f"[{' | '.join(header_parts)}]"
            enriched_text = f"{breadcrumb_header}\n\n{raw_text}" if raw_text else breadcrumb_header

            # Rough token estimate (character length / 4)
            num_tokens = max(1, len(enriched_text) // 4)

            prev_id = f"{document_id}_chunk_{idx - 1:04d}" if idx > 0 else None
            next_id = f"{document_id}_chunk_{idx + 1:04d}" if idx < total_chunks - 1 else None

            chunk = EnrichedChunk(
                chunk_id=chunk_id,
                document_id=document_id,
                citekey=citekey,
                chunk_index=idx,
                raw_text=raw_text,
                enriched_text=enriched_text,
                section_path=headings,
                parent_section=parent_section,
                previous_chunk_id=prev_id,
                next_chunk_id=next_id,
                has_math=has_math,
                has_table=has_table,
                math_expressions=math_exprs,
                num_tokens=num_tokens,
            )
            enriched_chunks.append(chunk)

        math_count = sum(1 for c in enriched_chunks if c.has_math)
        table_count = sum(1 for c in enriched_chunks if c.has_table)
        logger.info(
            "Chunked %s into %d chunks (math: %d, tables: %d)",
            document_id,
            len(enriched_chunks),
            math_count,
            table_count,
        )
        return enriched_chunks

    def _extract_headings(self, chunk: BaseChunk) -> list[str]:
        """Extract ordered heading breadcrumbs from chunk metadata."""
        if isinstance(chunk, DocChunk):
            headings = getattr(chunk.meta, "headings", None)
            if headings and isinstance(headings, list):
                return [str(h).strip() for h in headings if str(h).strip()]
        return []

    def _extract_math_expressions(self, chunk: BaseChunk, text: str) -> list[str]:
        """Extract LaTeX equations from Docling AST items and raw text."""
        exprs: list[str] = []

        # Check underlying AST items
        if isinstance(chunk, DocChunk):
            doc_items = getattr(chunk.meta, "doc_items", None)
            if doc_items and isinstance(doc_items, list):
                for item in doc_items:
                    if isinstance(item, FormulaItem):
                        expr_text = ""
                        if item.text and item.text.strip():
                            expr_text = item.text.strip()
                        elif item.orig and str(item.orig).strip():
                            expr_text = str(item.orig).strip()
                        else:
                            expr_text = f"[Formula: {getattr(item, 'self_ref', 'eq')}]"

                        if expr_text not in exprs:
                            exprs.append(expr_text)

        # Regex fallback on text
        for match in MATH_DISPLAY_RE.finditer(text):
            m = match.group(0).strip()
            if m not in exprs:
                exprs.append(m)

        for match in MATH_ENV_RE.finditer(text):
            m = match.group(0).strip()
            if m not in exprs:
                exprs.append(m)

        for match in MATH_INLINE_RE.finditer(text):
            m = match.group(0).strip()
            if m not in exprs and len(m) > 2:
                exprs.append(m)

        return exprs

    def _detect_tables(self, chunk: BaseChunk, text: str) -> bool:
        """Detect whether chunk contains tabular matrices."""
        if isinstance(chunk, DocChunk):
            doc_items = getattr(chunk.meta, "doc_items", None)
            if doc_items and isinstance(doc_items, list):
                for item in doc_items:
                    if isinstance(item, TableItem):
                        return True

        return bool(TABLE_LINE_RE.search(text))
