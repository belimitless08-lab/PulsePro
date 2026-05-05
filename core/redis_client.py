import redis.asyncio as redis
from config import REDIS_URL
import asyncio

async def get_redis():
    """Returns async Redis client"""
    client = redis.from_url(REDIS_URL, decode_responses=True)
    return client

# For testing
async def test_redis():
    client = await get_redis()
    await client.ping()
    print("✅ Redis connection successful")
    await client.close()

if __name__ == "__main__":
    asyncio.run(test_redis())
