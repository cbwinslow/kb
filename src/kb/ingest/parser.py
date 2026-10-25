"""Document parser module wrapping IBM Docling with hardware acceleration and CPU fallback."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import torch
from docling.datamodel.accelerator_options import (
    AcceleratorDevice,
    AcceleratorOptions,
)
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TableFormerMode,
    TableStructureOptions,
)
from docling.document_converter import (
    DocumentConverter,
    FormatOption,
    PdfFormatOption,
)
from docling_core.types.doc.document import DoclingDocument
from pydantic import BaseModel, ConfigDict, Field

logger = logging.getLogger(__name__)


class ParsedDocument(BaseModel):
    """Container for parsed scientific document outputs."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    file_path: str = Field(description="Original file path or URI of the document")
    markdown: str = Field(description="Full exported Markdown representation with LaTeX math")
    document: DoclingDocument = Field(description="Underlying structured Docling Document Model")
    device_used: str = Field(description="Hardware device used for parsing ('cuda' or 'cpu')")
    num_pages: int = Field(default=0, description="Total number of pages in the document")
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Extracted document metadata"
    )


class DoclingParser:
    """PDF parsing engine wrapping IBM Docling with CUDA/GPU acceleration and CPU fallback."""

    def __init__(
        self,
        device: str = "auto",
        num_threads: int = 4,
        do_table_structure: bool = True,
        do_ocr: bool = False,
        do_formula_enrichment: bool = False,
    ) -> None:
        """Initialize DoclingParser with target accelerator and pipeline options.

        Args:
            device: 'auto', 'cuda', or 'cpu'.
            num_threads: Number of worker threads for parallel inference.
            do_table_structure: Whether to extract structured table matrices.
            do_ocr: Whether to run OCR on bitmap scanned documents.
            do_formula_enrichment: Whether to run LaTeX formula recognition VLM.
        """
        self.requested_device = device.lower()
        self.num_threads = num_threads
        self.do_table_structure = do_table_structure
        self.do_ocr = do_ocr
        self.do_formula_enrichment = do_formula_enrichment

        self.device_used, self._accel_device = self._resolve_device(self.requested_device)
        self.converter = self._build_converter()

    def _resolve_device(self, requested: str) -> tuple[str, AcceleratorDevice]:
        """Resolve requested device to available hardware with automatic fallback."""
        cuda_available = torch.cuda.is_available()

        if requested in ("cuda", "auto") and cuda_available:
            dev_name = torch.cuda.get_device_name(0)
            logger.info("Using NVIDIA CUDA acceleration on device: %s", dev_name)
            try:
                # Enable TensorFloat32 on Ampere GPUs for 2x matrix multiplication throughput
                torch.set_float32_matmul_precision("high")
                torch.backends.cudnn.benchmark = True
            except Exception as e:
                logger.debug("Failed configuring cuDNN / matmul precision: %s", e)
            return "cuda", AcceleratorDevice.CUDA

        if requested == "cuda" and not cuda_available:
            logger.warning(
                "CUDA requested but torch.cuda.is_available() is False. Falling back to CPU."
            )

        logger.info("Using multi-threaded CPU acceleration.")
        return "cpu", AcceleratorDevice.CPU

    def _build_converter(self) -> DocumentConverter:
        """Construct the underlying Docling DocumentConverter."""
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_table_structure = self.do_table_structure
        pipeline_options.do_ocr = self.do_ocr
        pipeline_options.do_formula_enrichment = self.do_formula_enrichment
        pipeline_options.layout_batch_size = 8
        pipeline_options.table_batch_size = 8

        if self.do_table_structure:
            pipeline_options.table_structure_options = TableStructureOptions(
                mode=TableFormerMode.FAST,
                do_cell_matching=True,
            )

        pipeline_options.document_timeout = 300.0
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=self.num_threads,
            device=self._accel_device,
        )

        format_options: dict[InputFormat, FormatOption] = {
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
        return DocumentConverter(format_options=format_options)

    def parse_pdf(self, file_path: str | Path, max_num_pages: int = 60) -> ParsedDocument:
        """Parse a PDF document into a structured Markdown document and Docling AST.

        Args:
            file_path: Path to the local PDF file.
            max_num_pages: Cap on maximum pages to parse (default 60 for research papers).

        Returns:
            ParsedDocument with markdown, Docling AST, and metadata.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a PDF.
        """
        path = Path(file_path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"PDF document not found: {path}")
        if path.suffix.lower() != ".pdf":
            raise ValueError(f"Target file is not a PDF document: {path}")

        logger.info(
            "Parsing scientific PDF with Docling: %s (device: %s, max_pages: %d)",
            path.name,
            self.device_used,
            max_num_pages,
        )
        try:
            conv_result = self.converter.convert(
                str(path), page_range=(1, max_num_pages)
            )
            docling_doc = conv_result.document
            markdown_text = docling_doc.export_to_markdown()
        finally:
            if self.device_used == "cuda" and torch.cuda.is_available():
                torch.cuda.empty_cache()

        num_pages = len(docling_doc.pages) if hasattr(docling_doc, "pages") else 0

        return ParsedDocument(
            file_path=str(path),
            markdown=markdown_text,
            document=docling_doc,
            device_used=self.device_used,
            num_pages=num_pages,
            metadata={
                "name": docling_doc.name,
                "origin": str(docling_doc.origin) if hasattr(docling_doc, "origin") else None,
            },
        )
