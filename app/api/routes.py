from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.responses import StreamingResponse
import csv
import io

from app.database.db import SessionLocal
from app.models.lead import Lead
from app.services.search import serpapi_linkedin_search, store_leads

router = APIRouter()

async def get_db():
    async with SessionLocal() as db:
        yield db

@router.post("/hunt")
async def hunt_leads(
    niche: str = Query(..., description="e.g. SaaS founders, dental clinics, e-commerce owners"),
    country: str | None = Query(None, description="e.g. USA, Germany"),
    limit: int = Query(15, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    results = await serpapi_linkedin_search(niche=niche, country=country, limit=limit)
    saved = await store_leads(db, niche=niche, query=f"{niche} {country or ''}".strip(), leads=results)
    return {"found": len(results), "saved": saved}

@router.get("/leads")
async def list_leads(
    niche: str | None = None,
    limit: int = Query(50, ge=1, le=500),
    db: AsyncSession = Depends(get_db),
):
    q = select(Lead).order_by(Lead.created_at.desc())
    if niche:
        q = q.where(Lead.niche == niche)
    res = await db.execute(q)
    leads = res.scalars().all()[:limit]
    return [
        {
            "id": l.id,
            "name": l.name,
            "title": l.title,
            "company": l.company,
            "location": l.location,
            "profile_url": l.profile_url,
            "niche": l.niche,
            "created_at": l.created_at,
        }
        for l in leads
    ]

@router.get("/export.csv")
async def export_csv(
    niche: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    q = select(Lead).order_by(Lead.created_at.desc())
    if niche:
        q = q.where(Lead.niche == niche)
    res = await db.execute(q)
    leads = res.scalars().all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["name", "title", "company", "location", "profile_url", "niche", "created_at"])
    for l in leads:
        writer.writerow([l.name or "", l.title or "", l.company or "", l.location or "", l.profile_url, l.niche or "", l.created_at])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=leads.csv"})