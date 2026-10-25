"""Executable runner to ingest the curated sabermetric research corpus into the scientific KB.

Uses the domain-agnostic `DirectorySourceDiscoverer`, `IngestionPipeline`, and
`BatchIngestionRunner` abstractions to process academic PDFs, extract LaTeX formulas,
tables, dense embeddings, and link OpenAlex bibliometrics.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from pathlib import Path

from kb.enrich.openalex import OpenAlexClient
from kb.ingest.pipeline import (
    BatchIngestionRunner,
    DirectorySourceDiscoverer,
    IngestionPipeline,
    IngestionResult,
    PaperSource,
)
from kb.storage.database import DatabaseManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("baseball_ingest")

DEFAULT_SOURCES_DIR = Path("../sabermetricspy-research/sabermetricspy_research/sources")


async def run_corpus_ingestion(
    sources_dir: Path,
    limit: int | None = None,
    dry_run: bool = False,
    force: bool = False,
) -> int:
    """Discovers and ingests baseball research PDFs from the sources directory."""
    resolved_dir = sources_dir.resolve()
    if not resolved_dir.exists():
        print(
            f"[ERROR] Sabermetrics sources directory not found at: {resolved_dir}",
            file=sys.stderr,
        )
        return 1

    print(f"[*] Discovering baseball research papers in: {resolved_dir}")
    discoverer = DirectorySourceDiscoverer(
        root_dir=resolved_dir,
        pattern="*.pdf",
        recursive=True,
        parse_sidecars=True,
    )
    sources: list[PaperSource] = discoverer.discover()
    print(f"[*] Discovered {len(sources)} candidate papers with accompanying metadata.")

    if dry_run:
        print("\n" + "=" * 80)
        print("DRY RUN: Discovered Papers Preview")
        print("=" * 80)
        for idx, src in enumerate(sources[: (limit or len(sources))]):
            authors_str = ", ".join(src.authors or []) if src.authors else "Unknown"
            year_str = str(src.year or "undated")
            title_str = (src.title or src.pdf_path.stem)[:60]
            size_kb = src.pdf_path.stat().st_size // 1024
            print(
                f"[{idx + 1:2d}] {src.citekey:<24} | {year_str} | "
                f"{size_kb:4d} KB | {title_str} ({authors_str})"
            )
        print("=" * 80)
        print(f"Dry run complete. {len(sources)} papers ready for ingestion.")
        return 0

    db_manager = DatabaseManager()
    ok, msg = await db_manager.check_connection()
    if not ok:
        print(f"[ERROR] Database connection failed: {msg}", file=sys.stderr)
        return 1

    await db_manager.init_db()
    openalex_client = OpenAlexClient()

    pipeline = IngestionPipeline(
        db_manager=db_manager,
        openalex_client=openalex_client,
        fixtures_dir=Path("data/fixtures"),
    )
    runner = BatchIngestionRunner(pipeline=pipeline)

    def on_progress(res: IngestionResult) -> None:
        if res.status == "success":
            title_preview = (res.title or res.citekey)[:50]
            print(
                f"[INGESTED] {res.citekey:<22} | {res.chunk_count:3d} chunks | "
                f"{res.formula_count:2d} formulas | {res.table_count:2d} tables | {title_preview}"
            )
        elif res.status == "skipped":
            print(f"[SKIPPED]  {res.citekey:<22} | {res.reason}")
        else:
            print(f"[ERROR]    {res.citekey:<22} | {res.error}", file=sys.stderr)

    print(f"\n[*] Starting ingestion pipeline (limit: {limit or 'ALL'}, force: {force})...\n")
    stats = await runner.run(
        sources=sources,
        max_papers=limit,
        force=force,
        on_progress=on_progress,
    )

    print("\n" + "=" * 80)
    print("Ingestion Execution Summary:")
    print(f"  Total scanned:         {stats.total_scanned}")
    print(f"  Successfully ingested: {stats.total_ingested}")
    print(f"  Skipped (duplicates):  {stats.total_skipped}")
    print(f"  Errors:                {stats.total_errors}")
    print(f"  Chunks created:        {stats.chunks_created}")
    print(f"  Formulas extracted:    {stats.formulas_extracted}")
    print(f"  Tables exported:       {stats.tables_extracted}")
    print("=" * 80)

    await db_manager.close()
    return 0 if stats.total_errors == 0 else 1


def main() -> None:
    """CLI entrypoint for baseball corpus ingestion script."""
    parser = argparse.ArgumentParser(
        description="Ingest baseball and sabermetrics research corpus into scientific KB."
    )
    parser.add_argument(
        "--sources-dir",
        type=Path,
        default=DEFAULT_SOURCES_DIR,
        help=f"Path to sources directory (default: {DEFAULT_SOURCES_DIR})",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum papers to ingest (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and list discovered papers without parsing or database mutations",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing records in database",
    )
    args = parser.parse_args()

    exit_code = asyncio.run(
        run_corpus_ingestion(
            sources_dir=args.sources_dir,
            limit=args.limit,
            dry_run=args.dry_run,
            force=args.force,
        )
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
