"""SSH and SFTP remote synchronization manager for homelab storage."""

from __future__ import annotations

import contextlib
import logging
import os
import posixpath
from pathlib import Path

import paramiko

from kb.config import Settings, settings

logger = logging.getLogger(__name__)


class SSHSyncManager:
    """Manages encrypted file archiving to remote homelab server via SSH/SFTP."""

    def __init__(self, config: Settings | None = None) -> None:
        self.config = config or settings
        self.host = self.config.ssh_host
        self.port = self.config.ssh_port
        self.user = self.config.ssh_user
        self.key_path = (
            Path(os.path.expanduser(str(self.config.ssh_key_path)))
            if self.config.ssh_key_path
            else None
        )
        self.password = self.config.ssh_password
        self.remote_pdf_dir = self.config.ssh_remote_pdf_dir
        self.remote_fixtures_dir = self.config.ssh_remote_fixtures_dir

    @property
    def is_configured(self) -> bool:
        """Returns True if minimum SSH connection credentials are provided."""
        has_host = bool(self.host and self.user)
        has_auth = bool(
            (self.key_path and self.key_path.exists()) or self.password
        )
        return has_host and has_auth

    def _create_client(self) -> paramiko.SSHClient:
        """Instantiate and authenticate a Paramiko SSHClient."""
        if not self.is_configured:
            raise ValueError(
                "SSH synchronization is not configured. Set KB_SSH_HOST, KB_SSH_USER, "
                "and KB_SSH_KEY_PATH (or KB_SSH_PASSWORD) in .env or environment."
            )

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        connect_kwargs: dict[str, object] = {
            "hostname": self.host,
            "port": self.port,
            "username": self.user,
            "allow_agent": False,
            "timeout": 10.0,
        }

        if self.key_path and self.key_path.exists():
            connect_kwargs["key_filename"] = str(self.key_path)
        elif self.password:
            connect_kwargs["password"] = self.password

        client.connect(**connect_kwargs)  # type: ignore[arg-type]
        return client

    def test_connection(self) -> tuple[bool, str]:
        """Verify SSH and SFTP handshake and directory writability."""
        if not self.is_configured:
            return False, "SSH is not configured. Missing host, user, or key in settings."

        try:
            client = self._create_client()
            sftp = client.open_sftp()

            # Ensure remote directories exist
            self._ensure_remote_dir(sftp, self.remote_pdf_dir)
            self._ensure_remote_dir(sftp, self.remote_fixtures_dir)

            sftp.close()
            client.close()
            return True, f"SSH/SFTP connected to {self.user}@{self.host}:{self.port} (Dirs ready)"
        except Exception as exc:
            return False, f"SSH connection failed to {self.host}: {exc}"

    def _ensure_remote_dir(self, sftp: paramiko.SFTPClient, remote_dir: str) -> None:
        """Recursively ensure a remote directory exists (equivalent to mkdir -p)."""
        normalized = posixpath.normpath(remote_dir)
        parts = normalized.split("/")
        current = ""
        if normalized.startswith("/"):
            current = "/"

        for part in parts:
            if not part:
                continue
            current = posixpath.join(current, part)
            try:
                sftp.stat(current)
            except OSError:
                with contextlib.suppress(OSError):
                    sftp.mkdir(current)

    def upload_file(self, local_path: Path | str, remote_path: str) -> bool:
        """Upload a local file to a specified remote destination path."""
        local = Path(local_path)
        if not local.exists():
            logger.warning("Local file does not exist: %s", local)
            return False

        if not self.is_configured:
            logger.debug("SSH not configured, skipping remote upload of %s", local.name)
            return False

        try:
            client = self._create_client()
            sftp = client.open_sftp()

            remote_parent = posixpath.dirname(remote_path)
            self._ensure_remote_dir(sftp, remote_parent)

            sftp.put(str(local), remote_path)
            sftp.close()
            client.close()
            return True
        except Exception as exc:
            logger.error("Failed to upload %s to %s:%s: %s", local, self.host, remote_path, exc)
            return False

    def upload_pdf(self, local_pdf_path: Path | str, filename: str | None = None) -> str | None:
        """Archive a raw preprint PDF to the remote homelab storage directory."""
        local = Path(local_pdf_path)
        target_name = filename or local.name
        remote_dest = posixpath.join(self.remote_pdf_dir, target_name)
        if self.upload_file(local, remote_dest):
            return remote_dest
        return None

    def upload_fixture_tree(self, local_fixtures_dir: Path | str) -> int:
        """Recursively upload parquet and CSV fixtures to the homelab storage vault."""
        local_dir = Path(local_fixtures_dir)
        if not local_dir.exists():
            return 0

        if not self.is_configured:
            return 0

        uploaded_count = 0
        try:
            client = self._create_client()
            sftp = client.open_sftp()

            for file_path in local_dir.rglob("*"):
                if file_path.is_file():
                    rel_path = file_path.relative_to(local_dir).as_posix()
                    remote_dest = posixpath.join(self.remote_fixtures_dir, rel_path)
                    remote_parent = posixpath.dirname(remote_dest)
                    self._ensure_remote_dir(sftp, remote_parent)
                    sftp.put(str(file_path), remote_dest)
                    uploaded_count += 1

            sftp.close()
            client.close()
        except Exception as exc:
            logger.error("Failed uploading fixtures to %s: %s", self.host, exc)

        return uploaded_count

    def list_remote_pdfs(self) -> list[str]:
        """List filenames of all archived PDFs on the remote homelab server."""
        if not self.is_configured:
            return []

        try:
            client = self._create_client()
            sftp = client.open_sftp()
            files = sftp.listdir(self.remote_pdf_dir)
            sftp.close()
            client.close()
            return [f for f in files if f.lower().endswith(".pdf")]
        except Exception as exc:
            logger.debug("Failed listing remote PDFs on %s: %s", self.host, exc)
            return []


# Architectural alias
SSHStorageSync = SSHSyncManager
