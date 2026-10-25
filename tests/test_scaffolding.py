"""Basic scaffolding test for kb package."""

import kb
import kb.ingest
import kb.math
import kb.mcp
import kb.storage
import kb.zotero


def test_package_imports() -> None:
    assert kb is not None
    assert kb.ingest is not None
    assert kb.math is not None
    assert kb.storage is not None
    assert kb.mcp is not None
    assert kb.zotero is not None
