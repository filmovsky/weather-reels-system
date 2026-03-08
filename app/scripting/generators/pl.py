def generate_script(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")
    wind = weather.get("wind_speed")

    lines = []

    lines.append(f"Prognoza pogody dla regionu {region_name}.")

    if temperature is not None:
        lines.append(f"Aktualna temperatura wynosi około {temperature} stopni.")

    if precipitation and precipitation > 0:
        lines.append("Możliwe są opady.")

    if wind and wind > 30:
        lines.append("Miejscami może być silniejszy wiatr.")

    lines.append("Sprawdź kolejne aktualizacje pogody.")

    return " ".join(lines)