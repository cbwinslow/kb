# Design: Standalone Formula Library & Dynamic MCP Execution

## Architecture
- `src/kb/library/generator.py`: Traverses verified formulas, creates clean function names, docstrings with KaTeX equations, typed signatures, and builds Polars expressions.
- `packages/kb_formulas`: Independent Python package with its own `pyproject.toml` and wheel distribution.
- `src/kb/mcp/server.py`: Extends FastMCP server with `kb_compile_formula` and `kb_execute_formula`.
- `src/kb/sync/ssh.py`: Paramiko-based SFTP synchronization client respecting `Settings` for remote homelab persistence.
