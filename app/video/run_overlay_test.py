from app.video.map_fetcher import fetch_map
from app.weather.open_meteo_client import get_weather
from app.video.video_pipeline import create_weather_video
from pathlib import Path

# Parametry regionu testowego
region_name = "Test Region"
latitude = 52.23
longitude = 21.01

# Pobranie mapy
map_file = fetch_map(latitude, longitude)

# Pobranie pogody
weather_data = get_weather(latitude, longitude)

# Ścieżka do zapisu wideo testowego
output_path = Path(f"storage/renders/{region_name}_overlay_test.mp4")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Generacja wideo
video_file = create_weather_video(region_name, str(output_path), map_file=map_file, weather_data=weather_data)

print(f"Video generated at: {video_file}")