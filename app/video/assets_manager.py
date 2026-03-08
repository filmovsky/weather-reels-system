from pathlib import Path


ASSETS_DIR = Path("assets")


def get_asset_path(name: str):

    path = ASSETS_DIR / name

    if not path.exists():
        raise FileNotFoundError(f"Asset not found: {name}")

    return path