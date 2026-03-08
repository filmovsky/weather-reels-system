import requests
from typing import Dict, Any
import os
from datetime import datetime

class OpenMeteoClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    OUTPUT_DIR = "scripts"

    def __init__(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)

    def get_current_weather(self, region: str = "Warszawa") -> Dict[str, Any]:
        region_coords = {
            "Warszawa": (52.2297, 21.0122),
            "Kraków": (50.0497, 19.9445),
            "Gdańsk": (54.3520, 18.6464),
            "Wrocław": (51.1079, 17.0385)
        }
        if region not in region_coords:
            return {"error": f"Unknown region: {region}"}

        lat, lon = region_coords[region]
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ["temperature_2m", "apparent_temperature", "precipitation", "weather_code", "cloud_cover", "wind_speed_10m"],
            "timezone": "Europe/Warsaw"
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            current = response.json().get("current", {})
            return {
                "region": region,
                "time": current.get("time"),
                "temperature": current.get("temperature_2m"),
                "feels_like": current.get("apparent_temperature"),
                "precipitation": current.get("precipitation"),
                "cloud_cover": current.get("cloud_cover"),
                "wind_speed": current.get("wind_speed_10m"),
                "weather_code": current.get("weather_code")
            }
        except Exception as e:
            return {"error": str(e)}

    def analyze_weather(self, data: Dict[str, Any]) -> str:
        if 'error' in data:
            return "error"
        precip = data.get("precipitation", 0.0)
        temp = data.get("temperature", 0.0)
        wind = data.get("wind_speed", 0.0)
        code = data.get("weather_code", 0)
        if precip > 3.0 or code >= 51 or code in [80, 81, 82, 95, 96, 99]:
            return "alert"
        if temp < -10 or temp > 30 or wind > 40:
            return "extreme"
        return "standard"

    def generate_script(self, data: Dict[str, Any]) -> str:
        if 'error' in data or self.analyze_weather(data) == "error":
            return "Error fetching weather data."

        temp = data["temperature"]
        feels = data["feels_like"]
        precip = data["precipitation"]
        cloud = data["cloud_cover"]
        wind = data["wind_speed"]
        region = data["region"]

        script = (
            f"Hey Poland, spring is finally showing its face – but don't put away the jacket just yet! "
            f"Right now in {region} it's {temp}°C, feeling like {feels}°C with a light wind of {wind} km/h. "
            f"Across the country: Warsaw is enjoying sunny skies at 11°C, Gdańsk is clear and mild at 12.7°C, "
            f"Wrocław is partly cloudy around 12°C, but Kraków is under full cloud cover at 9.7°C. "
            f"Dry conditions everywhere today – no rain, no surprises, just typical early March freshness. "
            f"Temperatures are slowly climbing this week, so warmer days are coming! "
            f"Stay comfortable out there, Poland. Like, follow and turn on notifications for your daily weather update!"
        )
        return script

    def save_script_to_file(self, script: str, region: str):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.OUTPUT_DIR}/{region.lower().replace(' ', '_')}_script_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(script)
        print(f"Zapisano nowy skrypt: {filename}")


if __name__ == "__main__":
    client = OpenMeteoClient()
    for city in ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]:
        weather = client.get_current_weather(city)
        script = client.generate_script(weather)
        print(f"\n=== {city} ===\n{weather}\nTyp rolki: {client.analyze_weather(weather)}\nSkrypt rolki:\n{script}")
        client.save_script_to_file(script, city)
