content = """# LinkedIn AI LeadGen Bot – B2B Prospecting + AI Outreach

🚀 AI-powered LinkedIn lead generation bot that automates **B2B prospect discovery + AI outreach**.  
Find ideal clients by niche and country, store leads, and generate **high-converting personalized messages** using AI (DeepSeek).

🔗 **Live Demo (Telegram):** https://t.me/AIHunterLeadbot  
📡 **API Ready · AI Powered · Business Focused · Portfolio Friendly**

---

## ✅ Key Features

- 🔍 LinkedIn lead discovery via Google (SerpAPI)
- 🌎 Target by niche + optional country filter
- 🤖 AI Outreach message generation (DeepSeek)
- 💾 Saves leads to SQLite database
- 📤 Export leads to CSV
- ⚡ FastAPI REST backend + Telegram Bot frontend
- 🧩 Clean modular architecture
- 🚀 Deployable on Render / Railway / VPS

---

## 🛠️ Tech Stack

| Component       | Technology          |
| --------------- | ------------------- |
| Language        | Python 3.10+        |
| Bot Framework   | Aiogram 3           |
| Backend API     | FastAPI             |
| AI Model        | DeepSeek Chat       |
| Lead Search API | SerpAPI             |
| Database        | SQLite + SQLAlchemy |
| HTTP Client     | HTTPX               |
| Deployment      | Render              |

---

## 💼 Why this project matters

Businesses waste **hours manually searching and messaging leads on LinkedIn**.  
This project solves that by letting users:

✅ Find targeted leads automatically  
✅ Personalize outreach instantly using AI  
✅ Export lead data for CRM or campaigns  
✅ Automate sales prospecting to save time & close more deals

---

## 🏗️ Architecture Overview

```
Client (User)
     │ Telegram Bot
     ▼
 Command Handler ────▶ Lead Search Service ──▶ SerpAPI (LinkedIn)
     │
     ├──▶ AI Outreach Service ──────────────▶ DeepSeek AI
     │
     └──▶ Database (SQLite) ────────────────▶ CSV Export / API Access
```

---

## 📂 Project Structure

```
linkedin-leadgen-ai-bot/
├── app/
│   ├── api/               # FastAPI endpoints
│   ├── services/          # Lead search + AI logic
│   ├── models/            # DB models
│   ├── database/          # Connection + session
│   └── config.py          # Settings (.env)
├── bot/
│   ├── handlers/          # Bot commands
│   ├── utils/             # Helpers
│   └── main.py            # Bot bootstrap
├── main.py                # Run API + Bot
├── requirements.txt
└── .env
```

---

## 🚀 Installation

```bash
git clone https://github.com/softwarjx/linkedin-leadgen-ai-bot.git
cd linkedin-leadgen-ai-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```
DEEPSEEK_API_KEY=your_deepseek_key
SERPAPI_API_KEY=your_serpapi_key
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite+aiosqlite:///./app.db
```

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🤖 Telegram Commands

| Command                           | Description                        |
| --------------------------------- | ---------------------------------- |
| `/start`                          | Show help and usage                |
| `/hunt niche;country=USA;limit=5` | Search LinkedIn leads              |
| `/pitch niche`                    | Generate outreach message using AI |

Example:

```
/hunt SaaS founders;country=USA;limit=5
/pitch digital agencies
```

---

## 🔌 REST API

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| POST   | `/api/hunt`       | Search and store leads |
| GET    | `/api/leads`      | Retrieve leads         |
| GET    | `/api/export.csv` | Export leads to CSV    |

---

## ☁️ Deploy to Render (Free)

1. Push to GitHub
2. Create new web service on https://render.com
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Add environment variables in dashboard

---

## 💼 Use Cases

✅ B2B Prospecting  
✅ SaaS Lead Generation  
✅ Agency Client Outreach  
✅ LinkedIn Automation  
✅ Startup Sales Pipeline

---

## 🧩 TODO (Improvements)

- ✅ Add PostgreSQL support
- 🔄 Auto resume lead scraping
- 📩 Email scraping
- 🧠 Multi-language outreach
- 🌐 Web Dashboard

---

## ⭐ Hire Me

**Author:** Serhii Dev  
📍 Ukraine  
💬 Telegram: https://t.me/softwarjx  
📧 Email: softwarjx1@gmail.com  
⭐ Like this project? Star the repo!

---

## 📜 License

MIT License
"""
with open("README_FULL.md","w",encoding="utf-8") as f:
f.write(content)
