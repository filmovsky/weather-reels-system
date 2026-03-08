import requests
from typing import Dict, Any

class OpenMeteoClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, region: str = "Warszawa") -> Dict[str, Any]:
        # Mapowanie regionów → koordynaty (można rozszerzyć o więcej miast/województw)
        region_coords = {
            "Warszawa": (52.2297, 21.0122),
            "Kraków": (50.0497, 19.9445),
            "Gdańsk": (54.3520, 18.6464),
            "Wrocław": (51.1079, 17.0385)
        }

        if region not in region_coords:
            return {"error": f"Nieznany region: {region}"}

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
        """Prosta analiza pogody - zwraca typ rolki: standard / alert / extreme"""
        if 'error' in data:
            return "error"

        precip = data.get("precipitation", 0.0)
        temp = data.get("temperature", 0.0)
        wind = data.get("wind_speed", 0.0)
        code = data.get("weather_code", 0)

        # Alert: deszcz/śnieg/grad/burza
        if precip > 3.0 or code >= 51 or code in [80, 81, 82, 95, 96, 99]:
            return "alert"

        # Extreme: bardzo zimno/ciepło, silny wiatr
        if temp < -10 or temp > 30 or wind > 40:
            return "extreme"

        # Standard: reszta przypadków (sucho, normalne warunki)
        return "standard"


# Do testów – uruchom plik bezpośrednio
if __name__ == "__main__":
    client = OpenMeteoClient()
    for city in ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]:
        weather = client.get_current_weather(city)
        analysis = client.analyze_weather(weather)
        print(f"\n{city}:")
        print(weather)
        print(f"Typ rolki: {analysis}")
