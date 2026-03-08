from PIL import Image, ImageDraw

width = 1080
height = 1920

img = Image.new("RGB", (width, height), "#0a1a2f")
draw = ImageDraw.Draw(img)

for y in range(height):
    r = int(10 + y * 0.02)
    g = int(26 + y * 0.03)
    b = int(47 + y * 0.05)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

img.save("assets/backgrounds/weather_bg.png")

print("Background generated")