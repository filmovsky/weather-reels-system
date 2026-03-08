print("PIPELINE START")

from app.video.video_pipeline import create_weather_video
from pathlib import Path

output_path = Path("storage/renders/Production_Region.mp4")
output_path.parent.mkdir(parents=True, exist_ok=True)

video_file = create_weather_video("Test Region", str(output_path))

print("PIPELINE END")
print(video_file)