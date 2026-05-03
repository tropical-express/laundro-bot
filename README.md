# 🧺 LaundroBot

![License](https://img.shields.io/github/license/tropical-express/laundro-bot)
![Last Commit](https://img.shields.io/github/last-commit/tropical-express/laundro-bot)
![Repo Size](https://img.shields.io/github/repo-size/tropical-express/laundro-bot)
![Stars](https://img.shields.io/github/stars/tropical-express/laundro-bot)
![Uptime](https://img.shields.io/uptimerobot/status/mXXXXXXXXX)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![Environment](https://img.shields.io/badge/Config-.env-yellow)
![Automation](https://img.shields.io/badge/Automation-n8n-orange)
![Data Source](https://img.shields.io/badge/Data-OpenStreetMap-green)

A data pipeline for discovering laundromats using OpenStreetMap, storing results locally, and automating workflows with n8n.

---

## 🚀 Features

* 🌍 Scrapes laundromat data from OpenStreetMap (Overpass API)
* 🗄️ Stores structured data in a SQLite database
* ⚙️ Integrates with n8n for automation & workflows
* 📊 Optional dashboard for viewing collected data
* 🚦 Configurable request limits to avoid API timeouts

---

## 🧱 Tech Stack

* Node.js
* SQLite
* n8n (workflow automation)
* Overpass API (OpenStreetMap)

---

## 📦 Installation

```bash
git clone https://github.com/tropical-express/laundro-bot
cd laundro-bot
pnpm install
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Then configure:

```env
# 🌍 Overpass API
OVERPASS_URL=https://overpass-api.de/api/interpreter

# 🗄️ Database
DB_PATH=./data/laundromats.db

# ⚙️ n8n
N8N_HOST=localhost
N8N_PORT=5678
N8N_PROTOCOL=http
WEBHOOK_URL=http://localhost:5678/webhook/your-endpoint

# 📊 Dashboard
DASHBOARD_PORT=5000

# 🚦 Optional
REQUEST_DELAY_MS=2000
MAX_CONCURRENT_REQUESTS=2
OVERPASS_TIMEOUT=30000
```

---

## ▶️ Usage

Start the scraper:

```bash
pnpm start
```

What happens:

1. Fetches laundromat data from OpenStreetMap
2. Processes and cleans the data
3. Stores results in SQLite
4. (Optional) Triggers n8n workflows via webhook

---

## 🔗 n8n Integration

Make sure n8n is running:

```bash
npx n8n
```

Example webhook format:

```text
http://localhost:5678/webhook/laundromat-update
```

You can use this to:

* Send alerts
* Sync data
* Trigger automations

---

## 📊 Dashboard (Optional)

If your project includes a dashboard:

```bash
pnpm run dashboard
```

Then open:

```text
http://localhost:5000
```

---

## 🗂️ Project Structure

```text
laundro-bot/
├── data/            # SQLite database
├── scraper/         # OSM scraping logic
├── dashboard/       # UI (if included)
├── workflows/       # n8n workflows (optional)
├── .env.example
├── package.json
└── README.md
```

---

## ⚠️ Notes

* The Overpass API is rate-limited — avoid spamming requests
* Use delays (`REQUEST_DELAY_MS`) to prevent timeouts
* For large queries, split requests into smaller batches

---

## 🛠️ Troubleshooting

**Timeout errors from Overpass API**

* Increase `OVERPASS_TIMEOUT`
* Reduce request size
* Add delays between requests

**Database not found**

* Ensure `/data` folder exists

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Future Improvements

* Add cloud deployment (Vercel / VPS)
* Improve dashboard UI
* Add data export (CSV / API)
* Schedule automated scraping

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## ⭐ Support

If you find this useful, consider starring the repo!
