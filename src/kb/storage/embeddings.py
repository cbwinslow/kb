"""Local GPU-accelerated dense embedding pipeline supporting BAAI/bge-m3 and mock testing."""

from __future__ import annotations

import hashlib
import logging
import math
from typing import Any, Protocol, runtime_checkable

from kb.config import settings

logger = logging.getLogger(__name__)

DEFAULT_EMBEDDING_MODEL = settings.embedding_model
EMBEDDING_DIMENSION = 1024


@runtime_checkable
class EmbeddingProtocol(Protocol):
    """Protocol defining the interface for dense text embedders."""

    def embed_texts(self, texts: list[str], batch_size: int = 16) -> list[list[float]]:
        """Computes dense vector embeddings for a list of text strings."""
        ...

    def embed_query(self, text: str) -> list[float]:
        """Computes a dense vector embedding for a single search query."""
        ...


class MockEmbeddingGenerator:
    """Deterministic, fast mock embedder for hermetic testing without GPU or network downloads."""

    def __init__(self, dimension: int = EMBEDDING_DIMENSION) -> None:
        self.dimension = dimension

    def _hash_to_unit_vector(self, text: str) -> list[float]:
        """Converts text into a deterministic, unit-normalized float vector."""
        if not text:
            vec = [0.0] * self.dimension
            vec[0] = 1.0
            return vec

        raw_hash = hashlib.sha256(text.encode("utf-8")).digest()
        # Seed float components deterministically from sha256 bytes
        vec: list[float] = []
        for i in range(self.dimension):
            byte_val = raw_hash[i % len(raw_hash)]
            vec.append(float(byte_val) - 128.0)

        norm = math.sqrt(sum(x * x for x in vec))
        if norm == 0.0:
            vec[0] = 1.0
            return vec
        return [x / norm for x in vec]

    def embed_texts(self, texts: list[str], batch_size: int = 16) -> list[list[float]]:
        """Embeds a list of texts using deterministic hashing."""
        _ = batch_size
        return [self._hash_to_unit_vector(t) for t in texts]

    def embed_query(self, text: str) -> list[float]:
        """Embeds a query text using deterministic hashing."""
        return self._hash_to_unit_vector(text)


class LocalEmbeddingGenerator:
    """GPU-accelerated embedding generator wrapping sentence-transformers with VRAM controls."""

    def __init__(
        self,
        model_name: str = DEFAULT_EMBEDDING_MODEL,
        device: str = "auto",
        normalize: bool = True,
        max_seq_length: int = 1024,
    ) -> None:
        self.model_name = model_name
        self.normalize = normalize
        self.max_seq_length = max_seq_length
        self._model: Any = None

        if device == "auto":
            try:
                import torch

                self.device = "cuda" if torch.cuda.is_available() else "cpu"
            except ImportError:
                self.device = "cpu"
        else:
            self.device = device

        logger.info(
            "Configured LocalEmbeddingGenerator with model %s on %s (max_seq_length=%d)",
            self.model_name,
            self.device,
            self.max_seq_length,
        )

    @property
    def model(self) -> Any:
        """Lazy loads SentenceTransformer model into memory/VRAM on first access."""
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            logger.info("Loading embedding model %s onto %s...", self.model_name, self.device)
            self._model = SentenceTransformer(self.model_name, device=self.device)
            if hasattr(self._model, "max_seq_length"):
                self._model.max_seq_length = self.max_seq_length
        return self._model

    def embed_texts(self, texts: list[str], batch_size: int = 8) -> list[list[float]]:
        """Embeds a batch of texts into 1024-d normalized vectors with VRAM protection."""
        if not texts:
            return []

        try:
            embeddings = self.model.encode(
                texts,
                batch_size=batch_size,
                show_progress_bar=False,
                normalize_embeddings=self.normalize,
                convert_to_numpy=True,
            )
            return [vec.tolist() for vec in embeddings]
        finally:
            if self.device.startswith("cuda"):
                try:
                    import torch

                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                except ImportError:
                    pass

    def embed_query(self, text: str) -> list[float]:
        """Embeds a single query string into a 1024-d normalized vector."""
        if not text:
            return [0.0] * EMBEDDING_DIMENSION

        try:
            embedding = self.model.encode(
                text,
                show_progress_bar=False,
                normalize_embeddings=self.normalize,
                convert_to_numpy=True,
            )
            return embedding.tolist()  # type: ignore[no-any-return]
        finally:
            if self.device.startswith("cuda"):
                try:
                    import torch

                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                except ImportError:
                    pass
