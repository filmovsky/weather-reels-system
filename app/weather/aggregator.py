from app.weather.providers.open_meteo import get_forecast as get_open_meteo
from app.weather.providers.gfs import get_gfs_forecast as get_gfs
from app.weather.providers.ecmwf import get_ecmwf_forecast as get_ecmwf
from app.weather.providers.icon import get_icon_forecast as get_icon

def aggregate_weather_data(*providers):
    result = {}
    for provider in providers:
        if not provider:
            continue
        for key, value in provider.items():
            if value is not None:
                result[key] = value
    return result

def fetch_weather_for_region(region):
    lat = region["lat"]
    lon = region["lon"]
    open_meteo_data = get_open_meteo(lat, lon)
    gfs_data = get_gfs(lat, lon)
    ecmwf_data = get_ecmwf(lat, lon)
    icon_data = get_icon(lat, lon)
    weather = aggregate_weather_data(open_meteo_data, gfs_data, ecmwf_data, icon_data)
    return weather