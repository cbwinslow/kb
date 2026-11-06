"""Deep corpus audit script inspecting documents, topics, formulas, and sampling quality."""

from __future__ import annotations

import asyncio
import sys

from sqlalchemy import func, or_, select

from kb.storage.database import DatabaseManager
from kb.storage.models import Chunk, CitationLink, Document, Figure, Formula

sys.stdout.reconfigure(encoding="utf-8")


async def main() -> None:
    db = DatabaseManager()
    async with db.get_session() as session:
        doc_count = await session.scalar(select(func.count(Document.id)))
        chunk_count = await session.scalar(select(func.count(Chunk.id)))
        formula_count = await session.scalar(select(func.count(Formula.id)))
        figure_count = await session.scalar(select(func.count(Figure.id)))
        citation_count = await session.scalar(select(func.count(CitationLink.id)))

        status_res = await session.execute(
            select(Formula.validation_status, func.count(Formula.id)).group_by(Formula.validation_status)
        )
        status_dist = dict(status_res.all())

        print("==================================================")
        print("                 CORPUS TOTALS                    ")
        print("==================================================")
        print(f"Total Documents:     {doc_count}")
        print(f"Total Chunks:        {chunk_count}")
        print(f"Total Formulas:      {formula_count}")
        print(f"Total Figures:       {figure_count}")
        print(f"Total Citations:     {citation_count}")
        print(f"Status Distribution: {status_dist}")

        # List all documents with citekey, title, year
        print("\n==================================================")
        print("             ALL INGESTED DOCUMENTS               ")
        print("==================================================")
        docs_res = await session.execute(
            select(Document.citekey, Document.title, Document.year, Document.authors).order_by(Document.year.desc().nullslast())
        )
        all_docs = docs_res.all()
        for idx, (citekey, title, year, authors) in enumerate(all_docs, 1):
            auth_str = ", ".join(authors[:2]) if authors else "Unknown"
            print(f"[{idx:2d}] {citekey} ({year or 'N/A'}): {title[:70]}... [by {auth_str}]")

        # Search for key techniques across documents and chunks
        keywords = [
            "pecota", "zips", "marcel", "projection", "aging", "similarity",
            "markov", "run expectancy", "re24", "win probability", "wpa",
            "pythagorean", "log5", "statcast", "physics", "trajectory",
            "neural", "machine learning", "xgboost", "random forest", "clustering"
        ]
        print("\n==================================================")
        print("          KEYWORD & TOPIC COVERAGE                ")
        print("==================================================")
        for kw in keywords:
            stmt_doc = select(func.count(Document.id)).where(
                or_(
                    Document.title.ilike(f"%{kw}%"),
                    Document.abstract.ilike(f"%{kw}%")
                )
            )
            count_doc = await session.scalar(stmt_doc)
            stmt_chunk = select(func.count(Chunk.id)).where(Chunk.raw_text.ilike(f"%{kw}%"))
            count_chunk = await session.scalar(stmt_chunk)
            print(f"{kw:20s} -> Docs (title/abstract): {count_doc:2d} | Full-text chunks: {count_chunk:4d}")

        # Detailed search for PECOTA, ZiPS, Marcel
        print("\n==================================================")
        print("       IN-DEPTH PROJECTION SEARCH (PECOTA/ZiPS)   ")
        print("==================================================")
        for proj_term in ["pecota", "zips", "marcel", "markov", "projection"]:
            matches = await session.execute(
                select(Document.citekey, Document.title, Chunk.raw_text)
                .join(Chunk, Chunk.document_id == Document.id)
                .where(Chunk.raw_text.ilike(f"%{proj_term}%"))
                .limit(3)
            )
            rows = matches.all()
            print(f"\nMatches for '{proj_term}' ({len(rows)} samples):")
            for citekey, title, full_content in rows:
                snip = full_content.replace('\n', ' ').strip()[:160]
                print(f"  - [{citekey}] {title[:40]}: {snip}...")

        # Sample formulas across validation status
        print("\n==================================================")
        print("           FORMULA QUALITY SAMPLES                ")
        print("==================================================")
        for status in ["verified", "provisional", "degraded", "failed"]:
            formulas_res = await session.execute(
                select(Formula.id, Formula.citekey, Formula.raw_latex, Formula.sanitized_latex, Formula.sympy_repr, Formula.validation_score, Formula.validation_details)
                .where(Formula.validation_status == status)
                .limit(3)
            )
            f_rows = formulas_res.all()
            print(f"\n--- Status: {status} (Total: {status_dist.get(status, 0)}) ---")
            for fid, fcitekey, fraw, fsan, fsympy, fscore, fdetails in f_rows:
                grade = fdetails.get("grade", "N/A") if fdetails else "N/A"
                print(f"ID {fid[:8]}.. | Paper: {fcitekey} | Grade: {grade} | Score: {fscore}")
                print(f"  Raw:       {fraw[:80]}")
                print(f"  Sanitized: {fsan[:80]}")
                print(f"  SymPy:     {str(fsympy)[:80]}")
                if fdetails:
                    tiers = fdetails.get("tier_scores", {})
                    checks = fdetails.get("checks_passed", [])
                    print(f"  Tiers: {tiers} | Checks: {checks[:3]}")

asyncio.run(main())
