from app.video.renderer import render_video


def run(audio_path: str, output_path: str):

    video = render_video(audio_path, output_path)

    return video


if __name__ == "__main__":

    audio = "storage/audio/test.mp3"
    output = "storage/renders/test.mp4"

    result = run(audio, output)

    print(result)