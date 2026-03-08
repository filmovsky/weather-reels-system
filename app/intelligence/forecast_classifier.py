def classify_forecast(weather: dict):

    if not weather:
        return "standard_forecast"

    precipitation = weather.get("precipitation", 0)
    wind = weather.get("wind_speed", 0)
    temperature = weather.get("temperature")

    if precipitation and precipitation > 20:
        return "weather_alert"

    if wind and wind > 60:
        return "weather_alert"

    if temperature is not None:
        if temperature > 35 or temperature < -15:
            return "extreme_weather"

    return "standard_forecast"