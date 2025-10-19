import httpx
from app.config import settings

DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"

async def generate_outreach(niche: str, context: str | None = None, language: str = "en") -> str:
    headers = {
        "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = (
        f"You are an expert cold outreach copywriter. Write a personalized outreach message.\n"
        f"Niche: {niche}\n"
        f"Context: {context or 'none'}\n"
        f"Language: {language}\n"
        "Keep it under 600 characters. Be friendly and professional."
    )

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You write short, high-converting outreach."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.post(DEEPSEEK_URL, headers=headers, json=payload)
        data = response.json()

    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception:
        return "Error generating message. Try again."