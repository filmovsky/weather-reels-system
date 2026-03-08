import os
from PIL import Image
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

    def create_base_video(self):
        """
        Tworzy bazowe wideo w formie czarnego tła z określoną długością
        """
        base_video_path = os.path.join(self.output_dir, f"{self.region}_base.mp4")
        command = [
            "ffmpeg",
            "-f", "lavfi",
            "-i", f"color=c=black:s={self.width}x{self.height}:d={self.duration}",
            "-c:v", "libx264",
            "-t", str(self.duration),
            "-pix_fmt", "yuv420p",
            base_video_path
        ]
        import subprocess
        subprocess.run(command, check=True)
        print(f"Base video created at {base_video_path}")
        return base_video_path

    def fetch_weather(self):
        weather = self.weather_client.get_current_weather(self.region)
        print(f"Weather for {self.region}: {weather}")
        return weather

    def generate_overlay(self, weather_data):
        overlay_path = os.path.join(self.output_dir, f"{self.region}_weather_overlay.png")
        add_weather_overlay(weather_data, overlay_path)
        print(f"Weather overlay created at {overlay_path}")
        return overlay_path

    def render_final_video(self):
        base_video = self.create_base_video()
        weather_data = self.fetch_weather()
        overlay_path = self.generate_overlay(weather_data)
        final_video_path = os.path.join(self.output_dir, f"{self.region}_weather_video.mp4")
        self.ffmpeg.add_overlay(base_video, overlay_path, final_video_path)
        print(f"Final video with weather saved at {final_video_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Automated weather video renderer")
    parser.add_argument("--region", type=str, required=True, help="Region name")
    args = parser.parse_args()
    renderer = WeatherVideoAuto(region_name=args.region)
    renderer.render_final_video()