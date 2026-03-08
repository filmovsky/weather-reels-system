from app.video.map_fetcher import fetch_map

# Dane dla testowego regionu
latitude = 52.23
longitude = 21.01

# Pobranie mapy z wszystkimi warstwami
map_files = fetch_map(latitude, longitude)

# Wyświetlenie wyników
for f in map_files:
    print(f"Map generated: {f}")