import requests
from pathlib import Path
import time

def fetch_map(lat, lon, zoom=6):
    timestamp = int(time.time())
    url = f"https://staticmap.openstreetmap.de/staticmap.php?center={lat},{lon}&zoom={zoom}&size=1080x1920"
    
    output = Path(f"storage/maps/map_{lat}_{lon}_{timestamp}.png")
    output.parent.mkdir(parents=True, exist_ok=True)

    r = requests.get(url)
    with open(output, "wb") as f:
        f.write(r.content)
    
    return str(output)