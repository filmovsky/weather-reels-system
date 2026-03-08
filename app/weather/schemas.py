from typing import Optional
from pydantic import BaseModel


class WeatherData(BaseModel):
    temperature: Optional[float]
    temperature_min: Optional[float]
    temperature_max: Optional[float]

    precipitation: Optional[float]

    wind_speed: Optional[float]

    cloud_cover: Optional[float]