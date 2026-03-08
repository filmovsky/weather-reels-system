from app.video.map_fetcher import fetch_map
from app.video.weather_overlay import draw_temperature
from app.weather.open_meteo_client import get_weather

lat = 52.23
lon = 21.01

weather = get_weather(lat, lon)

temperature = weather["current_weather"]["temperature"]

map_file = fetch_map(lat, lon)

result = draw_temperature(map_file, temperature)

print("MAP:", map_file)
print("TEMP MAP:", result)