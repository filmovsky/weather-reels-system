def select_reel_type(forecast_type: str, alert: bool):

    if alert:
        return "weather_alert"

    if forecast_type == "extreme_weather":
        return "extreme_weather"

    if forecast_type == "weather_change":
        return "weather_change"

    return "standard_forecast"