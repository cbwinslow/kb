"""Global configuration settings for the Scientific Knowledge Base (kb).

Reads settings from environment variables or a local `.env` file with portable defaults.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for KB database, model paths, and remote synchronization."""

    model_config = SettingsConfigDict(
        env_prefix="KB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Database connection URL (defaults to portable SQLite if no PostgreSQL URL is provided)
    database_url: str = Field(
        default_factory=lambda: os.getenv(
            "KB_DATABASE_URL",
            "sqlite+aiosqlite:///data/kb.db",
        ),
        description="Async database connection URL (e.g. postgresql+asyncpg://... or sqlite+aiosqlite://...)",
    )

    # Local file paths
    data_dir: Path = Field(
        default=Path("data"),
        description="Root directory for local data artifacts",
    )
    fixtures_dir: Path = Field(
        default=Path("data/fixtures"),
        description="Directory for extracted benchmark Parquet/CSV tables",
    )
    pdf_download_dir: Path = Field(
        default=Path("data/arxiv_papers"),
        description="Directory for temporary or cached PDF downloads",
    )

    # Resource management
    disk_min_free_gb: float = Field(
        default=1.5,
        description="Minimum free disk space floor in GB before pausing downloads",
    )
    gpu_vram_fraction: float = Field(
        default=0.55,
        description="Maximum fraction of GPU VRAM allowed for batch model inferencing",
    )

    # Dense Embedding configuration
    embedding_model: str = Field(
        default="BAAI/bge-m3",
        description="HuggingFace model identifier for dense text embeddings",
    )
    embedding_device: Literal["auto", "cuda", "cpu"] = Field(
        default="auto",
        description="Target compute device for neural embedding models",
    )
    embedding_batch_size: int = Field(
        default=8,
        description="Batch size for embedding generation",
    )

    # Homelab Remote Storage (SSH / SFTP)
    ssh_host: str | None = Field(
        default=None,
        description="Remote homelab server hostname or IP address for archival storage",
    )
    ssh_port: int = Field(
        default=22,
        description="SSH port on remote homelab server",
    )
    ssh_user: str | None = Field(
        default=None,
        description="Username for SSH authentication",
    )
    ssh_key_path: Path | None = Field(
        default=Path("~/.ssh/id_ed25519").expanduser(),
        description="Path to SSH private key for key-based authentication",
    )
    ssh_password: str | None = Field(
        default=None,
        description="Optional password for SSH authentication if key is not used",
    )
    ssh_remote_pdf_dir: str = Field(
        default="/home/cbwinslow/workspace/kb/pdfs",
        description="Remote directory path on homelab for raw PDF archiving",
    )
    ssh_remote_fixtures_dir: str = Field(
        default="/home/cbwinslow/workspace/kb/fixtures",
        description="Remote directory path on homelab for benchmark Parquet fixtures",
    )

    # Web Dashboard UI settings
    ui_host: str = Field(
        default="127.0.0.1",
        description="Host interface for the interactive web dashboard",
    )
    ui_port: int = Field(
        default=8080,
        description="Port for the interactive web dashboard",
    )


# Global singleton settings instance
settings = Settings()
