import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cv2
from diffusers import StableDiffusionPipeline
import torch
import requests

def generate_map(prompt: str, output_file: str):
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")
    image = pipe(prompt, height=1080, width=1920).images[0]
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    image.save(output_file)
    return output_file

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,cloudcover_10m,windspeed_10m,precipitation"
    r = requests.get(url)
    r.raise_for_status()
    current = r.json()['current_weather']
    return {
        'temperature': current['temperature'],
        'windspeed': current['windspeed'],
        'cloudcover': current.get('cloudcover', 0),
        'precipitation': current.get('precipitation', 0)
    }

def overlay_weather(map_file, weather_data):
    img = Image.open(map_file).convert("RGBA")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 50), f"Temp: {weather_data['temperature']}°C", font=font, fill=(255,0,0,255))
    draw.text((50, 120), f"Wind: {weather_data['windspeed']} km/h", font=font, fill=(0,255,0,255))
    draw.text((50, 190), f"Clouds: {weather_data['cloudcover']}%", font=font, fill=(255,255,255,255))
    draw.text((50, 260), f"Precipitation: {weather_data['precipitation']} mm", font=font, fill=(0,0,255,255))
    output_dir = Path("storage/renders/")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"solec_overlay_{int(time.time())}.png"
    img.save(output_file)
    return str(output_file)

def create_video(image_files, output_file="storage/renders/solec_weather_full.mp4"):
    frames = [cv2.imread(f) for f in image_files]
    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, 1, (width, height))
    for frame in frames:
        video.write(frame)
    video.release()
    return output_file

lat, lon = 52.623, 18.015
map_file = "storage/maps/solec_kujawski_generated.png"
prompt = "A highly detailed digital map of Solec-Kujawski, Poland, professional style, 4k, realistic terrain and city layout"
generate_map(prompt, map_file)
weather = get_weather(lat, lon)
overlay_file = overlay_weather(map_file, weather)
video_file = create_video([overlay_file])
print(f"Video wygenerowane: {video_file}")