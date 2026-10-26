# Proposal: Standalone Formula Library, Dynamic MCP Execution, and SSH Homelab Sync

## Problem Statement
The scientific knowledge base extracted thousands of mathematical formulas, but they remained locked inside PostgreSQL without a portable, zero-dependency distribution format. Furthermore, AI agents connected via FastMCP could only view static formula strings rather than compiling or executing them on demand. Additionally, local workstation disk space was constrained by large PDF downloads that should reside in the 24/7 homelab vault.

## Proposed Solution
1. **Standalone Formula Package (`kb-formulas`)**:
   - Create a code generator compiling all valid formulas into typed Python functions and Polars column expressions.
   - Package as an installable zero-dependency wheel (`kb_formulas-0.1.0-py3-none-any.whl`) under `packages/kb_formulas`.
2. **FastMCP Dynamic Execution**:
   - Add `kb_compile_formula` (dynamic AST compilation to Python & Polars).
   - Add `kb_execute_formula` (dynamic calculation given parameter dict).
3. **SSH Storage Sync**:
   - Safely stream PDFs to `/home/cbwinslow/workspace/kb/pdfs` on homelab (`cbwdellr720`) via paramiko/SSH.
   - Clean up local PDF files to maintain $\ge 1.5$ GB disk space on workstation `cbwwin`.
