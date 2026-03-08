import requests
from app.core.config import OPEN_METEO_BASE_URL


def get_forecast(latitude: float, longitude: float):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,cloudcover,windspeed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto"
    }

    response = requests.get(OPEN_METEO_BASE_URL + "/forecast", params=params)

    if response.status_code != 200:
        raise Exception("Weather API error")

    return response.json()