def generate_script(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")
    wind = weather.get("wind_speed")

    lines = []

    lines.append(f"Wettervorhersage für die Region {region_name}.")

    if temperature is not None:
        lines.append(f"Die aktuelle Temperatur liegt bei etwa {temperature} Grad.")

    if precipitation and precipitation > 0:
        lines.append("Es kann zu Niederschlägen kommen.")

    if wind and wind > 30:
        lines.append("Stellenweise kann der Wind stärker sein.")

    lines.append("Bleiben Sie dran für weitere Wetteraktualisierungen.")

    return " ".join(lines)