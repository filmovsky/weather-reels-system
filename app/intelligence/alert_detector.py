def detect_alert(weather: dict):

    if not weather:
        return False

    precipitation = weather.get("precipitation", 0)
    wind = weather.get("wind_speed", 0)

    if precipitation and precipitation > 30:
        return True

    if wind and wind > 70:
        return True

    return False