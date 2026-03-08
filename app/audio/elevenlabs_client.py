from elevenlabs import generate, set_api_key
from app.core.config import ELEVENLABS_API_KEY


set_api_key(ELEVENLABS_API_KEY)


def generate_voice(text: str, voice_id: str):

    audio = generate(
        text=text,
        voice=voice_id,
        model="eleven_multilingual_v2"
    )

    return audio