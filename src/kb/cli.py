"""Command-line interface (CLI) for Scientific Knowledge Base (kb)."""

from __future__ import annotations

import argparse
import asyncio
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from kb.enrich.openalex import OpenAlexClient

from sqlalchemy import select

from kb.storage.database import DatabaseManager
from kb.storage.embeddings import EmbeddingProtocol, LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Chunk, Document, Formula


async def async_db_check() -> int:
    """Verifies connection to PostgreSQL or configured database."""
    manager = DatabaseManager()
    ok, message = await manager.check_connection()
    if ok:
        print(f"[OK] {message}")
        await manager.close()
        return 0
    print(f"[ERROR] {message}", file=sys.stderr)
    await manager.close()
    return 1


async def async_db_init() -> int:
    """Initializes schema and vector extensions."""
    manager = DatabaseManager()
    await manager.init_db()
    print("[OK] Database schema initialized successfully.")
    await manager.close()
    return 0


async def async_ingest(
    pdf_path: Path,
    citekey: str,
    title: str | None = None,
    authors: list[str] | None = None,
    year: int | None = None,
    embedder: EmbeddingProtocol | None = None,
    manager: DatabaseManager | None = None,
) -> int:
    """Ingests a scientific paper PDF, extracts formulas/tables, and stores in database."""
    if not pdf_path.exists():
        print(f"[ERROR] File not found: {pdf_path}", file=sys.stderr)
        return 1

    print(f"[*] Ingesting paper: {pdf_path.name} (citekey: {citekey})...")
    from kb.ingest.chunker import DocumentChunker
    from kb.ingest.parser import DoclingParser
    from kb.ingest.tables import TableExtractor
    from kb.math.extractor import ExtractedFormula, FormulaExtractor

    parser = DoclingParser()
    parsed_doc = parser.parse_pdf(pdf_path)

    # 1. Chunk document
    chunker = DocumentChunker()
    enriched_chunks = chunker.chunk_document(parsed_doc, citekey=citekey)
    print(f"[*] Generated {len(enriched_chunks)} structural chunks.")

    # 2. Extract formulas
    extractor = FormulaExtractor()
    extracted_formulas: list[ExtractedFormula] = []
    for c in enriched_chunks:
        extracted_formulas.extend(extractor.extract_from_chunk(c))
    print(f"[*] Extracted {len(extracted_formulas)} formulas.")

    # 3. Extract tables
    table_extractor = TableExtractor()
    doc_title = title or str(parsed_doc.metadata.get("title", pdf_path.stem))
    fixtures_dir = Path("data/fixtures") / citekey
    tables = table_extractor.extract_from_docling_document(
        parsed_doc.document, citekey=citekey, document_id=citekey
    )
    fixture_files = table_extractor.export_all_fixtures(tables, output_dir=fixtures_dir)
    print(
        f"[*] Extracted {len(tables)} tables "
        f"({len(fixture_files)} fixtures exported to {fixtures_dir})."
    )

    # 4. Compute dense vector embeddings
    print(f"[*] Computing 1024-d dense embeddings for {len(enriched_chunks)} chunks...")
    active_embedder = embedder or LocalEmbeddingGenerator()
    chunk_texts = [c.enriched_text for c in enriched_chunks]
    embeddings = active_embedder.embed_texts(chunk_texts)

    # 5. Store in database
    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    async with db_manager.get_session() as session:
        doc = Document(
            citekey=citekey,
            title=doc_title,
            authors=authors or [],
            year=year,
            file_path=str(pdf_path.resolve()),
        )
        session.add(doc)
        await session.flush()

        # Add chunks with embeddings
        chunk_models: dict[str, Chunk] = {}
        for idx, c in enumerate(enriched_chunks):
            chunk_model = Chunk(
                id=c.chunk_id,
                document_id=doc.id,
                chunk_index=c.chunk_index,
                citekey=citekey,
                raw_text=c.raw_text,
                enriched_text=c.enriched_text,
                section_path=c.section_path,
                parent_section=c.parent_section,
                previous_chunk_id=c.previous_chunk_id,
                next_chunk_id=c.next_chunk_id,
                has_math=c.has_math,
                has_table=c.has_table,
                embedding=embeddings[idx] if idx < len(embeddings) else None,
            )
            session.add(chunk_model)
            chunk_models[c.chunk_id] = chunk_model

        await session.flush()

        # Add formulas
        for f in extracted_formulas:
            formula_model = Formula(
                document_id=doc.id,
                chunk_id=f.chunk_id if f.chunk_id in chunk_models else None,
                citekey=citekey,
                raw_latex=f.raw_latex,
                sanitized_latex=f.sanitized_latex,
                sympy_repr=str(f.sympy_expr) if f.sympy_expr is not None else None,
                symbols=f.symbols,
                is_valid=f.is_valid,
                is_equality=f.is_equality,
                lhs=f.lhs,
                rhs=f.rhs,
            )
            session.add(formula_model)

        # Add tables
        for idx, t in enumerate(tables):
            pq_path = str(fixture_files[idx][0].resolve()) if idx < len(fixture_files) else None
            csv_path = str(fixture_files[idx][1].resolve()) if idx < len(fixture_files) else None
            table_model = BenchmarkTable(
                document_id=doc.id,
                citekey=citekey,
                caption=t.caption,
                parquet_path=pq_path,
                csv_path=csv_path,
                num_rows=t.num_rows,
                num_cols=t.num_cols,
                column_names=t.column_names,
                schema_metadata=t.metadata,
            )
            session.add(table_model)

    if manager is None:
        await db_manager.close()
    print(f"[SUCCESS] Ingestion completed and committed to database for {citekey}!")
    return 0


async def async_ingest_batch(
    dir_path: Path,
    pattern: str = "*.pdf",
    limit: int | None = None,
    force: bool = False,
    manager: DatabaseManager | None = None,
) -> int:
    """Batch ingests scientific papers from a directory hierarchy with deduplication."""
    if not dir_path.exists():
        print(f"[ERROR] Source directory not found: {dir_path}", file=sys.stderr)
        return 1

    from kb.enrich.openalex import OpenAlexClient
    from kb.ingest.pipeline import (
        BatchIngestionRunner,
        DirectorySourceDiscoverer,
        IngestionPipeline,
    )

    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    discoverer = DirectorySourceDiscoverer(root_dir=dir_path, pattern=pattern)
    sources = discoverer.discover()
    print(f"[*] Discovered {len(sources)} candidate papers in {dir_path}")

    pipeline = IngestionPipeline(
        db_manager=db_manager,
        openalex_client=OpenAlexClient(),
    )
    runner = BatchIngestionRunner(pipeline=pipeline)

    def on_progress(res: Any) -> None:
        if res.status == "success":
            print(
                f"[INGESTED] {res.citekey} ({res.chunk_count} chunks, "
                f"{res.formula_count} formulas, {res.table_count} tables)"
            )
        elif res.status == "skipped":
            print(f"[SKIPPED] {res.citekey} - {res.reason}")
        else:
            print(f"[ERROR] {res.citekey} - {res.error}", file=sys.stderr)

    stats = await runner.run(sources, max_papers=limit, force=force, on_progress=on_progress)

    print("\n" + "=" * 60)
    print("Batch Ingestion Summary:")
    print(f"  Total scanned:         {stats.total_scanned}")
    print(f"  Successfully ingested: {stats.total_ingested}")
    print(f"  Skipped (duplicates):  {stats.total_skipped}")
    print(f"  Errors:                {stats.total_errors}")
    print(f"  Chunks created:        {stats.chunks_created}")
    print(f"  Formulas extracted:    {stats.formulas_extracted}")
    print(f"  Tables extracted:      {stats.tables_extracted}")
    print("=" * 60)

    if manager is None:
        await db_manager.close()

    return 0


async def async_ingest_openalex(
    query: str,
    download_dir: Path | None = None,
    limit: int = 50,
    per_page: int = 50,
    force: bool = False,
    manager: DatabaseManager | None = None,
) -> int:
    """Discovers Open Access research papers via OpenAlex and runs batch ingestion."""
    from kb.enrich.openalex import OpenAlexClient
    from kb.ingest.pipeline import (
        BatchIngestionRunner,
        IngestionPipeline,
        OpenAlexSourceDiscoverer,
    )

    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    target_dir = download_dir or Path("data/openalex_papers")
    client = OpenAlexClient()
    discoverer = OpenAlexSourceDiscoverer(openalex_client=client, download_dir=target_dir)

    print(f"[*] Querying OpenAlex for query '{query}' (limit: {limit}, per-page: {per_page})...")
    sources = await discoverer.discover(query=query, limit=limit, per_page=per_page)
    print(f"[*] Retrieved {len(sources)} Open Access papers with full PDFs ready for pipeline.")

    pipeline = IngestionPipeline(db_manager=db_manager, openalex_client=client)
    runner = BatchIngestionRunner(pipeline=pipeline)

    def on_progress(res: Any) -> None:
        if res.status == "success":
            print(f"[INGESTED] {res.citekey}: {res.title} ({res.chunk_count} chunks)")
        elif res.status == "skipped":
            print(f"[SKIPPED] {res.citekey} - {res.reason}")
        else:
            print(f"[ERROR] {res.citekey} - {res.error}", file=sys.stderr)

    stats = await runner.run(sources, max_papers=limit, force=force, on_progress=on_progress)

    print("\n" + "=" * 60)
    print(f"OpenAlex Batch Ingestion for '{query}':")
    print(f"  Successfully ingested: {stats.total_ingested}")
    print(f"  Skipped (duplicates):  {stats.total_skipped}")
    print(f"  Errors:                {stats.total_errors}")
    print(f"  Chunks created:        {stats.chunks_created}")
    print(f"  Formulas extracted:    {stats.formulas_extracted}")
    print("=" * 60)

    if manager is None:
        await db_manager.close()

    return 0


async def async_embed(
    citekey: str | None = None,
    embed_all: bool = False,
    embedder: EmbeddingProtocol | None = None,
    manager: DatabaseManager | None = None,
) -> int:
    """Computes and stores dense vector embeddings for chunks missing embeddings."""
    if not citekey and not embed_all:
        print("[ERROR] Specify --citekey <key> or --all to embed chunks.", file=sys.stderr)
        return 1

    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    async with db_manager.get_session() as session:
        stmt = select(Chunk).where(Chunk.embedding.is_(None))
        if citekey:
            stmt = stmt.where(Chunk.citekey == citekey)

        res = await session.execute(stmt)
        chunks = list(res.scalars().all())

        if not chunks:
            target = f"for citekey '{citekey}'" if citekey else "in database"
            print(f"[*] No chunks missing embeddings {target}.")
            if manager is None:
                await db_manager.close()
            return 0

        print(f"[*] Embedding {len(chunks)} chunks...")
        active_embedder = embedder or LocalEmbeddingGenerator()
        texts = [c.enriched_text for c in chunks]
        vectors = active_embedder.embed_texts(texts, batch_size=16)

        for chunk, vec in zip(chunks, vectors, strict=True):
            chunk.embedding = vec

        await session.flush()

    if manager is None:
        await db_manager.close()
    print(f"[SUCCESS] Successfully embedded and updated {len(chunks)} chunks in PostgreSQL!")
    return 0


async def async_enrich_openalex(
    citekey: str | None = None,
    enrich_all: bool = False,
    client: OpenAlexClient | None = None,
    manager: DatabaseManager | None = None,
) -> int:
    """Enriches stored documents with OpenAlex bibliometric metadata and topics."""
    from kb.enrich.openalex import OpenAlexClient

    if not citekey and not enrich_all:
        print("[ERROR] Specify --citekey <key> or --all to enrich documents.", file=sys.stderr)
        return 1

    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    openalex_client = client or OpenAlexClient()

    async with db_manager.get_session() as session:
        stmt = select(Document)
        if citekey:
            stmt = stmt.where(Document.citekey == citekey)

        res = await session.execute(stmt)
        docs = list(res.scalars().all())

        if not docs:
            print("[*] No documents found to enrich.")
            if manager is None:
                await db_manager.close()
            return 0

        print(f"[*] Querying OpenAlex for {len(docs)} documents...")
        enriched_count = 0
        for doc in docs:
            print(f"[*] Resolving: {doc.citekey} - '{doc.title[:40]}'...")
            work = await openalex_client.resolve_work(
                doi=doc.doi,
                arxiv_id=doc.arxiv_id,
                title=doc.title,
                authors=doc.authors,
                year=doc.year,
            )
            if work:
                doc.openalex_id = work.id
                doc.citation_count = work.cited_by_count
                doc.topics = work.topics
                doc.referenced_works = work.referenced_works
                enriched_count += 1
                print(
                    f"    [MATCH] OpenAlex ID: {work.short_id} | "
                    f"Citations: {work.cited_by_count} | Topics: {len(work.topics)}"
                )
            else:
                print(f"    [WARN] No match found on OpenAlex for {doc.citekey}")

        await session.flush()

    if manager is None:
        await db_manager.close()

    print(f"[SUCCESS] Successfully enriched {enriched_count}/{len(docs)} documents!")
    return 0


async def async_migrate_legacy(
    dry_run: bool = False,
    min_quality: int = 7,
    min_relevance: int = 7,
    sources: list[str] | None = None,
    limit: int | None = None,
    manager: DatabaseManager | None = None,
) -> int:
    """Audits and migrates high-quality documents and chunks from legacy schema."""
    from kb.storage.legacy_adapter import LegacyMigrationAdapter

    db_manager = manager or DatabaseManager()
    await db_manager.init_db()

    adapter = LegacyMigrationAdapter(db_manager=db_manager)
    mode_label = "[DRY-RUN] " if dry_run else ""
    print(
        f"[*] {mode_label}Starting legacy homelab migration audit "
        f"(min_quality={min_quality}, min_relevance={min_relevance})..."
    )

    def on_progress(current: int, total: int, cand: Any) -> None:
        safe_title = cand.title[:45].encode("ascii", errors="replace").decode("ascii")
        print(
            f"    [{current}/{total}] {cand.source}: {safe_title} "
            f"(Q:{cand.quality}, R:{cand.relevance})"
        )

    stats = await adapter.migrate_batch(
        min_quality=min_quality,
        min_relevance=min_relevance,
        sources=sources,
        limit=limit,
        dry_run=dry_run,
        on_progress=on_progress,
    )

    print("\n" + "=" * 55)
    print(f"[*] {mode_label}Migration Summary:")
    print(f"    Scanned Candidates:  {stats.scanned_candidates}")
    print(f"    Migrated Documents:  {stats.migrated_documents}")
    print(f"    Migrated Chunks:     {stats.migrated_chunks}")
    print(
        f"    Migrated Formulas:   {stats.migrated_formulas} "
        f"({stats.valid_formulas} symbolically validated)"
    )
    print(f"    Failed Documents:    {stats.failed_documents}")
    print("=" * 55)

    if manager is None:
        await db_manager.close()

    return 0 if stats.failed_documents == 0 else 1


async def async_search(
    query: str,
    limit: int = 5,
    citekey: str | None = None,
    manager: DatabaseManager | None = None,
) -> int:
    """Executes hybrid vector + full-text search across ingested chunks."""
    from kb.storage.search import HybridSearchEngine

    db_manager = manager or DatabaseManager()
    engine = HybridSearchEngine(db_manager=db_manager)

    print(f"[*] Running hybrid search for: '{query}' (limit={limit})...")
    async with db_manager.get_session() as session:
        hits = await engine.hybrid_search(
            session=session,
            query_text=query,
            limit=limit,
            citekey=citekey,
        )

    if not hits:
        print("[*] No matching literature found.")
        if manager is None:
            await db_manager.close()
        return 0

    print(f"\n[SUCCESS] Found {len(hits)} matching chunks:\n")
    for idx, hit in enumerate(hits, 1):
        print(
            f"--- Hit #{idx} [Citekey: {hit.citekey}] "
            f"(RRF: {hit.rrf_score:.4f}, Dense: #{hit.dense_rank}, Sparse: #{hit.sparse_rank}) ---"
        )
        section = (
            " > ".join(hit.section_path)
            if hit.section_path
            else (hit.parent_section or "Main")
        )
        print(f"Section: {section}")
        preview = hit.text.replace("\n", " ")[:200]
        safe_preview = preview.encode("ascii", errors="replace").decode("ascii")
        print(f"Content: {safe_preview}...\n")

    if manager is None:
        await db_manager.close()
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Builds the argument parser for kb CLI."""
    parser = argparse.ArgumentParser(
        prog="kb",
        description="Scientific Knowledge Base CLI & Research Engine",
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    # mcp serve
    mcp_parser = subparsers.add_parser("mcp", help="Model Context Protocol commands")
    mcp_sub = mcp_parser.add_subparsers(dest="mcp_subcommand")
    mcp_sub.add_parser("serve", help="Run the FastMCP server daemon")

    # db commands
    db_parser = subparsers.add_parser("db", help="Database management commands")
    db_sub = db_parser.add_subparsers(dest="db_subcommand")
    db_sub.add_parser("check", help="Test connectivity to PostgreSQL 16 on cbwdellr720")
    db_sub.add_parser("init", help="Create database tables and vector extensions")

    # ingest command
    ingest_parser = subparsers.add_parser("ingest", help="Ingest scientific papers into KB")
    ingest_parser.add_argument(
        "pdf_path",
        type=Path,
        nargs="?",
        default=None,
        help="Path to PDF file, or mode keyword ('batch', 'search-openalex')",
    )
    ingest_parser.add_argument(
        "--citekey", type=str, default=None, help="BibTeX citation key (required for single PDF)"
    )
    ingest_parser.add_argument("--title", type=str, default=None, help="Paper title")
    ingest_parser.add_argument("--authors", nargs="+", default=[], help="Authors list")
    ingest_parser.add_argument("--year", type=int, default=None, help="Publication year")
    ingest_parser.add_argument(
        "--dir", type=Path, default=None, help="Directory path for batch ingestion"
    )
    ingest_parser.add_argument(
        "--pattern",
        type=str,
        default="*.pdf",
        help="File pattern for batch discovery (default: *.pdf)",
    )
    ingest_parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Search query terms for OpenAlex OA batch discovery",
    )
    ingest_parser.add_argument(
        "--download-dir",
        type=Path,
        default=None,
        help="Staging directory for downloaded OpenAlex PDFs",
    )
    ingest_parser.add_argument(
        "--limit", type=int, default=None, help="Maximum papers to ingest in batch run"
    )
    ingest_parser.add_argument(
        "--per-page",
        type=int,
        default=50,
        help="Results per OpenAlex request (default: 50)",
    )
    ingest_parser.add_argument(
        "--force", action="store_true", help="Overwrite existing documents in database"
    )

    # embed command
    embed_parser = subparsers.add_parser("embed", help="Compute dense vector embeddings for chunks")
    embed_group = embed_parser.add_mutually_exclusive_group(required=True)
    embed_group.add_argument("--citekey", type=str, help="BibTeX citation key to embed chunks for")
    embed_group.add_argument(
        "--all",
        dest="embed_all",
        action="store_true",
        help="Embed all chunks missing embeddings",
    )

    # zotero commands
    zotero_parser = subparsers.add_parser("zotero", help="Zotero synchronization commands")
    zotero_sub = zotero_parser.add_subparsers(dest="zotero_subcommand")
    watch_parser = zotero_sub.add_parser("watch", help="Watch Zotero library for new papers")
    watch_parser.add_argument(
        "--interval",
        type=float,
        default=10.0,
        help="Polling interval in seconds (default: 10.0)",
    )
    watch_parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help="Zotero data directory path",
    )

    # enrich commands
    enrich_parser = subparsers.add_parser("enrich", help="Enrich documents with external metadata")
    enrich_sub = enrich_parser.add_subparsers(dest="enrich_subcommand")
    openalex_sub = enrich_sub.add_parser("openalex", help="Enrich documents from OpenAlex")
    openalex_group = openalex_sub.add_mutually_exclusive_group(required=True)
    openalex_group.add_argument("--citekey", type=str, help="Citation key to enrich")
    openalex_group.add_argument(
        "--all",
        dest="enrich_all",
        action="store_true",
        help="Enrich all stored documents",
    )

    # migrate commands
    migrate_parser = subparsers.add_parser(
        "migrate", help="Data migration adapters for legacy schemas"
    )
    migrate_sub = migrate_parser.add_subparsers(dest="migrate_subcommand")
    legacy_sub = migrate_sub.add_parser(
        "legacy", help="Migrate research documents and pre-embedded chunks from public schema"
    )
    legacy_sub.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate migration without modifying target tables",
    )
    legacy_sub.add_argument(
        "--min-quality",
        type=int,
        default=7,
        help="Minimum quality threshold score (default: 7)",
    )
    legacy_sub.add_argument(
        "--min-relevance",
        type=int,
        default=7,
        help="Minimum relevance threshold score (default: 7)",
    )
    legacy_sub.add_argument(
        "--sources",
        nargs="+",
        default=None,
        help="Allowed source domains (e.g. arxiv fangraphs-library)",
    )
    legacy_sub.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum candidate documents to migrate",
    )

    # search command
    search_parser = subparsers.add_parser(
        "search", help="Execute hybrid dense + sparse retrieval across chunks"
    )
    search_parser.add_argument("query", type=str, help="Search query string")
    search_parser.add_argument(
        "--limit", type=int, default=5, help="Number of search hits (default: 5)"
    )
    search_parser.add_argument(
        "--citekey", type=str, default=None, help="Filter search hits by citekey"
    )

    return parser


def main(argv: Sequence[str] | None = None) -> None:
    """Main CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.subcommand == "mcp":
        if args.mcp_subcommand == "serve":
            from kb.mcp.server import mcp

            mcp.run()
        else:
            parser.parse_args(["mcp", "--help"])
    elif args.subcommand == "db":
        if args.db_subcommand == "check":
            code = asyncio.run(async_db_check())
            sys.exit(code)
        elif args.db_subcommand == "init":
            code = asyncio.run(async_db_init())
            sys.exit(code)
        else:
            parser.parse_args(["db", "--help"])
    elif args.subcommand == "ingest":
        cmd_str = str(args.pdf_path or "")
        if cmd_str == "batch" or args.dir is not None:
            batch_dir = args.dir or Path(".")
            code = asyncio.run(
                async_ingest_batch(
                    dir_path=batch_dir,
                    pattern=args.pattern,
                    limit=args.limit,
                    force=args.force,
                )
            )
            sys.exit(code)
        elif cmd_str == "search-openalex" or args.query is not None:
            query = args.query or "sabermetrics"
            code = asyncio.run(
                async_ingest_openalex(
                    query=query,
                    download_dir=args.download_dir,
                    limit=args.limit or 50,
                    per_page=args.per_page,
                    force=args.force,
                )
            )
            sys.exit(code)
        else:
            if not args.pdf_path:
                parser.parse_args(["ingest", "--help"])
            if not args.citekey:
                print(
                    "[ERROR] --citekey is required for single paper ingestion.",
                    file=sys.stderr,
                )
                sys.exit(1)
            code = asyncio.run(
                async_ingest(
                    pdf_path=args.pdf_path,
                    citekey=args.citekey,
                    title=args.title,
                    authors=args.authors,
                    year=args.year,
                )
            )
            sys.exit(code)
    elif args.subcommand == "embed":
        code = asyncio.run(
            async_embed(
                citekey=args.citekey,
                embed_all=args.embed_all,
            )
        )
        sys.exit(code)
    elif args.subcommand == "zotero":
        if args.zotero_subcommand == "watch":
            from kb.zotero.watcher import ZoteroWatcher

            watcher = ZoteroWatcher(data_dir=args.data_dir, poll_interval=args.interval)
            try:
                asyncio.run(watcher.watch())
            except KeyboardInterrupt:
                print("\n[INFO] Zotero watcher stopped by user.")
                sys.exit(0)
        else:
            parser.parse_args(["zotero", "--help"])
    elif args.subcommand == "enrich":
        if args.enrich_subcommand == "openalex":
            code = asyncio.run(
                async_enrich_openalex(
                    citekey=args.citekey,
                    enrich_all=args.enrich_all,
                )
            )
            sys.exit(code)
        else:
            parser.parse_args(["enrich", "--help"])
    elif args.subcommand == "migrate":
        if args.migrate_subcommand == "legacy":
            code = asyncio.run(
                async_migrate_legacy(
                    dry_run=args.dry_run,
                    min_quality=args.min_quality,
                    min_relevance=args.min_relevance,
                    sources=args.sources,
                    limit=args.limit,
                )
            )
            sys.exit(code)
        else:
            parser.parse_args(["migrate", "--help"])
    elif args.subcommand == "search":
        code = asyncio.run(
            async_search(
                query=args.query,
                limit=args.limit,
                citekey=args.citekey,
            )
        )
        sys.exit(code)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
