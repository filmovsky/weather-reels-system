import json
from pathlib import Path


def load_regions():

    path = Path("config/regions/regions_global.json")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("regions", [])


def run():

    regions = load_regions()

    print(f"Loaded {len(regions)} regions")

    for r in regions:
        print(r["name"], r["country"])


if __name__ == "__main__":
    run()
