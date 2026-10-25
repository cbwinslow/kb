"""Unit tests for tabular data extraction and Parquet/CSV benchmark fixture export."""

from pathlib import Path

import polars as pl
import pyarrow.parquet as pq
import pytest
from docling_core.types.doc.document import DoclingDocument
from docling_core.types.doc.items.table.table_data import TableCell, TableData
from docling_core.types.doc.labels import DocItemLabel

from kb.ingest.tables import TableExtractor


@pytest.fixture
def table_extractor() -> TableExtractor:
    return TableExtractor()


SAMPLE_RUN_EXPECTANCY_MD = """
### Table 1: Run Expectancy by Base/Out State (Tango et al.)

| Base State | Outs | Run Expectancy | Probability Score |
| :--- | :--- | :--- | :--- |
| Empty | 0 | 0.481 | 0.272 |
| 1B | 0 | 0.859 | 0.416 |
| 2B | 0 | 1.100 | 0.614 |
| 3B | 0 | 1.350 | 0.820 |
| 1B_2B | 1 | 0.884 | 0.429 |
| Loaded | 2 | 0.748 | 0.320 |
"""


def test_table_extractor_from_markdown(table_extractor: TableExtractor) -> None:
    tables = table_extractor.extract_from_markdown(
        SAMPLE_RUN_EXPECTANCY_MD,
        citekey="tango2006thebook",
        document_id="doc_thebook",
    )
    assert len(tables) == 1
    table = tables[0]

    assert table.citekey == "tango2006thebook"
    assert table.num_rows == 6
    assert table.num_cols == 4
    assert "Base State" in table.column_names
    assert "Run Expectancy" in table.column_names

    # Convert to Polars DataFrame
    pldf = table.to_polars()
    assert isinstance(pldf, pl.DataFrame)
    assert pldf.shape == (6, 4)

    # Verify type inference: Outs is int, Run Expectancy is float
    assert pldf["Outs"].dtype in (pl.Int64, pl.Int32)
    assert pldf["Run Expectancy"].dtype in (pl.Float64, pl.Float32)
    assert pldf["Run Expectancy"][0] == 0.481


def test_table_export_parquet_and_csv_fixtures(
    table_extractor: TableExtractor, tmp_path: Path
) -> None:
    tables = table_extractor.extract_from_markdown(
        SAMPLE_RUN_EXPECTANCY_MD,
        citekey="tango2006thebook",
        document_id="doc_thebook",
    )
    assert len(tables) == 1
    written = table_extractor.export_all_fixtures(tables, output_dir=tmp_path)
    assert len(written) == 1
    pq_path, csv_path = written[0]

    # 1. Verify files exist on disk with citekey prefix
    assert pq_path.exists()
    assert csv_path.exists()
    assert "tango2006thebook" in pq_path.name
    assert pq_path.suffix == ".parquet"
    assert csv_path.suffix == ".csv"

    # 2. Reload Parquet file and verify integrity
    reloaded_arrow = pq.read_table(pq_path)
    assert reloaded_arrow.num_rows == 6
    assert reloaded_arrow.num_columns == 4

    # 3. Reload into Polars and verify exact values
    reloaded_polars = pl.read_parquet(pq_path)
    assert reloaded_polars.shape == (6, 4)
    assert reloaded_polars["Base State"].to_list() == [
        "Empty",
        "1B",
        "2B",
        "3B",
        "1B_2B",
        "Loaded",
    ]
    assert reloaded_polars["Run Expectancy"][2] == 1.100


def test_table_extractor_from_docling_document(table_extractor: TableExtractor) -> None:
    doc = DoclingDocument(name="synthetic_tabular_paper")
    doc.add_text(label=DocItemLabel.SECTION_HEADER, text="Empirical Results")

    # Add a 2x2 table to Docling Document
    table_data = TableData(num_rows=2, num_cols=2)
    table_data.table_cells = [
        TableCell(
            text="Metric",
            row_span=1,
            col_span=1,
            start_row_offset_idx=0,
            end_row_offset_idx=1,
            start_col_offset_idx=0,
            end_col_offset_idx=1,
        ),
        TableCell(
            text="RMSE",
            row_span=1,
            col_span=1,
            start_row_offset_idx=0,
            end_row_offset_idx=1,
            start_col_offset_idx=1,
            end_col_offset_idx=2,
        ),
        TableCell(
            text="Pythagorean_1.83",
            row_span=1,
            col_span=1,
            start_row_offset_idx=1,
            end_row_offset_idx=2,
            start_col_offset_idx=0,
            end_col_offset_idx=1,
        ),
        TableCell(
            text="0.024",
            row_span=1,
            col_span=1,
            start_row_offset_idx=1,
            end_row_offset_idx=2,
            start_col_offset_idx=1,
            end_col_offset_idx=2,
        ),
    ]
    doc.add_table(data=table_data)

    tables = table_extractor.extract_from_docling_document(doc, citekey="miller2008benchmark")
    assert len(tables) >= 1
    tbl = tables[0]
    assert tbl.citekey == "miller2008benchmark"
    assert tbl.num_rows > 0
