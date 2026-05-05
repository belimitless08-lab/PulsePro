from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import asyncio
from dotenv import load_dotenv

load_dotenv()

from core.redis_client import get_redis
from engine.professional_signal_engine import get_professional_engine

app = FastAPI(title="PulsePro - Intraday F&O Signals")

@app.get("/")
async def root():
    return {"status": "PulsePro is running 🚀", "dashboard": "/dashboard"}

@app.get("/dashboard")
async def dashboard():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/test-engine")
async def test_engine():
    """Test the new 7-layer professional engine"""
    redis = await get_redis()
    engine = await get_professional_engine(redis)
    
    # Test data
    snapshot = {"ltp": 1685.0, "choppiness": 38.0, "avg_volume_5d": 120000}
    current_5m = {"timestamp": "2026-05-05T09:25:00", "volume": 85000}
    
    signal = await engine.generate_signal(
        symbol="HDFCBANK",
        snapshot=snapshot,
        current_5m=current_5m,
        five_day_candles=[],
        nifty_snapshot={},
        options_data=None
    )
    
    await redis.close()
    return signal if signal else {"message": "No signal generated"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
