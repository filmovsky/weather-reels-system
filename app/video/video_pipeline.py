from app.video.layouts.layout_selector import select_layout
from app.video.render_video import render_video
from pathlib import Path
import time


def create_weather_video(region_name: str, output_path: str):

    print("VIDEO PIPELINE START")

    layout = select_layout()
    print(f"LAYOUT: {layout['id']}")

    timestamp = int(time.time())

    output_file = Path(
        f"storage/renders/{region_name}_{layout['id']}_{timestamp}.mp4"
    )

    output_file.parent.mkdir(parents=True, exist_ok=True)

    audio_path = "storage/audio/test_audio.mp3"

    result = render_video(audio_path, str(output_file))

    print(f"VIDEO CREATED: {result}")

    print("VIDEO PIPELINE END")

    return result