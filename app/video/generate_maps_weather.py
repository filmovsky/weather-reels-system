import os
import requests
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip

# Katalogi systemowe
MAPS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/maps")
REELS_DIR = os.path.join(os.path.dirname(__file__), "../../assets/reels")
os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(REELS_DIR, exist_ok=True)

# Lista regionów – możesz dodać wszystkie regiony produkcyjne
regions = [
    {"name": "Warszawa", "lat": 52.2297, "lon": 21.0122},
    {"name": "Kraków", "lat": 50.0647, "lon": 19.9450},
    {"name": "Gdańsk", "lat": 54.3520, "lon": 18.6466},
]

# API do pobierania pogody (przykład OpenWeatherMap)
API_KEY = "TU_WSTAW_SWÓJ_KLUCZ_API"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(region):
    """Pobiera aktualną pogodę dla regionu"""
    params = {"lat": region["lat"], "lon": region["lon"], "appid": API_KEY, "units": "metric"}
    response = requests.get(API_URL, params=params)
    if response.status_code != 200:
        print(f"Nie udało się pobrać pogody dla {region['name']}")
        return None
    data = response.json()
    weather_info = {
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    }
    return weather_info

def generate_map_png(region, weather):
    """Tworzy mapę PNG z naniesioną pogodą"""
    img_path = os.path.join(MAPS_DIR, f"{region['name'].lower()}.png")
    img = Image.new("RGB", (1280, 720), color=(73, 109, 137))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    text = f"{region['name']}\n{weather['temp']}°C, {weather['desc']}"
    draw.multiline_text((640, 360), text, fill=(255, 255, 0), font=font, anchor="mm", align="center")
    img.save(img_path)
    print(f"Mapa PNG gotowa: {img_path}")
    return img_path

def create_reel():
    images = []
    for region in regions:
        weather = fetch_weather(region)
        if weather:
            png = generate_map_png(region, weather)
            images.append(png)
    if not images:
        raise FileNotFoundError("Nie wygenerowano żadnych map PNG")
    clip = ImageSequenceClip(images, fps=2)
    output_file = os.path.join(REELS_DIR, "weather_reel.mp4")
    clip.write_videofile(output_file)
    print(f"Rolka pogodowa wygenerowana: {output_file}")

if __name__ == "__main__":
    create_reel()