from aiogram import Bot

async def safe_send(bot: Bot, chat_id: int, text: str):
    try:
        await bot.send_message(chat_id, text)
    except Exception:
        pass