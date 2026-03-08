def calculate_confidence(weather: dict):

    if not weather:
        return 0.0

    score = 1.0

    if weather.get("temperature") is None:
        score -= 0.2

    if weather.get("wind_speed") is None:
        score -= 0.2

    if weather.get("precipitation") is None:
        score -= 0.2

    if weather.get("cloud_cover") is None:
        score -= 0.2

    return max(score, 0.0)