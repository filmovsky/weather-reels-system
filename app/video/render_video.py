import subprocess
from pathlib import Path


def render_video(audio_path: str, output_path: str):

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=6",
        "-vf",
        "drawtext=text='WEATHER FORECAST':fontcolor=white:fontsize=80:x=(w-text_w)/2:y=400,"
        "drawtext=text='TEST REGION':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=600",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        str(output_file)
    ]

    subprocess.run(command, check=True)

    return str(output_file)