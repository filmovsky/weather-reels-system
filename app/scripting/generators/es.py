def generate_script(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")
    wind = weather.get("wind_speed")

    lines = []

    lines.append(f"Pronóstico del tiempo para la región de {region_name}.")

    if temperature is not None:
        lines.append(f"La temperatura actual es de aproximadamente {temperature} grados.")

    if precipitation and precipitation > 0:
        lines.append("Puede haber precipitaciones.")

    if wind and wind > 30:
        lines.append("En algunas zonas el viento puede ser más fuerte.")

    lines.append("Mantente atento a las próximas actualizaciones del tiempo.")

    return " ".join(lines)