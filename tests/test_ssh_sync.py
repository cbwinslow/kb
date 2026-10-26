"""Unit tests for SSHSyncManager with mocked paramiko transport."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

from kb.config import Settings
from kb.sync.ssh import SSHSyncManager


def test_ssh_sync_unconfigured() -> None:
    config = Settings(ssh_host=None, ssh_user=None)
    mgr = SSHSyncManager(config=config)
    assert not mgr.is_configured
    ok, msg = mgr.test_connection()
    assert not ok
    assert "not configured" in msg


def test_ssh_sync_configured(tmp_path: Path) -> None:
    key_file = tmp_path / "fake_key"
    key_file.write_text("fake_ssh_key")

    config = Settings(
        ssh_host="test_host",
        ssh_user="test_user",
        ssh_key_path=key_file,
    )
    mgr = SSHSyncManager(config=config)
    assert mgr.is_configured

    mock_client = MagicMock()
    mock_sftp = MagicMock()
    mock_client.open_sftp.return_value = mock_sftp

    with patch.object(mgr, "_create_client", return_value=mock_client):
        ok, msg = mgr.test_connection()
        assert ok
        assert "connected" in msg

        # Test upload_file
        local_file = tmp_path / "test.txt"
        local_file.write_text("sample content")
        res = mgr.upload_file(local_file, "/remote/path/test.txt")
        assert res
        mock_sftp.put.assert_called_once_with(str(local_file), "/remote/path/test.txt")
