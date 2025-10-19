import os
from pydantic import BaseModel
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

class Settings(BaseModel):
    # API Keys
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    SERPAPI_API_KEY: str = os.getenv("SERPAPI_API_KEY", "")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")

    # Default app settings
    DEFAULT_LIMIT: int = int(os.getenv("DEFAULT_LIMIT", "10"))

settings = Settings()