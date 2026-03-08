import requests

class OpenMeteoClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, region: str):
        lat, lon = 52.2297, 21.0122  # Warszawa - na początek można zamienić na mapping region->coords
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        current = data.get("current_weather", {})
        return {
            "temp": current.get("temperature"),
            "description": f"Wind {current.get('windspeed', 0)} km/h",
            "icon": None
        }