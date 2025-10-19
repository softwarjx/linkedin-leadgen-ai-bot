import httpx
from typing import List, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.config import settings
from app.models.lead import Lead

SERPAPI_URL = "https://serpapi.com/search.json"

def _build_query(niche: str, country: str | None = None) -> str:
    q = f'site:linkedin.com "{niche}"'
    if country:
        q += f' "{country}"'
    return q

async def serpapi_linkedin_search(niche: str, country: str | None, limit: int) -> List[Dict]:
    params = {
        "engine": "google",
        "q": _build_query(niche, country),
        "api_key": settings.SERPAPI_API_KEY,
        "num": min(limit, 20),
    }
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(SERPAPI_URL, params=params)
        r.raise_for_status()
        data = r.json()

    results = []
    for item in data.get("organic_results", []):
        link = item.get("link")
        title = item.get("title")  # часто содержит имя/должность
        snippet = item.get("snippet", "")
        displayed_link = item.get("displayed_link", "")

        if not link or "linkedin.com" not in link:
            continue

        parsed = {
            "name": None,
            "title": None,
            "company": None,
            "location": None,
            "profile_url": link,
        }

        # Простейший парсинг заголовка/сниппета (лучше не усложнять)
        if title:
            parsed["title"] = title
        if snippet:
            parsed["company"] = snippet[:300]

        results.append(parsed)
        if len(results) >= limit:
            break

    return results

async def store_leads(db: AsyncSession, niche: str, query: str | None, leads: List[Dict]) -> int:
    saved = 0
    for l in leads:
        # проверка дубликатов по profile_url
        exists = await db.execute(select(Lead).where(Lead.profile_url == l["profile_url"]))
        if exists.scalar_one_or_none():
            continue
        lead = Lead(
            name=l.get("name"),
            title=l.get("title"),
            company=l.get("company"),
            location=l.get("location"),
            profile_url=l["profile_url"],
            email=None,
            niche=niche,
            query=query,
        )
        db.add(lead)
        saved += 1
    await db.commit()
    return saved