from pathlib import Path
from app.video.map_fetcher import fetch_map
from app.video.overlay_weather import overlay_weather_on_map

# Lista regionów do wygenerowania map z pogodą
regions = [
    {"name": "Test Region", "lat": 52.23, "lon": 21.01},
    # dodaj kolejne regiony tutaj
]

for region in regions:
    # Pobierz mapę
    map_file = fetch_map(region["lat"], region["lon"])
    
    # Nałóż dane pogodowe
    final_map = overlay_weather_on_map(map_file, region["name"])
    
    print(f"Generated overlay map: {final_map}")