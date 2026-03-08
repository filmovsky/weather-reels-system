import json
from pathlib import Path


def load_voices(language: str):

    path = Path(f"config/voices/voices_{language}.json")

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("voices", [])


def select_voice(language: str):

    voices = load_voices(language)

    if not voices:
        return None

    return voices[0]