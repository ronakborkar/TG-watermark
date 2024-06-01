import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    LOG_CHANNEL = os.getenv("LOG_CHANNEL")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL")
    OWNER_ID = int(os.getenv("OWNER_ID"))
    DOWN_PATH = "downloads"
    PRESET = "ultrafast"
