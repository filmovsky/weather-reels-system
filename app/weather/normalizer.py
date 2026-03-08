def normalize_weather_data(provider_data: dict):

    if not provider_data:
        return None

    normalized = {
        "temperature": None,
        "temperature_min": None,
        "temperature_max": None,
        "precipitation": None,
        "wind_speed": None,
        "cloud_cover": None
    }

    try:
        current = provider_data.get("current_weather", {})

        normalized["temperature"] = current.get("temperature")
        normalized["wind_speed"] = current.get("windspeed")

        daily = provider_data.get("daily", {})

        if "temperature_2m_min" in daily:
            normalized["temperature_min"] = daily["temperature_2m_min"][0]

        if "temperature_2m_max" in daily:
            normalized["temperature_max"] = daily["temperature_2m_max"][0]

        if "precipitation_sum" in daily:
            normalized["precipitation"] = daily["precipitation_sum"][0]

    except Exception:
        return None

    return normalized