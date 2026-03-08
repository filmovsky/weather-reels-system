import requests
from typing import Dict, Any

class OpenMeteoClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

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
            "current": [
                "temperature_2m",
                "apparent_temperature",
                "precipitation",
                "weather_code",
                "cloud_cover",
                "wind_speed_10m"
            ],
            "timezone": "Europe/Warsaw"
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            json_data = response.json()
            current = json_data.get("current", {})

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

        hook = "Poland today: Spring is here, but still feels fresh!" if temp < 15 else "Warm vibes across Poland today!"

        overview = f"{region}: {temp}°C (feels like {feels}°C), wind {wind} km/h."
        if cloud > 70:
            overview += " Mostly cloudy skies."
        elif cloud < 30:
            overview += " Sunny and clear."
        else:
            overview += " Partly cloudy."

        if precip > 0:
            overview += f" Light precipitation ({precip} mm)."
        else:
            overview += " Dry day ahead."

        outro = "Stay tuned for updates – follow for daily forecasts!"

        return f"[Hook] {hook}\n[Overview] {overview}\n[Outro] {outro}"


# Do testów
if __name__ == "__main__":
    client = OpenMeteoClient()
    for city in ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]:
        weather = client.get_current_weather(city)
        script = client.generate_script(weather)
        print(f"\n=== {city} ===\n{weather}\nTyp rolki: {client.analyze_weather(weather)}\nSkrypt rolki:\n{script}")
