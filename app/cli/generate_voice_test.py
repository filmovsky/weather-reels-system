from app.audio.elevenlabs_tts import generate_voice

def generate_audio(region_id, voice_id="voice_1"):
    audio_path = generate_voice(region_id, None, voice_id=voice_id)
    print(f"Audio generated at: {audio_path}")
    return audio_path

if __name__ == "__main__":
    test_region = "warszawa"
    generate_audio(test_region)