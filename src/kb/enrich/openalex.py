"""OpenAlex client for paper resolution, citation graph traversal, and topic enrichment."""

from __future__ import annotations

import logging
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://api.openalex.org"
DEFAULT_USER_AGENT = "ScientificKB/1.0 (mailto:blaine.winslow@gmail.com)"


@dataclass
class OpenAlexTopic:
    """Represents a scientific topic classification from OpenAlex."""

    id: str
    name: str
    score: float
    subfield: str = ""
    field: str = ""
    domain: str = ""


@dataclass
class OpenAlexWork:
    """Represents a research publication entity from OpenAlex."""

    id: str
    title: str
    doi: str | None = None
    publication_year: int | None = None
    cited_by_count: int = 0
    topics: list[dict[str, Any]] = field(default_factory=list)
    referenced_works: list[str] = field(default_factory=list)
    related_works: list[str] = field(default_factory=list)
    landing_page_url: str | None = None
    pdf_url: str | None = None
    authors: list[str] = field(default_factory=list)

    @property
    def short_id(self) -> str:
        """Returns the short OpenAlex ID without URI prefix (e.g., 'W1533576069')."""
        return self.id.split("/")[-1]


class OpenAlexClient:
    """Asynchronous client for OpenAlex API with rate-limiting respect and polite pool headers."""

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        email: str = "blaine.winslow@gmail.com",
        api_key: str | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        timeout: float = 15.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.email = email
        self.api_key = api_key or os.getenv("OPENALEX_API_KEY")
        self.timeout = timeout
        self.transport = transport

    def get_headers(self) -> dict[str, str]:
        """Returns polite User-Agent headers adhering to OpenAlex API conventions."""
        return self._headers()

    def parse_work_json(self, data: dict[str, Any]) -> OpenAlexWork:
        """Parses an OpenAlex work JSON dictionary into an OpenAlexWork dataclass."""
        return self._parse_work_json(data)

    def _headers(self) -> dict[str, str]:
        """Builds polite User-Agent headers adhering to OpenAlex API conventions."""
        headers = {
            "User-Agent": f"ScientificKB/1.0 (mailto:{self.email})",
            "Accept": "application/json",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _parse_work_json(self, data: dict[str, Any]) -> OpenAlexWork:
        """Parses an OpenAlex work JSON dictionary into an OpenAlexWork dataclass."""
        topics: list[dict[str, Any]] = []
        for t in data.get("topics", []):
            topics.append(
                {
                    "id": t.get("id"),
                    "name": t.get("display_name"),
                    "score": float(t.get("score", 0.0)),
                    "subfield": t.get("subfield", {}).get("display_name", ""),
                    "field": t.get("field", {}).get("display_name", ""),
                    "domain": t.get("domain", {}).get("display_name", ""),
                }
            )

        authors: list[str] = []
        for authorship in data.get("authorships", []):
            name = authorship.get("author", {}).get("display_name")
            if name:
                authors.append(name)

        best_oa = data.get("best_oa_location") or {}

        return OpenAlexWork(
            id=data.get("id", ""),
            title=data.get("title") or "Untitled",
            doi=data.get("doi"),
            publication_year=data.get("publication_year"),
            cited_by_count=int(data.get("cited_by_count", 0)),
            topics=topics,
            referenced_works=data.get("referenced_works", []),
            related_works=data.get("related_works", []),
            landing_page_url=best_oa.get("landing_page_url"),
            pdf_url=best_oa.get("pdf_url"),
            authors=authors,
        )

    async def get_work(self, work_id: str) -> OpenAlexWork | None:
        """Retrieves a single work by OpenAlex ID or full URI."""
        clean_id = work_id.split("/")[-1]
        url = f"{self.base_url}/works/{clean_id}"

        async with httpx.AsyncClient(
            transport=self.transport, timeout=self.timeout, headers=self._headers()
        ) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                return self._parse_work_json(resp.json())
            if resp.status_code == 404:
                return None
            logger.warning("OpenAlex get_work returned status %d: %s", resp.status_code, resp.text)
            return None

    async def get_work_by_doi(self, doi: str) -> OpenAlexWork | None:
        """Looks up a work by DOI."""
        clean_doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip())
        url = f"{self.base_url}/works/https://doi.org/{clean_doi}"

        async with httpx.AsyncClient(
            transport=self.transport, timeout=self.timeout, headers=self._headers()
        ) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                return self._parse_work_json(resp.json())
            if resp.status_code == 404:
                return None
            logger.warning("OpenAlex DOI lookup returned %d: %s", resp.status_code, resp.text)
            return None

    async def resolve_work(
        self,
        doi: str | None = None,
        arxiv_id: str | None = None,
        title: str | None = None,
        authors: list[str] | None = None,
        year: int | None = None,
    ) -> OpenAlexWork | None:
        """Resolves paper to an OpenAlex Work using DOI, arXiv, or title/author search."""
        # 1. Try DOI resolution first if available
        if doi:
            work = await self.get_work_by_doi(doi)
            if work:
                return work

        # 2. Try arXiv ID resolution via doi.org/10.48550/arxiv.<id>
        if arxiv_id:
            clean_arxiv = arxiv_id.strip()
            work = await self.get_work_by_doi(f"10.48550/arxiv.{clean_arxiv}")
            if work:
                return work

        # 3. Fallback: Search by title and author verification
        if title:
            clean_title = re.sub(r"[^\w\s]", " ", title).strip()
            title_words = [w for w in clean_title.split() if len(w) > 3][:6]
            key_terms = " ".join(title_words)

            candidates: list[dict[str, Any]] = []

            async with httpx.AsyncClient(
                transport=self.transport, timeout=self.timeout, headers=self._headers()
            ) as client:
                # Strategy A: Full title search
                resp_a = await client.get(
                    f"{self.base_url}/works",
                    params={"search": clean_title, "per-page": 5},
                )
                if resp_a.status_code == 200:
                    candidates.extend(resp_a.json().get("results", []))

                # Strategy B: Author last name + key terms search
                if authors and len(authors) > 0:
                    last_name = authors[0].split()[-1]
                    resp_b = await client.get(
                        f"{self.base_url}/works",
                        params={
                            "filter": f"default.search:{last_name} {key_terms}",
                            "per-page": 5,
                        },
                    )
                    if resp_b.status_code == 200:
                        candidates.extend(resp_b.json().get("results", []))

            # Prioritize candidate matching author last name and closest publication year
            if year and candidates:
                candidates.sort(key=lambda c: abs((c.get("publication_year") or 9999) - year))

            if authors and len(authors) > 0:
                first_author_last = authors[0].split()[-1].lower()
                for c in candidates:
                    cand_authors = [
                        a.get("author", {}).get("display_name", "").lower()
                        for a in c.get("authorships", [])
                    ]
                    if any(first_author_last in a for a in cand_authors):
                        return self._parse_work_json(c)

            # Otherwise return first candidate if available
            if candidates:
                return self._parse_work_json(candidates[0])

        return None

    async def get_citations(self, openalex_id: str, limit: int = 10) -> list[OpenAlexWork]:
        """Retrieves papers that cite the specified work."""
        clean_id = openalex_id.split("/")[-1]
        async with httpx.AsyncClient(
            transport=self.transport, timeout=self.timeout, headers=self._headers()
        ) as client:
            params = {
                "filter": f"cites:{clean_id}",
                "sort": "cited_by_count:desc",
                "per-page": limit,
            }
            resp = await client.get(f"{self.base_url}/works", params=params)
            if resp.status_code == 200:
                results = resp.json().get("results", [])
                return [self._parse_work_json(r) for r in results]
            return []

    async def get_related_papers(self, openalex_id: str, limit: int = 10) -> list[OpenAlexWork]:
        """Retrieves related works for the specified paper."""
        work = await self.get_work(openalex_id)
        if not work:
            return []

        # If the work has related_works IDs, fetch the top candidates
        if work.related_works:
            target_ids = [w.split("/")[-1] for w in work.related_works[:limit]]
            id_filter = "|".join(target_ids)
            async with httpx.AsyncClient(
                transport=self.transport, timeout=self.timeout, headers=self._headers()
            ) as client:
                params = {"filter": f"openalex:{id_filter}", "per-page": limit}
                resp = await client.get(f"{self.base_url}/works", params=params)
                if resp.status_code == 200:
                    results = resp.json().get("results", [])
                    return [self._parse_work_json(r) for r in results]

        # Fallback: Query by primary topic
        if work.topics:
            primary_topic_id = work.topics[0]["id"]
            if primary_topic_id:
                async with httpx.AsyncClient(
                    transport=self.transport, timeout=self.timeout, headers=self._headers()
                ) as client:
                    params = {
                        "filter": f"topics.id:{primary_topic_id}",
                        "sort": "cited_by_count:desc",
                        "per-page": limit,
                    }
                    resp = await client.get(f"{self.base_url}/works", params=params)
                    if resp.status_code == 200:
                        results = resp.json().get("results", [])
                        return [self._parse_work_json(r) for r in results if r.get("id") != work.id]

        return []

    async def search_targeted_corpus(
        self,
        keywords: list[str] | None = None,
        year_range: tuple[int, int] = (2024, 2026),
        limit: int = 25,
    ) -> list[OpenAlexWork]:
        """Harvests recent 2024-2026 academic literature covering bat tracking, aerodynamics, and biomechanics.

        Args:
            keywords: List of domain keyword phrases.
            year_range: Tuple of (start_year, end_year).
            limit: Maximum works to return.

        Returns:
            List of OpenAlexWork objects matching the query criteria.
        """
        search_terms = keywords or [
            "baseball bat tracking",
            "seam shifted wake",
            "baseball aerodynamics",
            "baseball biomechanics",
            "bat ball collision mechanics",
        ]
        query_str = " OR ".join(f'"{kw}"' for kw in search_terms)
        start_year, end_year = year_range

        async with httpx.AsyncClient(
            transport=self.transport, timeout=self.timeout, headers=self._headers()
        ) as client:
            params = {
                "filter": f"publication_year:{start_year}-{end_year},is_oa:true",
                "search": query_str,
                "sort": "publication_date:desc",
                "per-page": limit,
            }
            resp = await client.get(f"{self.base_url}/works", params=params)
            if resp.status_code == 200:
                results = resp.json().get("results", [])
                return [self._parse_work_json(r) for r in results]
            logger.warning("Targeted OpenAlex harvest returned %d: %s", resp.status_code, resp.text)
            return []

    async def download_work_pdf(
        self,
        work: OpenAlexWork,
        target_dir: Path | str,
        min_free_disk_gb: float = 1.5,
    ) -> Path | None:
        """Download open access PDF for an OpenAlexWork with local disk space threshold protection.

        Args:
            work: OpenAlexWork instance with pdf_url.
            target_dir: Local destination directory.
            min_free_disk_gb: Minimum free disk space in GB required (default 1.5 GB).

        Returns:
            Path to downloaded PDF or None if download failed or disk space threshold reached.
        """
        if not work.pdf_url:
            logger.debug("Work %s has no direct open access PDF URL", work.short_id)
            return None

        dest_dir = Path(target_dir)
        dest_dir.mkdir(parents=True, exist_ok=True)

        _total, _used, free = shutil.disk_usage(dest_dir)
        free_gb = free / (1024**3)
        if free_gb < min_free_disk_gb:
            logger.error(
                "Disk space safeguard triggered: %.2f GB free < %.2f GB threshold. Aborting download.",
                free_gb,
                min_free_disk_gb,
            )
            return None

        out_path = dest_dir / f"{work.short_id}.pdf"
        try:
            async with httpx.AsyncClient(
                transport=self.transport,
                timeout=30.0,
                headers={"User-Agent": f"ScientificKB/1.0 (mailto:{self.email})"},
                follow_redirects=True,
            ) as client:
                resp = await client.get(work.pdf_url)
                if resp.status_code == 200 and resp.content.startswith(b"%PDF"):
                    out_path.write_bytes(resp.content)
                    return out_path
                logger.warning(
                    "Failed downloading PDF for %s (status=%d, size=%d)",
                    work.short_id,
                    resp.status_code,
                    len(resp.content),
                )
                return None
        except Exception as exc:
            logger.error("Download exception for %s: %s", work.short_id, exc)
            return None
