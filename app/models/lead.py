from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func, Text
from app.database.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    title: Mapped[str | None] = mapped_column(String(300), nullable=True)
    company: Mapped[str | None] = mapped_column(String(300), nullable=True)
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    profile_url: Mapped[str] = mapped_column(String(800), nullable=False, unique=True)
    email: Mapped[str | None] = mapped_column(String(300), nullable=True)
    niche: Mapped[str | None] = mapped_column(String(200), nullable=True, index=True)
    query: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped["DateTime"] = mapped_column(DateTime(timezone=True), server_default=func.now())