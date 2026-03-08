def validate_weather_data(weather: dict):

    if not isinstance(weather, dict):
        return False

    required_fields = [
        "temperature",
        "wind_speed",
        "precipitation"
    ]

    for field in required_fields:
        if field not in weather:
            return False

    return True