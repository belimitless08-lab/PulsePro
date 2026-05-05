# PulsePro

Professional Intraday F&O Signal Dashboard  
7-layer quant engine + dynamic F&O universe (Fyers API)

## Tech Stack
- FastAPI + WebSocket
- Fyers API (live + historical + options)
- Redis
- Clean 7-layer signal logic

## Setup
1. Copy `.env.example` → `.env` and fill credentials
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`
