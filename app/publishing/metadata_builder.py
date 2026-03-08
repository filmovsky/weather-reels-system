def build_metadata(region_name: str):

    title = f"Prognoza pogody dla {region_name}"

    description = (
        f"Najnowsza prognoza pogody dla regionu {region_name}. "
        "Sprawdź temperaturę, opady i wiatr."
    )

    hashtags = [
        "#pogoda",
        "#prognozapogody",
        "#weather",
        "#forecast"
    ]

    return {
        "title": title,
        "description": description,
        "hashtags": hashtags
    }