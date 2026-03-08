from PIL import Image, ImageDraw, ImageFont

def add_weather_overlay(weather_data: dict, overlay_path: str):
    img = Image.new('RGBA', (800, 200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    temp_text = f"{weather_data.get('temp', '--')}°C"
    desc_text = weather_data.get('description', 'Unknown')

    draw.text((10, 10), temp_text, fill="white", font=font)
    draw.text((10, 40), desc_text, fill="white", font=font)

    icon_path = weather_data.get('icon')
    if icon_path:
        icon = Image.open(icon_path).convert("RGBA")
        img.paste(icon, (200, 10), icon)

    img.save(overlay_path)