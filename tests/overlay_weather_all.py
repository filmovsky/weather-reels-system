from pathlib import Path
from app.video.map_fetcher import fetch_map
from app.video.overlay_weather import overlay_weather_on_map
import time

# Lista regionów do wygenerowania map z pogodą
regions = [
    {"name": "Test Region", "lat": 52.23, "lon": 21.01},
    # dodaj kolejne regiony tutaj
]

timestamp = int(time.time())

for region in regions:
    # Pobierz mapę
    map_file = fetch_map(region["lat"], region["lon"])
    
    # Nałóż dane pogodowe
    final_map_name = f"{region['name'].replace(' ', '_')}_{timestamp}.png"
    final_map = overlay_weather_on_map(map_file, region["name"], output_name=final_map_name)
    
    print(f"Generated overlay map: {final_map}")