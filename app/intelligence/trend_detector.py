def detect_trend(current_weather: dict, previous_weather: dict):

    if not current_weather or not previous_weather:
        return "stable"

    current_temp = current_weather.get("temperature")
    previous_temp = previous_weather.get("temperature")

    if current_temp is None or previous_temp is None:
        return "stable"

    difference = current_temp - previous_temp

    if difference > 5:
        return "warming"

    if difference < -5:
        return "cooling"

    return "stable"