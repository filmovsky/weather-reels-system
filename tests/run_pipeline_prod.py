from app.video.video_pipeline import create_weather_video
from pathlib import Path

# Lista regionów do wygenerowania wideo
regions = [
    {"name": "Test Region", "lat": 52.23, "lon": 21.01},
    # dodaj kolejne regiony tutaj
]

for region in regions:
    # Ścieżka do zapisu wideo
    output_path = Path(f"storage/renders/{region['name'].replace(' ', '_')}_video.mp4")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Generacja wideo dla regionu
    video_file = create_weather_video(region['name'], str(output_path))
    
    print(f"Video generated at: {video_file}")