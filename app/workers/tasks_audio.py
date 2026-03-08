from app.workers.celery_app import celery_app
from app.audio.elevenlabs_client import generate_voice


@celery_app.task
def generate_audio(script: str, voice_id: str):

    audio = generate_voice(script, voice_id)

    return {
        "script": script,
        "voice_id": voice_id,
        "audio": audio
    }