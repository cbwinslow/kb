# AGENTS.md — Development & Architecture Guidelines for kb

## 1. Mandatory OpenSpec Discipline
- **Every major feature, architectural evolution, or tooling addition MUST use OpenSpec.**
- Before implementing substantial functionality:
  1. Create or update an OpenSpec change folder under `openspec/changes/<change-id>/` containing `proposal.md`, `design.md`, `tasks.md`, and delta specs under `specs/`.
  2. Implement tasks step-by-step with continuous test-driven verification.
  3. Keep `openspec/specs/` and project documentation in sync.
  4. Archive completed changes cleanly under `openspec/changes/archive/`.
- Never bypass documentation or spec creation.

## 2. Comprehensive Documentation Standards
- **Maintain Documentation Integrity**: Preserve all existing docstrings and comments.
- **Strict Typing & Docstrings**: Every module, class, method, function, and CLI command must include standard Google or Sphinx-style docstrings and explicit type hints (`from __future__ import annotations`).
- Keep `README.md`, `openspec/project.md`, and any user-facing dashboards updated whenever capabilities expand.

## 3. Infrastructure & Portability Rules
- **Domain-Agnostic & Portable**: The core engine must be portable across machines (Windows, Linux, macOS).
- **Zero Hardcoded Paths & Secrets**: Never hardcode hostnames, IPs, absolute paths, database passwords, or API keys in source code. All configuration must resolve via Pydantic `Settings` (`kb.config.settings`) backed by `.env`.
- **Homelab Storage Preservation**: Original PDFs, large binaries, and long-term artifacts are persisted to the homelab vault via SSH/SFTP (`kb.sync.ssh.SSHStorageSync`). Local temporary files on workstation `cbwwin` must be cleaned up to protect local disk space ($\ge 1.5$ GB free minimum).
- **No Samba Dependency**: Use direct SSH / SFTP protocols for remote file transfers.
- **Compute Isolation**: Run compute-heavy ingestion (Docling OCR, BGE-M3 embedding generation) on GPU worker (`cbwwin`) while utilizing PostgreSQL 16 on the homelab (`cbwdellr720`).

## 4. Verification & Quality Gates
- Every pull request or goal execution must pass:
  1. `uv run ruff check src/ tests/ scripts/ packages/`
  2. `uv run pyright src/ tests/ packages/`
  3. `uv run pytest tests/`
- Formula code generation must strictly validate symbolic ASTs and preserve numerical accuracy.
