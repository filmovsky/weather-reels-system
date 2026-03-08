import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cv2
import json
import subprocess

# --- Funkcja generująca mapę lokalnie przez Stable Diffusion ---
def generate_local_map(region_name, output_dir="storage/maps/"):
    timestamp = int(time.time())
    output_path = Path(output_dir) / f"{region_name.replace(' ', '_')}_{timestamp}.png"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Wywołanie Stable Diffusion lokalnie (przykład, zastąp rzeczywistym wywołaniem SD)
    prompt = f"High quality map of {region_name}, realistic, topographic, professional style"
    # subprocess.run(["python", "stable_diffusion_script.py", "--prompt", prompt, "--output", str(output_path)])
    
    # Placeholder: pusty obraz dla testu
    img = Image.new("RGB", (1080, 1920), color=(150, 200, 255))
    img.save(output_path)

    return str(output_path)

# --- Funkcja pobierająca pogodę ---
def get_weather(lat, lon):
    import requests
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,cloudcover_10m,windspeed_10m,precipitation"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    current = data['current_weather']
    return {
        'temperature': current['temperature'],
        'windspeed': current['windspeed'],
        'cloudcover': current.get('cloudcover', 0),
        'precipitation': current.get('precipitation', 0)
    }

# --- Funkcja nakładania pogody na mapę ---
def overlay_weather(map_file, weather_data, region_name):
    img = Image.open(map_file).convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw.text((50, 50), f"Temp: {weather_data['temperature']}°C", font=font, fill=(255,0,0,255))
    draw.text((50, 120), f"Wind: {weather_data['windspeed']} km/h", font=font, fill=(0,255,0,255))
    draw.text((50, 190), f"Clouds: {weather_data['cloudcover']}%", font=font, fill=(255,255,255,255))
    draw.text((50, 260), f"Precipitation: {weather_data['precipitation']} mm", font=font, fill=(0,0,255,255))

    output_dir = Path("storage/renders/")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{region_name.replace(' ', '_')}_overlay_{int(time.time())}.png"
    img.save(output_path)
    return str(output_path)

# --- Funkcja generująca wideo ---
def create_video(image_files, output_file="storage/renders/solec_weather_video.mp4"):
    frames = [cv2.imread(f) for f in image_files]
    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, 1, (width, height))
    for frame in frames:
        video.write(frame)
    video.release()
    return output_file

# --- Główna sekwencja ---
region_name = "Solec Kujawski"
lat, lon = 52.623, 18.015

map_file = generate_local_map(region_name)
weather = get_weather(lat, lon)
overlay_file = overlay_weather(map_file, weather, region_name)
video_file = create_video([overlay_file])

print(f"Video generated: {video_file}")