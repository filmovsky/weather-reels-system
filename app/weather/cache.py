import time

_weather_cache = {}


def set_cache(key: str, data: dict, ttl: int = 1800):
    _weather_cache[key] = {
        "data": data,
        "expires": time.time() + ttl
    }


def get_cache(key: str):
    item = _weather_cache.get(key)

    if not item:
        return None

    if item["expires"] < time.time():
        del _weather_cache[key]
        return None

    return item["data"]