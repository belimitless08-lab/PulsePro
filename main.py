from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
from dotenv import load_dotenv

load_dotenv()

from core.redis_client import get_redis

app = FastAPI(title="PulsePro - Intraday F&O Signals")

# Mount frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    return {"message": "PulsePro is running 🚀"}

@app.get("/dashboard")
async def dashboard():
    """Main dashboard page"""
    with open("frontend/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(html_content)

@app.websocket("/ws/signals")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time signals"""
    await websocket.accept()
    print("✅ Client connected to /ws/signals")
    try:
        while True:
            # Later we will broadcast real signals here
            await asyncio.sleep(1)
    except Exception:
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
