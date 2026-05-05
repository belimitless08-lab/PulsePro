from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

# Fyers credentials (will be in .env)
FYERS_APP_ID = os.getenv("FYERS_APP_ID")
FYERS_ACCESS_TOKEN = os.getenv("FYERS_ACCESS_TOKEN")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Engine settings
USE_PROFESSIONAL_ENGINE = True
MIN_EXECUTE_SCORE = 72
MIN_WATCHLIST_SCORE = 52

BASE_DIR = Path(__file__).parent
