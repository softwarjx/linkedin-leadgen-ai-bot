import asyncio
from fastapi import FastAPI
from app.database.db import init_db
from app.api.routes import router as api_router
from bot.main import start_bot

app = FastAPI(title="AI Lead Hunter (LinkedIn Edition)")

@app.on_event("startup")
async def on_startup():
    await init_db()
    asyncio.create_task(start_bot())

@app.get("/")
async def health():
    return {"status": "ok", "message": "API ✅, Bot 🤖 running"}

app.include_router(api_router, prefix="/api", tags=["leads"])