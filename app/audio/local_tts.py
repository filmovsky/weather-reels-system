import pyttsx3


def generate_local_voice(text: str, output_path: str):

    engine = pyttsx3.init()

    engine.save_to_file(text, output_path)

    engine.runAndWait()

    return output_path