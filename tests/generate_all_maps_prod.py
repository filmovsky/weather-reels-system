from app.video.generate_all_maps import fetch_map
from pathlib import Path

# Regiony i wartości pogodowe
regions = [
    {"name": "Test Region", "lat": 52.23, "lon": 21.01, "temperature": [0, 5, 10, 15]}
]

# Folder docelowy
output_folder = Path("storage/maps")
output_folder.mkdir(parents=True, exist_ok=True)

for region in regions:
    lat = region["lat"]
    lon = region["lon"]
    name = region["name"]
    for temp in region["temperature"]:
        file_path = fetch_map(lat, lon, "temp", temp)
        print(f"Map generated: {file_path}")