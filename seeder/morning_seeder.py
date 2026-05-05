# seeder/morning_seeder.py
"""
PulsePro Morning Seeder
- Builds dynamic F&O universe from Fyers instrument master
- Fetches 5-day historical 1m/5m candles
- Seeds Redis with snapshots and volume profiles
"""

import asyncio
import json
from datetime import datetime
from data_feed.fyers_client import get_fyers_client
from core.redis_client import get_redis
from config import FYERS_APP_ID

async def build_universe():
    """Build dynamic F&O universe from Fyers"""
    print("🚀 Starting PulsePro Morning Seeder...")

    redis = await get_redis()
    fyers = await get_fyers_client()

    # Step 1: Get full instrument master from Fyers
    print("Fetching Fyers instrument master...")
    # Fyers API call for instrument master will go here
    # For now we simulate
    universe = ["RELIANCE", "HDFCBANK", "ICICIBANK", "INFY", "TCS"]  # Will be replaced with real dynamic list

    # Step 2: Save dynamic universe to Redis
    await redis.delete("universe:symbols")
    await redis.sadd("universe:symbols", *universe)
    await redis.set("universe:last_updated", datetime.now().isoformat())

    print(f"✅ Dynamic F&O universe built with {len(universe)} symbols")

    # Step 3: Fetch historical candles for each symbol (will be expanded)
    for symbol in universe[:5]:  # limit for testing
        print(f"Fetching historical data for {symbol}")
        # Historical call will be added in next iteration

    await redis.close()
    print("🎉 Morning Seeder completed successfully!")


if __name__ == "__main__":
    asyncio.run(build_universe())
