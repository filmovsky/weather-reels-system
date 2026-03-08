from pydub import AudioSegment


def normalize_audio(input_path: str, output_path: str):

    audio = AudioSegment.from_file(input_path)

    normalized = audio.normalize()

    normalized.export(output_path, format="mp3")

    return output_path