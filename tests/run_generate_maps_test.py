from app.video.generate_weather_maps import generate_weather_series

# Dane testowe
lat, lon = 52.23, 21.01
weather_samples = [
    {'temperature': 5, 'clouds': 20, 'wind': 10},
    {'temperature': 7, 'clouds': 50, 'wind': 12},
    {'temperature': 9, 'clouds': 70, 'wind': 8},
]

generated_maps = generate_weather_series(lat, lon, weather_samples)
for path in generated_maps:
    print(f"Generated map: {path}")