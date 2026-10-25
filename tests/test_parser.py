"""Tests for DoclingParser PDF parsing and hardware acceleration fallback."""

from pathlib import Path

import pytest
from docling_core.types.doc.items.text import FormulaItem

from kb.ingest.parser import DoclingParser


def test_parser_device_resolution_cpu() -> None:
    parser = DoclingParser(device="cpu")
    assert parser.device_used == "cpu"


def test_parser_device_resolution_auto_or_cuda() -> None:
    # On cbwwin, if CUDA is present in torch it uses cuda, otherwise falls back to cpu
    parser = DoclingParser(device="auto")
    assert parser.device_used in ("cuda", "cpu")

    # Requesting cuda explicitly must succeed via fallback or direct cuda
    parser_cuda = DoclingParser(device="cuda")
    assert parser_cuda.device_used in ("cuda", "cpu")


def test_parser_file_not_found() -> None:
    parser = DoclingParser(device="cpu")
    with pytest.raises(FileNotFoundError):
        parser.parse_pdf("non_existent_file.pdf")


def test_parser_non_pdf_file(tmp_path: Path) -> None:
    fake_txt = tmp_path / "test.txt"
    fake_txt.write_text("Hello world", encoding="utf-8")
    parser = DoclingParser(device="cpu")
    with pytest.raises(ValueError, match="not a PDF document"):
        parser.parse_pdf(fake_txt)


@pytest.mark.slow
def test_parse_sample_pdf_miller2008() -> None:
    sample_pdf = Path("data/fixtures/miller2008.pdf")
    if not sample_pdf.exists():
        pytest.skip("Sample PDF fixture not found")

    parser = DoclingParser(device="auto", num_threads=4, do_table_structure=True)
    result = parser.parse_pdf(sample_pdf)

    assert result.num_pages > 0
    assert len(result.markdown) > 1000
    assert result.document is not None
    assert "BAYESBALL" in result.markdown
    assert "|" in result.markdown  # Verified markdown table extraction

    # Verify that Docling identifies formula elements in the document AST
    formula_items = [
        item for item, _ in result.document.iterate_items() if isinstance(item, FormulaItem)
    ]
    assert len(formula_items) > 0
