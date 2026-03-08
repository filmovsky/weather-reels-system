def generate_script(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")
    wind = weather.get("wind_speed")

    lines = []

    lines.append(f"Prévisions météo pour la région de {region_name}.")

    if temperature is not None:
        lines.append(f"La température actuelle est d'environ {temperature} degrés.")

    if precipitation and precipitation > 0:
        lines.append("Des précipitations sont possibles.")

    if wind and wind > 30:
        lines.append("Le vent peut être plus fort par endroits.")

    lines.append("Restez connectés pour les dernières mises à jour météo.")

    return " ".join(lines)