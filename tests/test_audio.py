from app.audio.local_tts import generate_local_voice


def test_local_tts():

    text = "This is a test voice."

    output = "storage/audio/test.mp3"

    result = generate_local_voice(text, output)

    assert result == output

    print("Audio generation test OK")