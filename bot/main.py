from aiogram import Bot, Dispatcher
from bot.handlers import commands
from app.config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(commands.router)

async def start_bot():
    print("🤖 AI Lead Hunter bot started")
    await dp.start_polling(bot)