# 🌦️ AI-Powered Weather Agent (Backend-Only)

Stateless Flask API that answers natural-language weather questions using Open‑Meteo and a Gemini-powered ReAct agent. Ready for one-shot calls and deployment on Render.

## Endpoints

- POST /weather
  - body: { "query": "Will it rain in Dhaka tomorrow?" }
  - resp: { "response": "...", "sentiment": 0.0 }
- GET /health → { "status": "healthy" }

## Local run

```bash
pip install -r requirements.txt
set GEMINI_API_KEY=your_key_here
python app.py
# http://localhost:5000/health
```

## Deploy to Render

This repo includes render.yaml.

1) Push to GitHub.
2) On render.com → New → Web Service → Connect the repo.
3) Environment
   - GEMINI_API_KEY: your Gemini API key
4) Render will build with requirements.txt and start with Gunicorn.

Notes
- No database is used. Each /weather call is independent.
- Keep GEMINI_API_KEY secret (set it in Render Dashboard).
- The service binds to PORT provided by Render.
