# data_feed/fyers_client.py
"""
Fyers API Client for PulsePro
Handles login, historical data, live WebSocket
"""

import asyncio
from fyers_apiv3 import fyersModel
from config import FYERS_APP_ID, FYERS_SECRET_KEY
import redis.asyncio as redis

class FyersClient:
    def __init__(self):
        self.fyers = None
        self.access_token = None

    async def initialize(self):
        """Initialize Fyers client"""
        self.fyers = fyersModel.FyersModel(
            client_id=FYERS_APP_ID,
            is_async=True,
            token=FYERS_SECRET_KEY,
            log_path="logs/"
        )
        print("✅ Fyers client initialized")
        return self.fyers

    async def get_historical_candles(self, symbol: str, days: int = 5):
        """Fetch historical 1m candles for seeder"""
        # Will be implemented fully once we test login
        print(f"Fetching historical data for {symbol}")
        return []

    async def subscribe_live(self, symbols: list):
        """Subscribe to live WebSocket"""
        print(f"Subscribing to {len(symbols)} symbols")
        # Full WebSocket implementation in next phase


# Singleton
fyers_client = FyersClient()


async def get_fyers_client():
    await fyers_client.initialize()
    return fyers_client
