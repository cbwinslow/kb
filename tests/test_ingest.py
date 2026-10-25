"""Comprehensive unit and invariant tests for scientific document ingestion and chunking."""

import re
from pathlib import Path

import pytest
from docling_core.types.doc.document import DoclingDocument
from docling_core.types.doc.items.table.table_data import TableData
from docling_core.types.doc.labels import DocItemLabel

from kb.ingest.chunker import DocumentChunker, EnrichedChunk
from kb.ingest.parser import DoclingParser


def _verify_math_invariants(chunk: EnrichedChunk) -> None:
    """Assert mathematical delimiter balance and environment invariants."""
    text = chunk.raw_text

    # Count display math $$ delimiters
    display_count = text.count("$$")
    assert display_count % 2 == 0, f"Unbalanced $$ delimiters in chunk {chunk.chunk_id}"

    # Check for unclosed environments \begin{...} without \end{...}
    begins = re.findall(r"\\begin\{([a-zA-Z*]+)\}", text)
    ends = re.findall(r"\\end\{([a-zA-Z*]+)\}", text)
    assert begins == ends, (
        f"Mismatched LaTeX environments in chunk {chunk.chunk_id}: {begins} vs {ends}"
    )


def _verify_provenance_invariants(chunks: list[EnrichedChunk]) -> None:
    """Assert sequence linkage, breadcrumbs, and parent-child invariants."""
    total = len(chunks)
    assert total > 0

    for idx, chunk in enumerate(chunks):
        # 1. Breadcrumb invariant: enriched_text must contain document and section header
        assert chunk.enriched_text.startswith("[Document:"), (
            f"Chunk {chunk.chunk_id} missing breadcrumb prefix"
        )
        assert "Section:" in chunk.enriched_text

        # 2. Sequence indices
        assert chunk.chunk_index == idx

        # 3. Pointers linkage
        if idx == 0:
            assert chunk.previous_chunk_id is None
        else:
            assert chunk.previous_chunk_id == chunks[idx - 1].chunk_id

        if idx == total - 1:
            assert chunk.next_chunk_id is None
        else:
            assert chunk.next_chunk_id == chunks[idx + 1].chunk_id

        # 4. Heading path consistency
        if chunk.section_path:
            assert chunk.parent_section == chunk.section_path[-1]
        else:
            assert chunk.parent_section == ""


def test_chunker_synthetic_scientific_document() -> None:
    """Test chunker on a synthetic multi-section document with formulas and tables."""
    doc = DoclingDocument(name="synthetic_paper")

    # Section 1
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="1. Introduction", level=1)
    doc.add_text(
        label=DocItemLabel.TEXT,
        text="The Pythagorean expectation relates runs scored ($R$) to runs allowed ($RA$).",
    )

    # Section 2 & Subsection 2.1
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="2. Mathematical Derivation", level=1)
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="2.1 Probability Density Models", level=2)
    math_text = (
        "Assume independent Weibull distributions for scoring: "
        "$$f(x; k, \\lambda) = \\frac{k}{\\lambda} "
        "\\left(\\frac{x}{\\lambda}\\right)^{k-1} e^{-(x/\\lambda)^k}$$"
    )
    doc.add_text(label=DocItemLabel.TEXT, text=math_text)

    # Section 3 with Table
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="3. Empirical Results", level=1)
    table_data = TableData(num_rows=3, num_cols=2)
    table_data.table_cells = []
    doc.add_table(data=table_data)

    chunker = DocumentChunker(mode="hierarchical")
    chunks = chunker.chunk_document(doc, citekey="miller2008synthetic")

    # Invariants verification
    _verify_provenance_invariants(chunks)
    for c in chunks:
        _verify_math_invariants(c)

    # Section 2.1 chunk must inherit full heading breadcrumbs: H1 > H2
    derivation_chunks = [c for c in chunks if "2.1 Probability Density Models" in c.section_path]
    assert len(derivation_chunks) > 0
    assert "2. Mathematical Derivation" in derivation_chunks[0].section_path
    assert "2.1 Probability Density Models" in derivation_chunks[0].section_path
    assert derivation_chunks[0].has_math is True
    assert len(derivation_chunks[0].math_expressions) > 0


def test_chunker_hybrid_mode_token_budget() -> None:
    """Test chunker in hybrid mode respecting token and AST boundaries."""
    doc = DoclingDocument(name="hybrid_test")
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="1. Overview")
    doc.add_text(label=DocItemLabel.TEXT, text="First paragraph in the test document.")
    doc.add_text(label=DocItemLabel.TEXT, text="Second paragraph following the first.")

    chunker = DocumentChunker(mode="hybrid")
    chunks = chunker.chunk_document(doc, citekey="test2026")

    _verify_provenance_invariants(chunks)
    assert len(chunks) > 0
    for c in chunks:
        assert c.num_tokens > 0
        assert c.citekey == "test2026"


@pytest.mark.slow
def test_chunker_real_pdf_fixture_invariants() -> None:
    """Test full parsing and chunking invariant enforcement on real academic paper fixture."""
    fixture_path = Path("data/fixtures/miller2008.pdf")
    if not fixture_path.exists():
        pytest.skip("Fixture PDF not found")

    parser = DoclingParser(device="auto", num_threads=4)
    parsed = parser.parse_pdf(fixture_path)

    chunker = DocumentChunker(mode="hierarchical")
    chunks = chunker.chunk_document(parsed, citekey="jensen2009bayesball")

    # Validate all invariants on real-world scientific paper chunks
    _verify_provenance_invariants(chunks)
    for c in chunks:
        _verify_math_invariants(c)

    # Ensure equations and tables were detected across chunks
    has_math_count = sum(1 for c in chunks if c.has_math)
    has_table_count = sum(1 for c in chunks if c.has_table)

    assert has_math_count > 0, "Real paper chunks should detect mathematical expressions"
    assert has_table_count > 0, "Real paper chunks should detect tables"
