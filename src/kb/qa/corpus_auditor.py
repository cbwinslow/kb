"""Corpus relational integrity and quality invariant auditor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import func, select

from kb.storage.database import DatabaseManager
from kb.storage.models import BenchmarkTable, Chunk, Document, Figure, Formula


@dataclass
class CorpusAuditReport:
    """Detailed health and integrity metrics for the literature corpus."""

    total_documents: int = 0
    total_chunks: int = 0
    total_formulas: int = 0
    total_figures: int = 0
    total_benchmark_tables: int = 0
    orphaned_chunks: int = 0
    orphaned_formulas: int = 0
    unvalidated_formulas: int = 0
    verified_formulas: int = 0
    provisional_formulas: int = 0
    degraded_formulas: int = 0
    failed_formulas: int = 0
    is_healthy: bool = True
    violations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Converts report to dictionary representation."""
        return {
            "total_documents": self.total_documents,
            "total_chunks": self.total_chunks,
            "total_formulas": self.total_formulas,
            "total_figures": self.total_figures,
            "total_benchmark_tables": self.total_benchmark_tables,
            "orphaned_chunks": self.orphaned_chunks,
            "orphaned_formulas": self.orphaned_formulas,
            "unvalidated_formulas": self.unvalidated_formulas,
            "verified_formulas": self.verified_formulas,
            "provisional_formulas": self.provisional_formulas,
            "degraded_formulas": self.degraded_formulas,
            "failed_formulas": self.failed_formulas,
            "is_healthy": self.is_healthy,
            "violations": self.violations,
        }


class CorpusAuditor:
    """Performs integrity checks and health scoring across the knowledge base."""

    def __init__(self, db_manager: DatabaseManager) -> None:
        """Initializes the CorpusAuditor with a database manager."""
        self.db = db_manager

    async def run_audit(self) -> CorpusAuditReport:
        """Executes a full corpus relational integrity and quality audit."""
        report = CorpusAuditReport()

        async with self.db.get_session() as session:
            # 1. Total counts
            report.total_documents = (
                await session.execute(select(func.count(Document.id)))
            ).scalar() or 0
            report.total_chunks = (
                await session.execute(select(func.count(Chunk.id)))
            ).scalar() or 0
            report.total_formulas = (
                await session.execute(select(func.count(Formula.id)))
            ).scalar() or 0
            report.total_figures = (
                await session.execute(select(func.count(Figure.id)))
            ).scalar() or 0
            report.total_benchmark_tables = (
                await session.execute(select(func.count(BenchmarkTable.id)))
            ).scalar() or 0

            # 2. Relational integrity (orphans)
            doc_ids_subquery = select(Document.id)
            orphaned_chunks_stmt = select(func.count(Chunk.id)).where(
                ~Chunk.document_id.in_(doc_ids_subquery)
            )
            report.orphaned_chunks = (await session.execute(orphaned_chunks_stmt)).scalar() or 0

            orphaned_formulas_stmt = select(func.count(Formula.id)).where(
                ~Formula.document_id.in_(doc_ids_subquery)
            )
            report.orphaned_formulas = (await session.execute(orphaned_formulas_stmt)).scalar() or 0

            # 3. Quality status breakdown
            status_stmt = select(
                Formula.validation_status, func.count(Formula.id)
            ).group_by(Formula.validation_status)
            status_rows = (await session.execute(status_stmt)).all()
            for status, count in status_rows:
                if status == "verified":
                    report.verified_formulas = count
                elif status == "provisional":
                    report.provisional_formulas = count
                elif status == "degraded":
                    report.degraded_formulas = count
                elif status == "failed":
                    report.failed_formulas = count
                elif status is None:
                    report.unvalidated_formulas = count

            # 4. Formulate violations
            if report.orphaned_chunks > 0:
                report.violations.append(f"Detected {report.orphaned_chunks} orphaned chunks.")
            if report.orphaned_formulas > 0:
                report.violations.append(f"Detected {report.orphaned_formulas} orphaned formulas.")
            if report.failed_formulas > 0:
                report.violations.append(f"Detected {report.failed_formulas} failed formulas requiring repair.")
            if report.unvalidated_formulas > 0:
                report.violations.append(
                    f"Found {report.unvalidated_formulas} unvalidated formulas awaiting QualityGate scoring."
                )

            report.is_healthy = report.orphaned_chunks == 0 and report.orphaned_formulas == 0

        return report
