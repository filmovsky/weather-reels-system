import subprocess
from pathlib import Path
import time


def render_video(audio_path: str, output_path: str):

    base = Path(output_path)
    base.parent.mkdir(parents=True, exist_ok=True)

    timestamp = int(time.time())
    output_file = base.parent / f"{base.stem}_{timestamp}.mp4"

    text_filter = (
        "drawtext=text='WEATHER FORECAST':fontcolor=white:fontsize=90:x=(w-text_w)/2:y=300,"
        "drawtext=text='TEST REGION':fontcolor=white:fontsize=70:x=(w-text_w)/2:y=500,"
        "drawtext=text='TEMPERATURE 15C':fontcolor=yellow:fontsize=140:x=(w-text_w)/2:y=850,"
        "drawtext=text='WIND 12 KM/H':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=1050,"
        "drawtext=text='CLOUDS 40%%':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=1150"
    )

    command = [
        "ffmpeg",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=6",
        "-vf", text_filter,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        str(output_file)
    ]

    subprocess.run(command, check=True)

    return str(output_file)