import time
from pathlib import Path
from app.video.map_fetcher import fetch_map

# Lista regionów i współrzędnych (przykład)
regions = [
    {"name": "Warsaw", "lat": 52.23, "lon": 21.01},
    {"name": "Krakow", "lat": 50.0647, "lon": 19.945},
    {"name": "Gdansk", "lat": 54.352, "lon": 18.6466}
]

# Generowanie map dla wszystkich regionów
for region in regions:
    timestamp = int(time.time())
    map_file = fetch_map(region["lat"], region["lon"], zoom=6)
    print(f"Map saved for {region['name']}: {map_file}")