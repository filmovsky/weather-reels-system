# Lokalizacja: app/tts/elevenlabs_tts.py

import os
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

API_KEY = "sk_d5de5199b0f74a7c4ad450f2c7b5d8ea4ffb560aea820899"
VOICE_ID = "o2xdfKUpc1Bwq7RchZuW"  # Piotr

client = ElevenLabs(api_key=API_KEY)

def generate_voice(region_id: str, text: str, output_path: str = None):
    if output_path is None:
        output_path = f"audio_{region_id}.mp3"

    audio_chunks = client.text_to_speech.convert(
        text=text,
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
        voice_settings=VoiceSettings()
    )

    with open(output_path, "wb") as f:
        for chunk in audio_chunks:
            if chunk:
                f.write(chunk)

    return output_path