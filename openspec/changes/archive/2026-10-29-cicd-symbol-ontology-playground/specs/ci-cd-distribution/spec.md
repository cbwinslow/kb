# Specification: CI/CD & PyPI Distribution

## Scope & Purpose
Defines the continuous integration and release delivery pipeline for the `kb` repository and its downstream compiled sub-package `packages/kb_formulas`.

## Requirements
1. **Multi-Platform Continuous Integration (`.github/workflows/ci.yml`)**:
   - MUST trigger on `push` and `pull_request` to `master`.
   - MUST run jobs on both `ubuntu-latest` and `windows-latest`.
   - MUST verify static linting via `ruff check` and format validation via `ruff format --check`.
   - MUST verify static type safety via `pyright` across `src/`, `tests/`, and `packages/`.
   - MUST execute the full pytest test suite with assertions on 100% pass rate.
2. **Formula Wheel & Sdist Distribution (`.github/workflows/publish-formulas.yml`)**:
   - MUST trigger on semver tag pushes (`v*.*.*`) or explicit manual dispatch.
   - MUST build standalone wheels and source tarballs for `packages/kb_formulas` using `uv build`.
   - MUST attach compiled distribution artifacts to the GitHub release.
   - MUST support PyPI deployment via PyPI token / Trusted Publishing credentials stored in GitHub repository secrets.
3. **Packaging Integrity**:
   - `packages/kb_formulas/pyproject.toml` MUST declare appropriate metadata including `name = "kb-formulas"`, versioning, dependencies (e.g. `polars`), and license.
