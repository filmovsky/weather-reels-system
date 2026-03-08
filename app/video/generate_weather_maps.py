from map_fetcher import fetch_map
from overlay_weather import overlay_weather
import time

def generate_weather_series(lat, lon, weather_data_list, zoom=6):
    """
    Generuje serię map z nakładką pogodową.
    
    lat, lon: współrzędne regionu
    weather_data_list: lista słowników {'temperature': int, 'clouds': int, 'wind': int}
    zoom: zoom mapy
    """
    map_paths = []
    
    for idx, weather in enumerate(weather_data_list):
        map_path = fetch_map(lat, lon, zoom)
        overlay_path = overlay_weather(
            map_path,
            temperature=weather.get('temperature'),
            clouds=weather.get('clouds'),
            wind=weather.get('wind')
        )
        map_paths.append(overlay_path)
        time.sleep(1)  # uniknięcie limitów serwera map
        
    return map_paths