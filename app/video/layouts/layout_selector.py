import json
import random
from pathlib import Path


LAYOUTS_PATH = Path("config/layouts/layouts.json")


def load_layouts():
    with open(LAYOUTS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["layouts"]


def select_layout():

    layouts = load_layouts()

    layout = random.choice(layouts)

    return layout