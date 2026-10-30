"""Scholarly web search and literature discovery engine."""

from __future__ import annotations

import asyncio
import re
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Literal

import bs4
import httpx
from pydantic import BaseModel, Field

from kb.logging import get_logger

logger = get_logger(__name__)


class SearchResult(BaseModel):
    """Structured representation of a scholarly or web search result."""

    title: str
    authors: list[str] = Field(default_factory=list)
    year: int | None = None
    abstract: str | None = None
    source: Literal["arxiv", "openalex", "web"]
    url: str
    pdf_url: str | None = None
    citation_count: int | None = None
    doi: str | None = None
    arxiv_id: str | None = None


class ScholarlyWebSearcher:
    """Async scholarly search coordinator querying arXiv, OpenAlex, and web resources."""

    def __init__(self, timeout: float = 12.0) -> None:
        """Initialize searcher with configurable HTTP timeout.

        Args:
            timeout: Maximum seconds to wait for external API responses.
        """
        self.timeout = timeout
        self.headers = {
            "User-Agent": "kb-research-engine/0.1 (mailto:kb-research@local.internal)",
            "Accept": "application/json, application/xml, text/html",
        }

    async def search_arxiv(self, query: str, limit: int = 10) -> list[SearchResult]:
        """Search arXiv via the official Atom API.

        Args:
            query: Search keywords or boolean search string.
            limit: Maximum number of records to return.

        Returns:
            List of normalized SearchResult instances from arXiv.
        """
        encoded_query = urllib.parse.quote(query)
        url = f"https://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={limit}"
        results: list[SearchResult] = []

        try:
            async with httpx.AsyncClient(timeout=self.timeout, follow_redirects=True) as client:
                resp = await client.get(url, headers=self.headers)
                if resp.status_code != 200:
                    logger.warning("arXiv search returned status %d for '%s'", resp.status_code, query)
                    return results

                root = ET.fromstring(resp.text)
                ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

                for entry in root.findall("atom:entry", ns):
                    id_elem = entry.find("atom:id", ns)
                    title_elem = entry.find("atom:title", ns)
                    summary_elem = entry.find("atom:summary", ns)
                    published_elem = entry.find("atom:published", ns)
                    doi_elem = entry.find("arxiv:doi", ns)

                    raw_id = id_elem.text.strip() if id_elem is not None and id_elem.text else ""
                    arxiv_id = raw_id.split("/abs/")[-1] if "/abs/" in raw_id else raw_id

                    title = " ".join(title_elem.text.split()) if title_elem is not None and title_elem.text else "Untitled"
                    summary = " ".join(summary_elem.text.split()) if summary_elem is not None and summary_elem.text else None

                    year: int | None = None
                    if published_elem is not None and published_elem.text:
                        match = re.search(r"(\d{4})", published_elem.text)
                        if match:
                            year = int(match.group(1))

                    authors: list[str] = []
                    for a in entry.findall("atom:author", ns):
                        name_elem = a.find("atom:name", ns)
                        if name_elem is not None and name_elem.text:
                            authors.append(name_elem.text.strip())

                    pdf_url: str | None = None
                    for link in entry.findall("atom:link", ns):
                        if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                            pdf_url = link.attrib.get("href")
                            break
                    if not pdf_url and arxiv_id:
                        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

                    doi = doi_elem.text.strip() if doi_elem is not None and doi_elem.text else None

                    results.append(
                        SearchResult(
                            title=title,
                            authors=authors,
                            year=year,
                            abstract=summary,
                            source="arxiv",
                            url=raw_id or f"https://arxiv.org/abs/{arxiv_id}",
                            pdf_url=pdf_url,
                            citation_count=None,
                            doi=doi,
                            arxiv_id=arxiv_id,
                        )
                    )
        except Exception as e:
            logger.warning("Failed to search arXiv for '%s': %s", query, e)

        return results

    async def search_openalex(self, query: str, limit: int = 10) -> list[SearchResult]:
        """Search OpenAlex works repository.

        Args:
            query: Search keywords or topic.
            limit: Maximum number of works to return.

        Returns:
            List of normalized SearchResult instances from OpenAlex.
        """
        encoded_query = urllib.parse.quote(query)
        url = f"https://api.openalex.org/works?search={encoded_query}&per_page={limit}&sort=cited_by_count:desc"
        results: list[SearchResult] = []

        try:
            async with httpx.AsyncClient(timeout=self.timeout, follow_redirects=True) as client:
                resp = await client.get(url, headers=self.headers)
                if resp.status_code != 200:
                    logger.warning("OpenAlex search returned status %d for '%s'", resp.status_code, query)
                    return results

                data = resp.json()
                for work in data.get("results", []):
                    title = work.get("display_name") or "Untitled"
                    year = work.get("publication_year")
                    citations = work.get("cited_by_count")
                    doi = work.get("doi")
                    openalex_url = work.get("id") or (doi if doi else "")

                    # Authors
                    authors: list[str] = []
                    for authorship in work.get("authorships", []):
                        author = authorship.get("author", {})
                        if author and author.get("display_name"):
                            authors.append(author["display_name"])

                    # Abstract from inverted index if present
                    abstract: str | None = None
                    inv_index = work.get("abstract_inverted_index")
                    if isinstance(inv_index, dict):
                        positions: list[tuple[int, str]] = []
                        for word, idxs in inv_index.items():
                            for pos in idxs:
                                positions.append((pos, word))
                        positions.sort(key=lambda x: x[0])
                        abstract = " ".join([w for _, w in positions])

                    # PDF URL
                    pdf_url: str | None = None
                    oa = work.get("open_access", {})
                    if oa.get("oa_url") and oa["oa_url"].endswith(".pdf"):
                        pdf_url = oa["oa_url"]
                    elif work.get("best_oa_location", {}).get("pdf_url"):
                        pdf_url = work["best_oa_location"]["pdf_url"]

                    results.append(
                        SearchResult(
                            title=title,
                            authors=authors,
                            year=year,
                            abstract=abstract[:800] if abstract else None,
                            source="openalex",
                            url=doi or openalex_url,
                            pdf_url=pdf_url,
                            citation_count=citations,
                            doi=doi.replace("https://doi.org/", "") if doi else None,
                            arxiv_id=None,
                        )
                    )
        except Exception as e:
            logger.warning("Failed to search OpenAlex for '%s': %s", query, e)

        return results

    async def search_web_fallback(self, query: str, limit: int = 5) -> list[SearchResult]:
        """Search DuckDuckGo HTML for quantitative articles and online glossaries.

        Args:
            query: Search query string.
            limit: Maximum web results to extract.

        Returns:
            List of SearchResult items with source='web'.
        """
        url = "https://html.duckduckgo.com/html/"
        results: list[SearchResult] = []

        try:
            async with httpx.AsyncClient(timeout=self.timeout, follow_redirects=True) as client:
                data = {"q": query}
                resp = await client.post(url, data=data, headers=self.headers)
                if resp.status_code != 200:
                    logger.warning("Web fallback search returned status %d", resp.status_code)
                    return results

                soup = bs4.BeautifulSoup(resp.text, "html.parser")
                links = soup.select(".result__body")

                for item in links[:limit]:
                    title_elem = item.select_one(".result__title .result__url") or item.select_one(".result__title")
                    snippet_elem = item.select_one(".result__snippet")
                    href_elem = item.select_one(".result__title a")

                    title = title_elem.get_text(strip=True) if title_elem else "Web Result"
                    snippet = snippet_elem.get_text(strip=True) if snippet_elem else None
                    target_url = href_elem.get("href") if href_elem else None

                    if target_url and isinstance(target_url, str):
                        # Extract redirect link if wrapped in DuckDuckGo uddg parameter
                        if "uddg=" in target_url:
                            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(target_url).query)
                            if "uddg" in parsed and parsed["uddg"]:
                                target_url = parsed["uddg"][0]

                        results.append(
                            SearchResult(
                                title=title,
                                authors=[],
                                year=None,
                                abstract=snippet,
                                source="web",
                                url=target_url,
                                pdf_url=target_url if target_url.endswith(".pdf") else None,
                                citation_count=None,
                                doi=None,
                                arxiv_id=None,
                            )
                        )
        except Exception as e:
            logger.warning("Web fallback search failed for '%s': %s", query, e)

        return results

    async def search(
        self,
        query: str,
        source: Literal["all", "arxiv", "openalex", "web"] = "all",
        limit: int = 10,
    ) -> list[SearchResult]:
        """Execute multi-source scholarly literature search.

        Args:
            query: Keywords, author names, or quantitative domain questions.
            source: Selected search endpoint or 'all' for unified multi-source queries.
            limit: Maximum combined results to return.

        Returns:
            List of deduplicated SearchResult objects ranked by relevance and citations.
        """
        if source == "arxiv":
            return await self.search_arxiv(query, limit=limit)
        elif source == "openalex":
            return await self.search_openalex(query, limit=limit)
        elif source == "web":
            return await self.search_web_fallback(query, limit=limit)

        # source == 'all': run concurrently
        arxiv_task = self.search_arxiv(query, limit=limit)
        openalex_task = self.search_openalex(query, limit=limit)

        arxiv_res, openalex_res = await asyncio.gather(arxiv_task, openalex_task, return_exceptions=True)

        combined: list[SearchResult] = []
        if isinstance(openalex_res, list):
            combined.extend(openalex_res)
        if isinstance(arxiv_res, list):
            combined.extend(arxiv_res)

        # Deduplicate results by title similarity and DOI
        seen_titles: set[str] = set()
        seen_dois: set[str] = set()
        deduped: list[SearchResult] = []

        for item in combined:
            norm_title = re.sub(r"[^a-zA-Z0-9]", "", item.title).lower()
            if item.doi and item.doi in seen_dois:
                continue
            if norm_title in seen_titles:
                continue

            if item.doi:
                seen_dois.add(item.doi)
            if norm_title:
                seen_titles.add(norm_title)
            deduped.append(item)

            if len(deduped) >= limit:
                break

        return deduped
