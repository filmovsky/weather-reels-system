def build_template(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")

    template = {
        "region": region_name,
        "temperature": temperature,
        "precipitation": precipitation
    }

    return template