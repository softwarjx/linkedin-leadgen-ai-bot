from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import SessionLocal
from app.services.search import serpapi_linkedin_search, store_leads
from app.services.ai import generate_outreach
from app.config import settings

router = Router()

def parse_hunt_args(text: str):
    # /hunt niche;country=USA;limit=10
    raw = text.split(" ", 1)
    if len(raw) == 1:
        return None, None, settings.DEFAULT_LIMIT
    params = {"niche": None, "country": None, "limit": settings.DEFAULT_LIMIT}
    payload = raw[1]
    parts = [p.strip() for p in payload.split(";") if p.strip()]
    if parts:
        params["niche"] = parts[0]
    for p in parts[1:]:
        if p.lower().startswith("country="):
            params["country"] = p.split("=", 1)[1]
        elif p.lower().startswith("limit="):
            try:
                params["limit"] = int(p.split("=", 1)[1])
            except ValueError:
                pass
    return params["niche"], params["country"], params["limit"]

@router.message(Command("start"))
async def cmd_start(m: Message):
    await m.answer(
        "👋 AI Lead Hunter (LinkedIn Edition)\n\n"
        "Commands:\n"
        "• /hunt niche;country=USA;limit=10 — find leads\n"
        "• /pitch <niche> — generate outreach text\n"
        "• /help — show help\n\n"
        "Example:\n/hunt SaaS founders;country=USA;limit=10"
    )

@router.message(Command("help"))
async def cmd_help(m: Message):
    await m.answer(
        "📘 Help\n"
        "/hunt <niche>;country=<COUNTRY>;limit=<N> — search & save leads\n"
        "/pitch <niche> — generate one outreach message"
    )

@router.message(Command("hunt"))
async def cmd_hunt(m: Message):
    niche, country, limit = parse_hunt_args(m.text or "")
    if not niche:
        return await m.answer("Usage:\n/hunt <niche>;country=USA;limit=10")
    await m.answer(f"🔎 Searching LinkedIn leads for: {niche} (country={country or 'any'}, limit={limit}) ...")

    async with SessionLocal() as db:  # type: AsyncSession
        results = await serpapi_linkedin_search(niche=niche, country=country, limit=limit)
        saved = await store_leads(db, niche=niche, query=f"{niche} {country or ''}".strip(), leads=results)

    await m.answer(f"✅ Done. Found: {len(results)} | Saved to DB: {saved}\nUse /pitch {niche} to generate outreach.\nExport via API: /export.csv")

@router.message(Command("pitch"))
async def cmd_pitch(m: Message):
    parts = (m.text or "").split(" ", 1)
    if len(parts) < 2:
        return await m.answer("Usage:\n/pitch <niche>")
    niche = parts[1].strip()
    text = await generate_outreach(niche=niche, context=None, language="en")
    await m.answer(f"✉️ Example outreach for *{niche}*:\n\n{text}", parse_mode="Markdown")