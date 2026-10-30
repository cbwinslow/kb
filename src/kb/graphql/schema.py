"""Multi-layer mathematical knowledge graph and GraphQL API schema."""

from __future__ import annotations

import logging

import strawberry
from sqlalchemy import func, select

from kb.codegen.compiler import FormulaCompiler
from kb.math.chaining import FormulaChainingEngine
from kb.math.ontology import get_symbol_ontology
from kb.storage.database import DatabaseManager
from kb.storage.models import BenchmarkTable, Document, Figure, Formula

logger = logging.getLogger(__name__)


@strawberry.type
class FormulaType:
    id: str
    citekey: str
    latex: str
    lhs: str | None
    rhs: str | None
    symbols: list[str]
    is_valid: bool
    is_equality: bool
    python_code: str | None = None
    polars_code: str | None = None
    document_title: str | None = None
    validation_score: float | None = None
    validation_status: str | None = None
    letter_grade: str | None = None


@strawberry.type
class ValidationCheckType:
    name: str
    tier: str
    passed: bool
    score: float
    max_score: float
    message: str


@strawberry.type
class ValidationScorecardType:
    formula_id: str
    citekey: str
    total_score: float
    letter_grade: str
    status: str
    is_valid: bool
    tier_scores_json: str
    checks: list[ValidationCheckType]
    recommendations: list[str]


@strawberry.type
class VariableType:
    name: str
    canonical_concept: str | None
    defining_formula_ids: list[str]
    using_formula_ids: list[str]


@strawberry.type
class ConceptType:
    name: str
    latex_repr: str
    description: str
    aliases: list[str]
    formula_count: int


@strawberry.type
class FigureType:
    id: str
    document_id: str
    citekey: str
    caption: str | None
    figure_index: int
    image_path: str | None


@strawberry.type
class DocumentType:
    id: str
    citekey: str
    title: str
    year: int | None
    doi: str | None
    authors: list[str]
    formula_count: int
    table_count: int
    citation_count: int = 0
    incoming_citation_count: int = 0
    outgoing_citation_count: int = 0
    figures: list[FigureType] = strawberry.field(default_factory=list)


@strawberry.type
class BenchmarkTableType:
    id: str
    citekey: str
    caption: str | None
    num_rows: int
    num_cols: int
    columns: list[str]
    parquet_path: str | None


@strawberry.type
class SubstitutionStepType:
    target_variable: str
    source_formula_id: str
    source_citekey: str
    original_expr: str
    substituted_expr: str
    dimensional_valid: bool = True
    dimensional_note: str = ""


@strawberry.type
class DerivationChainType:
    target_id: str
    target_citekey: str
    closed_form_latex: str
    primitive_symbols: list[str]
    steps: list[SubstitutionStepType]
    python_code: str | None
    polars_code: str | None
    is_dimensionally_valid: bool = True


@strawberry.type
class MultiHopChainType:
    from_concept: str
    to_concept: str
    target_id: str
    target_citekey: str
    formula_path: list[str]
    citekey_path: list[str]
    closed_form_latex: str
    primitive_symbols: list[str]
    is_dimensionally_valid: bool
    steps: list[SubstitutionStepType]
    python_code: str | None
    polars_code: str | None


@strawberry.type
class GraphNodeType:
    id: str
    label: str
    layer: str  # document, formula, variable, concept, table
    metadata: str


@strawberry.type
class GraphEdgeType:
    source: str
    target: str
    relation: str


@strawberry.type
class FormulaCoverageType:
    total_formulas: int
    valid_formulas: int
    invalid_formulas: int
    equality_formulas: int
    parse_yield_pct: float
    equality_yield_pct: float
    unique_symbols_count: int
    defined_symbols_count: int
    consumed_symbols_count: int
    ontology_mapped_symbols_count: int
    orphan_symbols_count: int
    top_orphan_symbols: list[str]
    top_characters: list[str]
    top_errors: list[str]


@strawberry.type
class KnowledgeGraphType:
    nodes: list[GraphNodeType]
    edges: list[GraphEdgeType]


@strawberry.type
class Query:
    @strawberry.field
    async def formula_coverage(
        self,
        limit: int | None = None,
    ) -> FormulaCoverageType:
        """Query formula parsing yield, symbol utilization, and non-ASCII coverage."""
        from kb.math.coverage import FormulaCoverageAnalyzer

        analyzer = FormulaCoverageAnalyzer()
        report = await analyzer.analyze_corpus(limit=limit)
        return FormulaCoverageType(
            total_formulas=report.total_formulas,
            valid_formulas=report.valid_formulas,
            invalid_formulas=report.invalid_formulas,
            equality_formulas=report.equality_formulas,
            parse_yield_pct=report.parse_yield_pct,
            equality_yield_pct=report.equality_yield_pct,
            unique_symbols_count=len(report.unique_symbols),
            defined_symbols_count=len(report.defined_symbols),
            consumed_symbols_count=len(report.consumed_symbols),
            ontology_mapped_symbols_count=len(report.ontology_mapped_symbols),
            orphan_symbols_count=len(report.orphan_symbols),
            top_orphan_symbols=report.orphan_symbols[:20],
            top_characters=[f"{k}: {v}" for k, v in list(report.character_accounting.items())[:15]],
            top_errors=[f"{k}: {v}" for k, v in list(report.error_taxonomy.items())[:10]],
        )

    @strawberry.field
    async def formulas(
        self,
        citekey: str | None = None,
        is_valid: bool | None = None,
        limit: int = 50,
    ) -> list[FormulaType]:
        """Query mathematical formulas with optional filters."""
        db = DatabaseManager()
        compiler = FormulaCompiler()
        async with db.get_session() as session:
            stmt = select(Formula, Document.title).outerjoin(
                Document, Formula.document_id == Document.id
            )
            if citekey:
                stmt = stmt.where(Formula.citekey == citekey)
            if is_valid is not None:
                stmt = stmt.where(Formula.is_valid.is_(is_valid))
            stmt = stmt.limit(limit)

            rows = (await session.execute(stmt)).all()
            results: list[FormulaType] = []
            for f, doc_title in rows:
                py_code = None
                pl_code = None
                if f.is_valid and f.is_equality and f.lhs and f.rhs:
                    comp = compiler.compile(
                        formula_id=f.id,
                        citekey=f.citekey,
                        raw_latex=f.sanitized_latex or f.raw_latex,
                        sympy_repr=f.sympy_repr,
                    )
                    py_code = comp.python_source
                    pl_code = comp.polars_expression

                results.append(
                    FormulaType(
                        id=f.id,
                        citekey=f.citekey,
                        latex=f.raw_latex,
                        lhs=f.lhs,
                        rhs=f.rhs,
                        symbols=f.symbols or [],
                        is_valid=f.is_valid,
                        is_equality=f.is_equality,
                        python_code=py_code,
                        polars_code=pl_code,
                        document_title=doc_title,
                        validation_score=f.validation_score,
                        validation_status=f.validation_status,
                        letter_grade="A"
                        if (f.validation_score or 0) >= 88
                        else "B"
                        if (f.validation_score or 0) >= 75
                        else "C"
                        if (f.validation_score or 0) >= 60
                        else "D"
                        if (f.validation_score or 0) >= 45
                        else "F"
                        if f.validation_score is not None
                        else None,
                    )
                )
            return results

    @strawberry.field
    async def formula(self, id: str) -> FormulaType | None:
        """Retrieve an individual formula by its unique ID."""
        db = DatabaseManager()
        compiler = FormulaCompiler()
        async with db.get_session() as session:
            stmt = (
                select(Formula, Document.title)
                .outerjoin(Document, Formula.document_id == Document.id)
                .where(Formula.id == id)
            )
            row = (await session.execute(stmt)).first()
            if not row:
                return None
            f, doc_title = row
            py_code = None
            pl_code = None
            if f.is_valid and f.is_equality and f.lhs and f.rhs:
                comp = compiler.compile(
                    formula_id=f.id,
                    citekey=f.citekey,
                    raw_latex=f.sanitized_latex or f.raw_latex,
                    sympy_repr=f.sympy_repr,
                )
                py_code = comp.python_source
                pl_code = comp.polars_expression

            return FormulaType(
                id=f.id,
                citekey=f.citekey,
                latex=f.raw_latex,
                lhs=f.lhs,
                rhs=f.rhs,
                symbols=f.symbols or [],
                is_valid=f.is_valid,
                is_equality=f.is_equality,
                python_code=py_code,
                polars_code=pl_code,
                document_title=doc_title,
                validation_score=f.validation_score,
                validation_status=f.validation_status,
                letter_grade="A"
                if (f.validation_score or 0) >= 88
                else "B"
                if (f.validation_score or 0) >= 75
                else "C"
                if (f.validation_score or 0) >= 60
                else "D"
                if (f.validation_score or 0) >= 45
                else "F"
                if f.validation_score is not None
                else None,
            )

    @strawberry.field
    async def concepts(self) -> list[ConceptType]:
        """Query canonical concepts from the symbol ontology."""
        ontology = get_symbol_ontology()
        db = DatabaseManager()
        results: list[ConceptType] = []

        async with db.get_session() as session:
            for c_id, c_def in ontology.concepts.items():
                concept_name = c_id.value if hasattr(c_id, "value") else str(c_id)
                # Count formulas mentioning this concept's symbols/aliases
                aliases = [concept_name] + c_def.aliases
                count_stmt = (
                    select(func.count(Formula.id))
                    .where(Formula.is_valid.is_(True))
                    .where(Formula.lhs.in_(aliases))
                )
                cnt = (await session.execute(count_stmt)).scalar_one()

                results.append(
                    ConceptType(
                        name=concept_name,
                        latex_repr=c_def.latex_repr,
                        description=c_def.description,
                        aliases=c_def.aliases,
                        formula_count=cnt,
                    )
                )
        return results

    @strawberry.field
    async def documents(self, limit: int = 50) -> list[DocumentType]:
        """Query documents with counts of associated formulas and benchmark tables."""
        db = DatabaseManager()
        async with db.get_session() as session:
            stmt = select(Document).limit(limit)
            docs = (await session.execute(stmt)).scalars().all()

            results: list[DocumentType] = []
            for d in docs:
                f_cnt = (
                    await session.execute(
                        select(func.count(Formula.id)).where(Formula.document_id == d.id)
                    )
                ).scalar_one()
                t_cnt = (
                    await session.execute(
                        select(func.count(BenchmarkTable.id)).where(
                            BenchmarkTable.document_id == d.id
                        )
                    )
                ).scalar_one()

                fig_stmt = (
                    select(Figure)
                    .where(Figure.document_id == d.id)
                    .order_by(Figure.figure_index.asc())
                )
                fig_rows = (await session.execute(fig_stmt)).scalars().all()
                doc_figs = [
                    FigureType(
                        id=f.id,
                        document_id=f.document_id,
                        citekey=f.citekey,
                        caption=f.caption,
                        figure_index=f.figure_index,
                        image_path=f.image_path,
                    )
                    for f in fig_rows
                ]

                results.append(
                    DocumentType(
                        id=d.id,
                        citekey=d.citekey,
                        title=d.title,
                        year=d.year,
                        doi=d.doi,
                        authors=d.authors or [],
                        formula_count=f_cnt,
                        table_count=t_cnt,
                        citation_count=d.citation_count or 0,
                        incoming_citation_count=len(d.incoming_citations)
                        if hasattr(d, "incoming_citations")
                        else 0,
                        outgoing_citation_count=len(d.outgoing_citations)
                        if hasattr(d, "outgoing_citations")
                        else 0,
                        figures=doc_figs,
                    )
                )
            return results

    @strawberry.field
    async def chain_formula(
        self,
        target_id: str,
        max_depth: int = 5,
    ) -> DerivationChainType | None:
        """Recursively chain and substitute component equations into target formula."""
        engine = FormulaChainingEngine()
        try:
            res = await engine.chain_formula(formula_id=target_id, max_depth=max_depth)
            steps = [
                SubstitutionStepType(
                    target_variable=s.target_variable,
                    source_formula_id=s.source_formula_id,
                    source_citekey=s.source_citekey,
                    original_expr=s.original_expr_str,
                    substituted_expr=s.substituted_expr_str,
                    dimensional_valid=s.dimensional_valid,
                    dimensional_note=s.dimensional_note,
                )
                for s in res.trace_steps
            ]
            return DerivationChainType(
                target_id=res.target_formula_id,
                target_citekey=res.target_citekey,
                closed_form_latex=res.closed_form_latex,
                primitive_symbols=res.primitive_symbols,
                steps=steps,
                python_code=res.python_code,
                polars_code=res.polars_code,
                is_dimensionally_valid=res.is_dimensionally_valid,
            )
        except Exception as e:
            logger.error("Failed to chain formula %s: %s", target_id, e)
            return None

    @strawberry.field
    async def equation_chain(
        self,
        from_concept: str,
        to_concept: str,
        max_depth: int = 5,
    ) -> MultiHopChainType | None:
        """Query multi-hop derivation chain connecting a source concept to a target concept."""
        engine = FormulaChainingEngine()
        try:
            res = await engine.chain_between(
                from_concept=from_concept,
                to_concept=to_concept,
                max_depth=max_depth,
            )
            steps = [
                SubstitutionStepType(
                    target_variable=s.target_variable,
                    source_formula_id=s.source_formula_id,
                    source_citekey=s.source_citekey,
                    original_expr=s.original_expr_str,
                    substituted_expr=s.substituted_expr_str,
                    dimensional_valid=s.dimensional_valid,
                    dimensional_note=s.dimensional_note,
                )
                for s in res.trace_steps
            ]
            return MultiHopChainType(
                from_concept=res.from_concept,
                to_concept=res.to_concept,
                target_id=res.target_formula_id,
                target_citekey=res.target_citekey,
                formula_path=res.formula_path,
                citekey_path=res.citekey_path,
                closed_form_latex=res.closed_form_latex,
                primitive_symbols=res.primitive_symbols,
                is_dimensionally_valid=res.is_dimensionally_valid,
                steps=steps,
                python_code=res.python_code,
                polars_code=res.polars_code,
            )
        except Exception as e:
            logger.error("Failed to chain concepts %s -> %s: %s", from_concept, to_concept, e)
            return None

    @strawberry.field
    async def knowledge_graph(self, limit: int = 100) -> KnowledgeGraphType:
        """Returns multi-layer nodes and edges connecting Documents, Formulas, Variables, Concepts, and Tables."""
        db = DatabaseManager()
        ontology = get_symbol_ontology()

        nodes_dict: dict[str, GraphNodeType] = {}
        edges: list[GraphEdgeType] = []

        async with db.get_session() as session:
            # 1. Fetch valid formulas
            stmt = (
                select(Formula, Document.title)
                .outerjoin(Document, Formula.document_id == Document.id)
                .where(Formula.is_valid.is_(True))
                .order_by(Formula.id.asc())
                .limit(limit)
            )
            rows = (await session.execute(stmt)).all()

            for f, doc_title in rows:
                # Document Node
                doc_node_id = f"doc_{f.citekey}"
                if doc_node_id not in nodes_dict:
                    nodes_dict[doc_node_id] = GraphNodeType(
                        id=doc_node_id,
                        label=f.citekey,
                        layer="document",
                        metadata=doc_title or f.citekey,
                    )

                # Formula Node
                form_node_id = f"form_{f.id}"
                nodes_dict[form_node_id] = GraphNodeType(
                    id=form_node_id,
                    label=f.lhs or f.id[:10],
                    layer="formula",
                    metadata=f.raw_latex,
                )

                # Edge: Document -> Formula
                edges.append(
                    GraphEdgeType(
                        source=doc_node_id,
                        target=form_node_id,
                        relation="contains_formula",
                    )
                )

                # Variable Nodes from LHS
                if f.lhs:
                    var_node_id = f"var_{f.lhs}"
                    if var_node_id not in nodes_dict:
                        nodes_dict[var_node_id] = GraphNodeType(
                            id=var_node_id,
                            label=f.lhs,
                            layer="variable",
                            metadata=f"Defined variable {f.lhs}",
                        )
                    edges.append(
                        GraphEdgeType(
                            source=form_node_id,
                            target=var_node_id,
                            relation="defines_variable",
                        )
                    )

                    # Concept Node connection
                    canonical = ontology.resolve_canonical(f.lhs)
                    if canonical:
                        canon_str = (
                            canonical.value if hasattr(canonical, "value") else str(canonical)
                        )
                        concept_node_id = f"concept_{canon_str}"
                        if concept_node_id not in nodes_dict:
                            c_def = ontology.get_concept(canonical)
                            desc = c_def.description if c_def else canon_str
                            nodes_dict[concept_node_id] = GraphNodeType(
                                id=concept_node_id,
                                label=canon_str,
                                layer="concept",
                                metadata=desc,
                            )
                        edges.append(
                            GraphEdgeType(
                                source=var_node_id,
                                target=concept_node_id,
                                relation="maps_to_concept",
                            )
                        )

                # Symbols in RHS
                for sym in (f.symbols or [])[:5]:
                    if sym != f.lhs:
                        sym_var_id = f"var_{sym}"
                        if sym_var_id not in nodes_dict:
                            nodes_dict[sym_var_id] = GraphNodeType(
                                id=sym_var_id,
                                label=sym,
                                layer="variable",
                                metadata=f"Input parameter {sym}",
                            )
                        edges.append(
                            GraphEdgeType(
                                source=form_node_id,
                                target=sym_var_id,
                                relation="uses_parameter",
                            )
                        )

        return KnowledgeGraphType(
            nodes=list(nodes_dict.values()),
            edges=edges,
        )

    @strawberry.field
    async def validate_formula(self, id: str) -> ValidationScorecardType | None:
        """Run multi-tier validation gate on a formula and return full scorecard."""
        import json

        from kb.math.validation import FormulaQualityGate

        db = DatabaseManager()
        gate = FormulaQualityGate()
        async with db.get_session() as session:
            stmt = select(Formula).where(Formula.id == id)
            f = (await session.execute(stmt)).scalar_one_or_none()
            if not f:
                return None
            card = gate.validate_formula(f)
            # Update database record
            f.validation_score = card.total_score
            f.validation_status = card.status
            f.validation_details = card.to_dict()
            await session.commit()

            checks = [
                ValidationCheckType(
                    name=c.name,
                    tier=c.tier.value,
                    passed=c.passed,
                    score=c.score,
                    max_score=c.max_score,
                    message=c.message,
                )
                for c in card.checks
            ]
            return ValidationScorecardType(
                formula_id=card.formula_id,
                citekey=card.citekey,
                total_score=card.total_score,
                letter_grade=card.letter_grade,
                status=card.status,
                is_valid=card.is_valid,
                tier_scores_json=json.dumps(card.tier_scores),
                checks=checks,
                recommendations=card.recommendations,
            )


schema = strawberry.Schema(query=Query)
