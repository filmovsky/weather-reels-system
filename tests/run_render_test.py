from app.video.video_pipeline import create_weather_video
from pathlib import Path

# Ścieżka do zapisu testowego wideo
output_path = Path("storage/renders/Test_Region_test.mp4")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Generacja wideo dla testowego regionu
video_file = create_weather_video("Test Region", str(output_path))
print(f"Video generated at: {video_file}")