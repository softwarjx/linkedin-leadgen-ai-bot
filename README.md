# 🚀 LinkedIn AI LeadGen Bot – Automate B2B Prospecting & AI Outreach

Smart AI-powered LinkedIn lead generation bot that finds **qualified B2B leads** and writes **personalized outreach messages** automatically. Built with **FastAPI + Telegram Bot + DeepSeek AI + SerpAPI**.

🔗 **Live Demo:** https://t.me/AIHunterLeadbot  
📣 Perfect for **Agencies · SaaS · B2B Sales · Freelancers · AI Automation**  
⚡ Boost outbound sales · Automate cold outreach · Save time · Scale faster

---

## ✅ Product Highlights

| Feature                   | Description                                                   |
| ------------------------- | ------------------------------------------------------------- |
| 🔎 AI Lead Finder         | Scrapes LinkedIn profiles via Google safely (no account risk) |
| 🎯 B2B Targeting          | Search by niche + country filters                             |
| ✉️ AI Outreach Copy       | Writes custom cold DMs using DeepSeek AI                      |
| 🛢 Lead Storage            | Saves leads to local database                                 |
| 📤 Export                 | Export leads to CSV for CRM/email campaigns                   |
| 🤖 Telegram Bot Interface | Easy to use — no UI needed                                    |
| ⚡ API Included           | Can integrate with SaaS or CRM                                |
| 🚀 Deployable             | Works on Render, Railway or VPS                               |

---

## 🛠️ Tech Stack

| Category       | Technologies        |
| -------------- | ------------------- |
| Language       | Python              |
| Backend        | FastAPI             |
| Bot Engine     | Aiogram 3           |
| AI Copywriting | DeepSeek AI         |
| Lead Scraping  | SerpAPI             |
| Database       | SQLite + SQLAlchemy |
| HTTP Client    | HTTPX               |
| Deployment     | Render              |

---

## 💼 Why this project?

Thousands of businesses lose leads because manual LinkedIn prospecting is slow and inefficient.  
This project solves that using **AI + Automation**:

✅ Faster prospecting → no manual search  
✅ Personalized messages → higher reply rate  
✅ Works for agencies, SaaS & B2B sales teams  
✅ Ready to use or extend into SaaS/business tool

---

## 🧠 Architecture

```
User
  │
  ├─> Telegram Bot (Aiogram)
  │       └─ Commands (/hunt, /pitch)
  │
  ├─> Lead Scraper (SerpAPI + Google Search)
  │
  ├─> AI Outreach Writer (DeepSeek API)
  │
  └─> Database (SQLite) + API + CSV Export
```

---

## 📂 Folder Structure

```
linkedin-leadgen-ai-bot/
├── app/
│   ├── api/            # FastAPI endpoints
│   ├── services/       # AI + Leadgen logic
│   ├── models/         # DB models
│   ├── database/       # DB config
│   └── config.py
├── bot/
│   ├── handlers/       # Telegram commands
│   ├── utils/
│   └── main.py
├── main.py
├── requirements.txt
└── .env
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/softwarjx/linkedin-leadgen-ai-bot.git
cd linkedin-leadgen-ai-bot
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env`:

```
DEEPSEEK_API_KEY=your_key_here
SERPAPI_API_KEY=your_key_here
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite+aiosqlite:///./app.db
```

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🤖 Telegram Commands

| Command                            | Purpose               |
| ---------------------------------- | --------------------- |
| `/start`                           | Welcome message       |
| `/hunt niche;country=USA;limit=10` | Search LinkedIn leads |
| `/pitch niche`                     | Generate AI message   |

✅ Example:

```
/hunt SaaS founders;country=USA;limit=5
/pitch digital agencies
```

---

## 🔌 REST API Included

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| POST   | `/api/hunt`       | Search and store leads |
| GET    | `/api/leads`      | Retrieve list of leads |
| GET    | `/api/export.csv` | Download leads as CSV  |

---

## ☁️ Deploy to Render (FREE)

```
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## ✅ Use Cases

✅ B2B Lead Generation  
✅ LinkedIn Prospecting Automation  
✅ AI Sales Outreach  
✅ Agency Client Finder  
✅ SaaS Founders Prospect Tool  
✅ AI SDR for sales teams

---

## 🛠️ Roadmap

- ✅ AI Outreach Generator
- ✅ LinkedIn Lead Hunter
- 🔜 Email scraper
- 🔜 Web dashboard
- 🔜 CRM (HubSpot/Pipedrive) integration

---

## 👨‍💻 Author

**Serhii Dev** — Python Backend & AI Automation  
📍 Ukraine  
💬 Telegram: https://t.me/softwarjx  
📧 Email: softwarjx1@gmail.com  
⭐ If you like this project – star the repo!

---

## 📜 License

MIT License – free to use and modify.

---

_Built with 🔥 Python + AI + Automation_
