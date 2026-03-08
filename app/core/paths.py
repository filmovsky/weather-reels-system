from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_DIR = BASE_DIR / "config"
ASSETS_DIR = BASE_DIR / "assets"
STORAGE_DIR = BASE_DIR / "storage"

WEATHER_RAW_DIR = STORAGE_DIR / "weather_raw"
WEATHER_NORMALIZED_DIR = STORAGE_DIR / "weather_normalized"

SCRIPTS_DIR = STORAGE_DIR / "scripts"
AUDIO_DIR = STORAGE_DIR / "audio"
SUBTITLES_DIR = STORAGE_DIR / "subtitles"

RENDERS_DIR = STORAGE_DIR / "renders"
THUMBNAILS_DIR = STORAGE_DIR / "thumbnails"

PUBLISH_READY_DIR = STORAGE_DIR / "publish_ready"

LOGS_DIR = STORAGE_DIR / "logs"