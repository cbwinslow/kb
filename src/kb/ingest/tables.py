"""Tabular data extractor and Parquet/CSV benchmark fixture exporter."""

from __future__ import annotations

import hashlib
import logging
import re
from pathlib import Path
from typing import Any

import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.csv as pa_csv
import pyarrow.parquet as pq
from docling_core.types.doc.document import DoclingDocument
from docling_core.types.doc.items.table.table import TableItem
from pydantic import BaseModel, ConfigDict, Field

logger = logging.getLogger(__name__)

# Markdown table block regex (table header, separator row, and subsequent data rows)
MD_TABLE_BLOCK_RE = re.compile(
    r"((?:^[ \t]*\|[^\r\n]+\|[ \t]*\r?\n)"
    r"(?:^[ \t]*\|(?:[ \t]*:?-+:?[ \t]*\|)+[ \t]*\r?\n)"
    r"(?:^[ \t]*\|[^\r\n]+\|[ \t]*(?:\r?\n|$))+)",
    re.MULTILINE,
)


class ExtractedTable(BaseModel):
    """Container for extracted empirical table matrices backed by PyArrow and Polars."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    table_id: str = Field(description="Deterministic identifier for the table")
    document_id: str = Field(description="Parent document identifier")
    citekey: str = Field(default="", description="BibTeX citation key")
    table_index: int = Field(description="Sequence index of the table within document")
    caption: str = Field(default="", description="Table caption or preceding heading")
    markdown_table: str = Field(description="Raw markdown representation of the table")
    arrow_table: pa.Table = Field(description="Underlying typed PyArrow Table")
    num_rows: int = Field(description="Number of rows in the table")
    num_cols: int = Field(description="Number of columns in the table")
    column_names: list[str] = Field(description="List of column names")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Metadata dictionary")

    def to_polars(self) -> pl.DataFrame:
        """Convert PyArrow table into a typed Polars DataFrame."""
        return pl.from_arrow(self.arrow_table)  # type: ignore[return-value]

    def to_pandas(self) -> pd.DataFrame:
        """Convert PyArrow table into a Pandas DataFrame."""
        return self.arrow_table.to_pandas()

    def export_parquet(self, output_path: str | Path) -> Path:
        """Export table to an Apache Parquet file.

        Args:
            output_path: Target path for the .parquet file.

        Returns:
            Resolved Path of the written parquet file.
        """
        path = Path(output_path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        pq.write_table(self.arrow_table, path)
        logger.info("Exported Parquet fixture to %s (%d rows)", path.name, self.num_rows)
        return path

    def export_csv(self, output_path: str | Path) -> Path:
        """Export table to a CSV file.

        Args:
            output_path: Target path for the .csv file.

        Returns:
            Resolved Path of the written CSV file.
        """
        path = Path(output_path).resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        pa_csv.write_csv(self.arrow_table, path)
        logger.info("Exported CSV fixture to %s (%d rows)", path.name, self.num_rows)
        return path


class TableExtractor:
    """Extracts tables from Docling AST documents or Markdown strings into PyArrow / Polars."""

    def extract_from_docling_document(
        self,
        doc: DoclingDocument,
        citekey: str = "",
        document_id: str = "",
    ) -> list[ExtractedTable]:
        """Extract all TableItems from a DoclingDocument into ExtractedTable objects.

        Args:
            doc: Parsed DoclingDocument AST.
            citekey: BibTeX citation key.
            document_id: Parent document identifier.

        Returns:
            List of ExtractedTable instances.
        """
        if not document_id:
            raw_hash = hashlib.sha256(
                (citekey or doc.name or "untitled").encode("utf-8")
            ).hexdigest()[:12]
            document_id = f"doc_{raw_hash}"

        tables: list[ExtractedTable] = []
        table_idx = 0

        for item, _ in doc.iterate_items():
            if isinstance(item, TableItem):
                try:
                    df: pd.DataFrame = item.export_to_dataframe()
                    if df.empty:
                        continue

                    # Clean column names (strip whitespace and stringify)
                    df.columns = [str(c).strip() for c in df.columns]

                    arrow_tbl = pa.Table.from_pandas(df, preserve_index=False)
                    caption_text = self._find_caption(item)
                    md_text = (
                        item.export_to_markdown() if hasattr(item, "export_to_markdown") else ""
                    )

                    tbl_hash = hashlib.sha256(
                        f"{document_id}_{table_idx}_{arrow_tbl.num_rows}".encode()
                    ).hexdigest()[:8]
                    table_id = f"{document_id}_tbl_{table_idx:02d}_{tbl_hash}"

                    extracted = ExtractedTable(
                        table_id=table_id,
                        document_id=document_id,
                        citekey=citekey,
                        table_index=table_idx,
                        caption=caption_text,
                        markdown_table=md_text,
                        arrow_table=arrow_tbl,
                        num_rows=arrow_tbl.num_rows,
                        num_cols=arrow_tbl.num_columns,
                        column_names=arrow_tbl.column_names,
                        metadata={"origin": str(item.self_ref)},
                    )
                    tables.append(extracted)
                    table_idx += 1
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Failed to extract TableItem %s: %s", item.self_ref, exc)

        logger.info("Extracted %d tables from Docling AST for %s", len(tables), document_id)
        return tables

    def extract_from_markdown(
        self,
        markdown_text: str,
        citekey: str = "",
        document_id: str = "",
    ) -> list[ExtractedTable]:
        """Extract all markdown tables from raw text into ExtractedTable objects.

        Args:
            markdown_text: Raw Markdown text containing one or more tables.
            citekey: BibTeX citation key.
            document_id: Parent document identifier.

        Returns:
            List of ExtractedTable instances.
        """
        if not document_id:
            raw_hash = hashlib.sha256((citekey or "md_doc").encode("utf-8")).hexdigest()[:12]
            document_id = f"doc_{raw_hash}"

        tables: list[ExtractedTable] = []
        matches = list(MD_TABLE_BLOCK_RE.finditer(markdown_text))

        for idx, match in enumerate(matches):
            raw_block = match.group(0).strip()
            arrow_tbl = self._parse_markdown_table_to_arrow(raw_block)
            if arrow_tbl is None or arrow_tbl.num_rows == 0:
                continue

            tbl_hash = hashlib.sha256(raw_block.encode("utf-8")).hexdigest()[:8]
            table_id = f"{document_id}_tbl_{idx:02d}_{tbl_hash}"

            extracted = ExtractedTable(
                table_id=table_id,
                document_id=document_id,
                citekey=citekey,
                table_index=idx,
                caption="",
                markdown_table=raw_block,
                arrow_table=arrow_tbl,
                num_rows=arrow_tbl.num_rows,
                num_cols=arrow_tbl.num_columns,
                column_names=arrow_tbl.column_names,
                metadata={},
            )
            tables.append(extracted)

        return tables

    def export_all_fixtures(
        self,
        tables: list[ExtractedTable],
        output_dir: str | Path = "data/fixtures",
    ) -> list[tuple[Path, Path]]:
        """Export a collection of tables as Parquet and CSV golden fixtures.

        Args:
            tables: List of ExtractedTable instances.
            output_dir: Directory where fixtures will be written.

        Returns:
            List of (parquet_path, csv_path) tuples.
        """
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        written: list[tuple[Path, Path]] = []

        for table in tables:
            cite = table.citekey or "dataset"
            stem = f"{cite}_{table.table_id}"
            pq_file = out_path / f"{stem}.parquet"
            csv_file = out_path / f"{stem}.csv"

            table.export_parquet(pq_file)
            table.export_csv(csv_file)
            written.append((pq_file, csv_file))

        return written

    def _find_caption(self, item: TableItem) -> str:
        """Find caption text associated with a TableItem if available."""
        caption = getattr(item, "caption", None)
        if caption:
            return str(caption).strip()
        return ""

    def _parse_markdown_table_to_arrow(self, table_str: str) -> pa.Table | None:
        """Parse markdown table string into a typed PyArrow Table with type inference."""
        lines = [line.strip() for line in table_str.strip().splitlines() if line.strip()]
        if len(lines) < 3:
            return None

        # Split cells by '|'
        header_line = lines[0]
        headers = [c.strip() for c in header_line.split("|")[1:-1]]
        if not headers:
            return None

        data_rows: list[list[int | float | bool | str | None]] = []
        for line in lines[2:]:
            # Ensure line starts and ends with '|'
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) == len(headers):
                data_rows.append([self._infer_value(c) for c in cells])
            elif len(cells) > 0:
                # Pad or truncate to header count
                padded = [self._infer_value(c) for c in cells[: len(headers)]]
                while len(padded) < len(headers):
                    padded.append(None)
                data_rows.append(padded)

        if not data_rows:
            return None

        # Transpose rows to columns dict
        col_dict: dict[str, list[int | float | bool | str | None]] = {
            h: [row[i] for row in data_rows] for i, h in enumerate(headers)
        }

        try:
            pydf = pd.DataFrame(col_dict)
            return pa.Table.from_pandas(pydf, preserve_index=False)
        except Exception as exc:  # noqa: BLE001
            logger.debug("Failed converting parsed markdown table to arrow: %s", exc)
            return None

    def _infer_value(self, cell: str) -> int | float | bool | str | None:
        """Infer numeric, boolean, or string data type for table cell."""
        text = cell.strip()
        if not text or text in ("-", "—", "N/A", "null"):
            return None

        # Integer
        if re.match(r"^-?\d+$", text):
            try:
                return int(text)
            except ValueError:
                pass

        # Float
        if re.match(r"^-?\d*\.\d+$", text):
            try:
                return float(text)
            except ValueError:
                pass

        # Boolean
        if text.lower() in ("true", "yes"):
            return True
        if text.lower() in ("false", "no"):
            return False

        return text
