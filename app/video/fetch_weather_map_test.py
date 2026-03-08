import os
from app.video.fetch_map import fetch_map  # moduł z repo
from app.core.config import OUTPUT_DIR  # jeśli istnieje, albo ustaw własną ścieżkę

region = "Warsaw,PL"
output_dir = os.path.join("output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"{region}_map.png")

# Pobranie mapy (funkcja z repo)
fetch_map(region_name=region, save_path=output_path)

print(f"Map for {region} saved at {output_path}")