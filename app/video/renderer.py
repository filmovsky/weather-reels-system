import os
from moviepy.editor import ImageSequenceClip

ASSETS_MAPS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/maps")
ASSETS_REELS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/reels")
os.makedirs(ASSETS_REELS_DIR, exist_ok=True)

def create_reel_from_maps():
    images = []
    for file in sorted(os.listdir(ASSETS_MAPS_DIR)):
        if file.endswith(".png"):
            images.append(os.path.join(ASSETS_MAPS_DIR, file))

    if not images:
        raise FileNotFoundError("Nie znaleziono map PNG do wygenerowania rolki")

    clip = ImageSequenceClip(images, fps=2)
    output_file = os.path.join(ASSETS_REELS_DIR, "weather_reel.mp4")
    clip.write_videofile(output_file)
    print(f"Rolka pogodowa wygenerowana: {output_file}")

if __name__ == "__main__":
    create_reel_from_maps()