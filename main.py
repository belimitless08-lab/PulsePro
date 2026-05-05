from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
from dotenv import load_dotenv

load_dotenv()

from core.redis_client import get_redis
from engine.professional_signal_engine import get_professional_engine

app = FastAPI(title="PulsePro - Intraday F&O Signals")

@app.get("/")
async def root():
    return {"message": "PulsePro is running. Go to /dashboard"}

@app.get("/dashboard")
async def dashboard():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws/signals")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Future: broadcast signals here
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
