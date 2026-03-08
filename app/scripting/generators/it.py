def generate_script(region_name: str, weather: dict):

    temperature = weather.get("temperature")
    precipitation = weather.get("precipitation")
    wind = weather.get("wind_speed")

    lines = []

    lines.append(f"Previsioni meteo per la regione di {region_name}.")

    if temperature is not None:
        lines.append(f"La temperatura attuale è di circa {temperature} gradi.")

    if precipitation and precipitation > 0:
        lines.append("Sono possibili precipitazioni.")

    if wind and wind > 30:
        lines.append("In alcune zone il vento potrebbe essere più forte.")

    lines.append("Segui i prossimi aggiornamenti meteo.")

    return " ".join(lines)