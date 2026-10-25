# Tasks: Legacy Knowledge Base Migration

## 1. Migration Adapter Implementation

- [x] 1.1 Implement `LegacyMigrationAdapter` in `src/kb/storage/legacy_adapter.py` with candidate scanning, quality filtering, citekey synthesis, direct vector mapping, and formula sanitization. Verify with unit test imports.
- [x] 1.2 Implement `tests/test_migration.py` covering candidate scanning, citekey generation, vector copying, and formula handling with hermetic SQLite tests. Verify with `uv run pytest tests/test_migration.py`.

## 2. CLI Integration and Safety Controls

- [x] 2.1 Add `kb migrate legacy` CLI subcommand in `src/kb/cli.py` supporting `--dry-run`, `--min-quality`, `--min-relevance`, `--sources`, and `--limit`. Verify command help and argument parsing with `uv run kb migrate legacy --help`.
- [x] 2.2 Add CLI invocation test in `tests/test_migration.py` verifying dry-run reporting without modifying database state. Verify with `uv run pytest tests/test_migration.py`.

## 3. Live Verification and Validation

- [x] 3.1 Execute dry-run against homelab database (`cbwdellr720`) with `uv run kb migrate legacy --dry-run` and verify candidate summary output.
- [x] 3.2 Execute test batch migration with `uv run kb migrate legacy --limit 10` and verify database records in `kb_documents`, `kb_chunks`, and `kb_formulas` with non-null embeddings.
- [x] 3.3 Verify hybrid search retrieval operates smoothly across migrated records with `uv run kb search "run expectancy"`.
- [x] 3.4 Run linters, type checks, and complete test suite: `uv run ruff check .`, `uv run pyright`, and `uv run pytest -m "not slow"`.

## Workflow follow-up

- Archive the change after review requirements are satisfied.
- Commit changes to git tracking.
