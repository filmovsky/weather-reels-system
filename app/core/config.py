import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_DIR = BASE_DIR / "config"
ASSETS_DIR = BASE_DIR / "assets"
STORAGE_DIR = BASE_DIR / "storage"

VIDEO_STORAGE = STORAGE_DIR / "renders"
AUDIO_STORAGE = STORAGE_DIR / "audio"
SCRIPT_STORAGE = STORAGE_DIR / "scripts"
LOG_STORAGE = STORAGE_DIR / "logs"

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

OPEN_METEO_BASE_URL = os.getenv(
    "OPEN_METEO_BASE_URL",
    "https://api.open-meteo.com/v1"
)