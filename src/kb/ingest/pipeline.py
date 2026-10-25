"""Domain-agnostic batch ingestion pipeline, paper discovery, and corpus orchestration."""

from __future__ import annotations

import logging
import re
import time
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

import httpx
from sqlalchemy import select

from kb.enrich.openalex import OpenAlexClient
from kb.ingest.chunker import DocumentChunker
from kb.ingest.parser import DoclingParser
from kb.ingest.tables import TableExtractor
from kb.math.extractor import ExtractedFormula, FormulaExtractor
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import EmbeddingProtocol, LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Chunk, Document, Formula

logger = logging.getLogger(__name__)


@dataclass
class PaperSource:
    """Standardized metadata and location container for candidate research papers."""

    pdf_path: Path
    citekey: str
    title: str | None = None
    authors: list[str] | None = None
    year: int | None = None
    doi: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class IngestionResult:
    """Outcome report for a single paper processed through the ingestion pipeline."""

    citekey: str
    status: str  # "success", "skipped", "error"
    title: str | None = None
    chunk_count: int = 0
    formula_count: int = 0
    table_count: int = 0
    reason: str | None = None
    error: str | None = None
    duration_seconds: float = 0.0


@dataclass
class BatchStats:
    """Aggregated execution metrics across a batch ingestion run."""

    total_scanned: int = 0
    total_ingested: int = 0
    total_skipped: int = 0
    total_errors: int = 0
    chunks_created: int = 0
    formulas_extracted: int = 0
    tables_extracted: int = 0
    errors: list[tuple[str, str]] = field(default_factory=list)

    def record(self, result: IngestionResult) -> None:
        """Records an individual IngestionResult into aggregated metrics."""
        self.total_scanned += 1
        if result.status == "success":
            self.total_ingested += 1
            self.chunks_created += result.chunk_count
            self.formulas_extracted += result.formula_count
            self.tables_extracted += result.table_count
        elif result.status == "skipped":
            self.total_skipped += 1
        elif result.status == "error":
            self.total_errors += 1
            if result.error:
                self.errors.append((result.citekey, result.error))

    def record_error(self, citekey: str, error_msg: str) -> None:
        """Records an unhandled exception for a given citekey."""
        self.total_scanned += 1
        self.total_errors += 1
        self.errors.append((citekey, error_msg))


class SourceDiscovererProtocol(Protocol):
    """Protocol for scientific paper discovery across local or remote sources."""

    def discover(self) -> Iterable[PaperSource]:
        """Discovers candidate paper sources."""
        ...


class DirectorySourceDiscoverer:
    """Discovers research PDFs from flat or hierarchical folder hierarchies.

    Supports parsing sidecar metadata files (SOURCE.md, .bib, or metadata.json)
    to populate title, author, year, and canonical citekeys automatically.
    """

    def __init__(
        self,
        root_dir: Path | str,
        pattern: str = "*.pdf",
        recursive: bool = True,
        parse_sidecars: bool = True,
    ) -> None:
        self.root_dir = Path(root_dir)
        self.pattern = pattern
        self.recursive = recursive
        self.parse_sidecars = parse_sidecars

    def _parse_sidecar_md(self, source_md_path: Path) -> dict[str, Any]:
        """Extracts title, authors, year, and canonical URLs from SOURCE.md."""
        info: dict[str, Any] = {}
        if not source_md_path.exists():
            return info

        try:
            content = source_md_path.read_text(encoding="utf-8", errors="ignore")

            # Extract Citation or Title
            m_cit = re.search(r"\*\*(?:Citation|Title)\*\*:\s*(.+)", content)
            if m_cit:
                raw_cit = m_cit.group(1).strip()
                info["citation"] = raw_cit
                # Look for 'Author(s) (Year). Title'
                m_year = re.search(r"\((\d{4})\)", raw_cit)
                if m_year:
                    info["year"] = int(m_year.group(1))
                    before_year = raw_cit[: m_year.start()].strip()
                    after_year = raw_cit[m_year.end() :].strip().lstrip(".").strip()
                    if before_year:
                        info["authors"] = [a.strip() for a in re.split(r"[;,]", before_year) if a]
                    if after_year:
                        # Extract title before 'arXiv:' or '.'
                        clean_title = re.split(r"(?:arXiv:|\.\s)", after_year)[0].strip()
                        info["title"] = clean_title

            # Extract DOI
            m_doi = re.search(r"https?://(?:dx\.)?doi\.org/([^\s;]+)", content)
            if m_doi:
                info["doi"] = m_doi.group(1).rstrip(".")

            # Extract arXiv ID
            m_arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", content)
            if m_arxiv:
                info["arxiv_id"] = m_arxiv.group(1)

        except Exception as err:
            logger.debug("Failed parsing sidecar %s: %s", source_md_path, err)

        return info

    def discover(self) -> list[PaperSource]:
        """Scans the configured root directory and yields discovered PaperSource entities."""
        if not self.root_dir.exists():
            logger.warning("Source directory does not exist: %s", self.root_dir)
            return []

        sources: list[PaperSource] = []
        seen_paths: set[Path] = set()

        # Strategy A: Check subdirectories (e.g. sources/<citekey>/*.pdf)
        if self.recursive:
            for sub_dir in sorted(self.root_dir.iterdir()):
                if not sub_dir.is_dir() or sub_dir.name.startswith("."):
                    continue

                # Find primary PDF in subdirectory
                pdf_candidates = [
                    p
                    for p in sub_dir.glob(self.pattern)
                    if not p.name.startswith(".") and not p.name.startswith("._")
                ]
                if not pdf_candidates:
                    continue

                # Prioritize a PDF sharing the folder name, or largest primary PDF
                pdf_candidates.sort(
                    key=lambda p: (
                        p.stem == sub_dir.name,
                        p.stat().st_size,
                    ),
                    reverse=True,
                )
                chosen_pdf = pdf_candidates[0]
                if chosen_pdf in seen_paths:
                    continue
                seen_paths.add(chosen_pdf)

                citekey = sub_dir.name.replace(".", "_")
                sidecar_data: dict[str, Any] = {}
                if self.parse_sidecars:
                    source_md = sub_dir / "SOURCE.md"
                    sidecar_data = self._parse_sidecar_md(source_md)

                title = sidecar_data.get("title") or chosen_pdf.stem
                authors = sidecar_data.get("authors")
                year = sidecar_data.get("year")
                doi = sidecar_data.get("doi")

                sources.append(
                    PaperSource(
                        pdf_path=chosen_pdf,
                        citekey=citekey,
                        title=title,
                        authors=authors,
                        year=year,
                        doi=doi,
                        metadata=sidecar_data,
                    )
                )

        # Strategy B: Flat directory PDFs directly in root_dir
        root_pdfs = [
            p
            for p in self.root_dir.glob(self.pattern)
            if p.is_file() and not p.name.startswith(".") and p not in seen_paths
        ]
        for pdf in sorted(root_pdfs):
            seen_paths.add(pdf)
            sources.append(
                PaperSource(
                    pdf_path=pdf,
                    citekey=pdf.stem.replace(".", "_"),
                    title=pdf.stem,
                )
            )

        return sources


class OpenAlexSourceDiscoverer:
    """Discovers Open Access research papers via OpenAlex API queries with high-yield paging."""

    def __init__(
        self,
        openalex_client: OpenAlexClient,
        download_dir: Path | str,
        timeout: float = 30.0,
    ) -> None:
        self.client = openalex_client
        self.download_dir = Path(download_dir)
        self.timeout = timeout

    async def discover(
        self,
        query: str,
        limit: int = 50,
        per_page: int = 50,
    ) -> list[PaperSource]:
        """Queries OpenAlex for relevant OA works and downloads candidate PDFs."""
        self.download_dir.mkdir(parents=True, exist_ok=True)
        url = f"{self.client.base_url}/works"
        params: dict[str, Any] = {
            "search": query,
            "filter": "has_oa_accepted_or_published_version:true",
            "per-page": min(per_page, 100),
        }

        discovered_sources: list[PaperSource] = []

        async with httpx.AsyncClient(
            transport=self.client.transport,
            timeout=self.timeout,
            headers=self.client.get_headers(),
        ) as http_client:
            resp = await http_client.get(url, params=params)
            if resp.status_code != 200:
                logger.error("OpenAlex search query failed [%d]: %s", resp.status_code, resp.text)
                return []

            results = resp.json().get("results", [])
            for item in results:
                if len(discovered_sources) >= limit:
                    break

                work = self.client.parse_work_json(item)
                if not work.pdf_url:
                    continue

                # Generate clean citekey
                author_slug = "anon"
                if work.authors:
                    author_slug = re.sub(r"[^\w]", "", work.authors[0].split()[-1].lower())
                year_slug = str(work.publication_year or "undated")
                citekey = f"openalex_{author_slug}{year_slug}_{work.short_id.lower()}"

                target_pdf = self.download_dir / f"{citekey}.pdf"
                if not target_pdf.exists():
                    try:
                        pdf_resp = await http_client.get(work.pdf_url, follow_redirects=True)
                        if pdf_resp.status_code == 200 and len(pdf_resp.content) > 1000:
                            target_pdf.write_bytes(pdf_resp.content)
                        else:
                            continue
                    except Exception as err:
                        logger.debug("Failed downloading PDF for %s: %s", work.id, err)
                        continue

                discovered_sources.append(
                    PaperSource(
                        pdf_path=target_pdf,
                        citekey=citekey,
                        title=work.title,
                        authors=work.authors,
                        year=work.publication_year,
                        doi=work.doi,
                        metadata={"openalex_id": work.id, "cited_by": work.cited_by_count},
                    )
                )

        return discovered_sources


class IngestionPipeline:
    """Domain-agnostic orchestrator coordinating layout parsing, extraction, and indexing."""

    def __init__(
        self,
        db_manager: DatabaseManager,
        embedder: EmbeddingProtocol | None = None,
        parser: DoclingParser | None = None,
        chunker: DocumentChunker | None = None,
        formula_extractor: FormulaExtractor | None = None,
        table_extractor: TableExtractor | None = None,
        openalex_client: OpenAlexClient | None = None,
        fixtures_dir: Path | str = "data/fixtures",
        gpu_memory_fraction: float | None = 0.55,
    ) -> None:
        self.db = db_manager
        self.embedder = embedder or LocalEmbeddingGenerator()
        self.parser = parser or DoclingParser()
        self.chunker = chunker or DocumentChunker()
        self.formula_extractor = formula_extractor or FormulaExtractor()
        self.table_extractor = table_extractor or TableExtractor()
        self.openalex_client = openalex_client
        self.fixtures_dir = Path(fixtures_dir)

        if gpu_memory_fraction is not None:
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.set_per_process_memory_fraction(gpu_memory_fraction, 0)
                    logger.info(
                        "Configured CUDA per-process memory fraction to %.2f", gpu_memory_fraction
                    )
            except Exception as e:
                logger.debug("Failed configuring CUDA per-process memory fraction: %s", e)

    async def ingest_source(
        self,
        source: PaperSource,
        force: bool = False,
    ) -> IngestionResult:
        """Ingests an individual PaperSource, handling deduplication and storage."""
        start_time = time.monotonic()

        if not source.pdf_path.exists():
            return IngestionResult(
                citekey=source.citekey,
                status="error",
                error=f"PDF file does not exist: {source.pdf_path}",
                duration_seconds=round(time.monotonic() - start_time, 2),
            )

        # 0. Deduplication check
        async with self.db.get_session() as session:
            stmt = select(Document).where(Document.citekey == source.citekey)
            existing = (await session.execute(stmt)).scalar_one_or_none()
            if existing and not force:
                return IngestionResult(
                    citekey=source.citekey,
                    status="skipped",
                    title=existing.title,
                    reason=f"Document '{source.citekey}' already exists in database.",
                    duration_seconds=round(time.monotonic() - start_time, 2),
                )

        # 1. Parse document structure
        try:
            parsed_doc = self.parser.parse_pdf(source.pdf_path)
        except Exception as e:
            return IngestionResult(
                citekey=source.citekey,
                status="error",
                error=f"Docling parsing error: {e}",
                duration_seconds=round(time.monotonic() - start_time, 2),
            )

        # 2. Chunk document with derivation clustering
        enriched_chunks = self.chunker.chunk_document(parsed_doc, citekey=source.citekey)
        if not enriched_chunks:
            return IngestionResult(
                citekey=source.citekey,
                status="error",
                error="Document yielded 0 structural chunks.",
                duration_seconds=round(time.monotonic() - start_time, 2),
            )

        # 3. Extract mathematical formulas
        extracted_formulas: list[ExtractedFormula] = []
        for c in enriched_chunks:
            extracted_formulas.extend(self.formula_extractor.extract_from_chunk(c))

        # 4. Extract tables and export parquet/csv fixtures
        doc_fixtures_dir = self.fixtures_dir / source.citekey
        tables = self.table_extractor.extract_from_docling_document(
            parsed_doc.document,
            citekey=source.citekey,
            document_id=source.citekey,
        )
        fixture_files = self.table_extractor.export_all_fixtures(
            tables, output_dir=doc_fixtures_dir
        )

        # Clear CUDA cache before embedding to isolate memory
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass

        # 5. Compute vector embeddings
        chunk_texts = [c.enriched_text for c in enriched_chunks]
        embeddings = self.embedder.embed_texts(chunk_texts)

        # Clear CUDA cache after embedding
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass

        # 6. Resolve OpenAlex enrichment if client configured
        openalex_work = None
        if self.openalex_client:
            try:
                openalex_work = await self.openalex_client.resolve_work(
                    doi=source.doi,
                    title=source.title or parsed_doc.metadata.get("title"),
                    authors=source.authors,
                    year=source.year,
                )
            except Exception as err:
                logger.debug("OpenAlex resolution failed for %s: %s", source.citekey, err)

        # 7. Persist to database
        doc_title = source.title or str(parsed_doc.metadata.get("title", source.pdf_path.stem))
        doc_year = source.year or (openalex_work.publication_year if openalex_work else None)
        doc_doi = source.doi or (openalex_work.doi if openalex_work else None)

        async with self.db.get_session() as session:
            # Upsert or replace Document
            existing_doc = (
                await session.execute(select(Document).where(Document.citekey == source.citekey))
            ).scalar_one_or_none()

            if existing_doc:
                await session.delete(existing_doc)
                await session.flush()

            doc_record = Document(
                id=source.citekey,
                citekey=source.citekey,
                title=doc_title,
                year=doc_year,
                doi=doc_doi,
                authors=source.authors or [],
                file_path=str(source.pdf_path),
            )
            session.add(doc_record)

            if openalex_work:
                doc_record.openalex_id = openalex_work.id
                doc_record.citation_count = openalex_work.cited_by_count
                doc_record.topics = openalex_work.topics

            await session.flush()

            # Store Chunks
            for idx, c in enumerate(enriched_chunks):
                chunk_record = Chunk(
                    id=c.chunk_id,
                    document_id=doc_record.id,
                    chunk_index=idx,
                    citekey=source.citekey,
                    raw_text=c.raw_text,
                    enriched_text=c.enriched_text,
                    section_path=c.section_path,
                    parent_section=c.parent_section,
                    has_math=c.has_math,
                    has_table=c.has_table,
                    embedding=embeddings[idx] if idx < len(embeddings) else None,
                )
                session.add(chunk_record)

            # Store Formulas
            chunk_id_set = {c.chunk_id for c in enriched_chunks}
            for f_idx, f in enumerate(extracted_formulas):
                unique_formula_id = f"{source.citekey}_form_{f_idx:04d}_{f.formula_id}"
                form_record = Formula(
                    id=unique_formula_id,
                    document_id=doc_record.id,
                    chunk_id=f.chunk_id if f.chunk_id in chunk_id_set else None,
                    citekey=source.citekey,
                    raw_latex=f.raw_latex,
                    sanitized_latex=f.sanitized_latex,
                    sympy_repr=str(f.sympy_expr) if f.sympy_expr is not None else None,
                    symbols=f.symbols,
                    is_valid=f.is_valid,
                    is_equality=f.is_equality,
                    lhs=f.lhs,
                    rhs=f.rhs,
                )
                session.add(form_record)

            # Store Tables
            for idx, t in enumerate(tables):
                pq_path = (
                    str(fixture_files[idx][0].resolve())
                    if idx < len(fixture_files)
                    else None
                )
                csv_path = (
                    str(fixture_files[idx][1].resolve())
                    if idx < len(fixture_files)
                    else None
                )
                tbl_record = BenchmarkTable(
                    id=t.table_id,
                    document_id=doc_record.id,
                    chunk_id=None,
                    citekey=source.citekey,
                    caption=t.caption,
                    parquet_path=pq_path,
                    csv_path=csv_path,
                    num_rows=t.num_rows,
                    num_cols=t.num_cols,
                    column_names=t.column_names,
                    schema_metadata={"sha256": t.metadata.get("sha256")},
                )
                session.add(tbl_record)

            await session.commit()

        return IngestionResult(
            citekey=source.citekey,
            status="success",
            title=doc_title,
            chunk_count=len(enriched_chunks),
            formula_count=len(extracted_formulas),
            table_count=len(tables),
            duration_seconds=round(time.monotonic() - start_time, 2),
        )


class BatchIngestionRunner:
    """Manages execution of an IngestionPipeline across an iterable stream of PaperSources."""

    def __init__(self, pipeline: IngestionPipeline) -> None:
        self.pipeline = pipeline

    async def run(
        self,
        sources: Iterable[PaperSource],
        max_papers: int | None = None,
        force: bool = False,
        on_progress: Callable[[IngestionResult], None] | None = None,
    ) -> BatchStats:
        """Executes batch ingestion over paper sources with progress reporting."""
        stats = BatchStats()

        for count, src in enumerate(sources):
            if max_papers is not None and count >= max_papers:
                break

            # Host disk protection guard to prevent out-of-space on cbwwin
            try:
                import shutil

                free_gb = shutil.disk_usage("C:\\").free / (1024**3)
                if free_gb < 1.0:
                    logger.error(
                        "Host disk C: is critically low (%.2f GB free). Halting batch ingestion.",
                        free_gb,
                    )
                    break
            except Exception:
                pass

            try:
                result = await self.pipeline.ingest_source(src, force=force)
                stats.record(result)
                if on_progress:
                    on_progress(result)
            except Exception as err:
                logger.error("Unexpected error ingesting %s: %s", src.citekey, err, exc_info=True)
                stats.record_error(src.citekey, str(err))

        return stats
