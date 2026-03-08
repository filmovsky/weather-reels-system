import os
import datetime
from app.weather.open_meteo_client import OpenMeteoClient
from app.video.overlay_weather import add_weather_overlay
from app.video.ffmpeg_builder import FFMPEGBuilder

class WeatherVideoAuto:
    def __init__(self, region_name: str, output_dir: str = "output", width=1280, height=720, duration=5):
        self.region = region_name
        self.output_dir = output_dir
        self.width = width
        self.height = height
        self.duration = duration  # długość wideo w sekundach
        self.weather_client = OpenMeteoClient()
        self.ffmpeg = FFMPEGBuilder()
        os.makedirs(output_dir, exist_ok=True)

    def render_final_video(self):
        # Generowanie unikalnego timestampu dla nazw plików
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_video = os.path.join(self.output_dir, f"{self.region}_base_{timestamp}.mp4")
        overlay_path = os.path.join(self.output_dir, f"{self.region}_weather_overlay_{timestamp}.png")
        final_video_path = os.path.join(self.output_dir, f"{self.region}_weather_video_{timestamp}.mp4")

        # 1️⃣ Tworzenie bazowego wideo (czarne tło)
        import subprocess
        command = [
            "ffmpeg",
            "-f", "lavfi",
            "-i", f"color=c=black:s={self.width}x{self.height}:d={self.duration}",
            "-c:v", "libx264",
            "-t", str(self.duration),
            "-pix_fmt", "yuv420p",
            base_video
        ]
        subprocess.run(command, check=True)
        print(f"Base video created at {base_video}")

        # 2️⃣ Pobranie danych pogodowych
        weather_data = self.weather_client.get_current_weather(self.region)
        print(f"Weather for {self.region}: {weather_data}")

        # 3️⃣ Generowanie overlay pogodowego
        add_weather_overlay(weather_data, overlay_path)
        print(f"Weather overlay created at {overlay_path}")

        # 4️⃣ Nakładanie overlay na wideo
        self.ffmpeg.add_overlay(base_video, overlay_path, final_video_path)
        print(f"Final video with weather saved at {final_video_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Automated weather video renderer")
    parser.add_argument("--region", type=str, required=True, help="Region name")
    args = parser.parse_args()

    renderer = WeatherVideoAuto(region_name=args.region)
    renderer.render_final_video()