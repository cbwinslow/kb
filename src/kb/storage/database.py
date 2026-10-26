"""Database connection manager and session factory for PostgreSQL and SQLite."""

from __future__ import annotations

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool

from kb.config import settings
from kb.storage.models import Base

logger = logging.getLogger(__name__)

DEFAULT_DATABASE_URL = settings.database_url


class DatabaseManager:
    """Manages asynchronous database connections, session lifecycle, and schema initialization."""

    def __init__(
        self,
        database_url: str | None = None,
        echo: bool = False,
        **engine_kwargs: Any,
    ) -> None:
        self.url = database_url or settings.database_url
        self.is_sqlite = self.url.startswith("sqlite")
        self.is_postgres = "postgresql" in self.url

        kwargs: dict[str, Any] = {"echo": echo, **engine_kwargs}
        if self.is_sqlite:
            if "poolclass" not in kwargs:
                kwargs["poolclass"] = StaticPool
        elif "pool_size" not in kwargs:
            kwargs["pool_size"] = 5
            kwargs["max_overflow"] = 10

        self.engine: AsyncEngine = create_async_engine(self.url, **kwargs)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    async def init_db(self) -> None:
        """Initializes extensions and creates database tables."""
        async with self.engine.begin() as conn:
            if self.is_postgres:
                # Enable pgvector extension if available
                await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
                # Ensure newly added columns exist on kb_documents
                await conn.execute(text(
                    "ALTER TABLE kb_documents ADD COLUMN IF NOT EXISTS openalex_id VARCHAR(128);"
                ))
                await conn.execute(text(
                    "ALTER TABLE kb_documents ADD COLUMN IF NOT EXISTS citation_count INTEGER;"
                ))
                await conn.execute(text(
                    "ALTER TABLE kb_documents ADD COLUMN IF NOT EXISTS "
                    "topics JSONB DEFAULT '[]'::jsonb;"
                ))
                await conn.execute(text(
                    "ALTER TABLE kb_documents ADD COLUMN IF NOT EXISTS "
                    "referenced_works JSONB DEFAULT '[]'::jsonb;"
                ))
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database schema initialized successfully for %s", self.url.split("@")[-1])

    async def drop_db(self) -> None:
        """Drops all database tables."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        logger.info("Database schema dropped successfully")

    async def check_connection(self) -> tuple[bool, str]:
        """Handshakes with the database server and returns connectivity status."""
        try:
            async with self.engine.connect() as conn:
                result = await conn.execute(text("SELECT 1;"))
                scalar = result.scalar()
                if scalar == 1:
                    host_info = self.url.split("@")[-1].split("/")[0] if "@" in self.url else "local"
                    backend = f"PostgreSQL ({host_info})" if self.is_postgres else "SQLite"
                    return True, f"Connection established to {backend} [{self.url.split('@')[-1]}]"
                return False, f"Unexpected response from database: {scalar}"
        except Exception as exc:
            target = self.url.split("@")[-1] if "@" in self.url else self.url
            return False, f"Database handshake failed for {target}: {exc}"

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Provides an asynchronous transactional session."""
        session: AsyncSession = self.session_factory()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def close(self) -> None:
        """Closes the connection pool and disposes the engine."""
        await self.engine.dispose()
