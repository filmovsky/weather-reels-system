import json
from pathlib import Path


LAYOUT_FILE = Path("config/layouts/layouts.json")


def load_layouts():

    with open(LAYOUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["layouts"]


def select_random_layout():

    layouts = load_layouts()

    active_layouts = [l for l in layouts if l["active"]]

    if not active_layouts:
        raise Exception("No active layouts")

    import random

    return random.choice(active_layouts)