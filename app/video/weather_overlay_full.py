import os
from app.weather.open_meteo_client import OpenMeteoClient
from app.video.ffmpeg_builder import FFMPEGBuilder
from app.video.overlay_weather import add_weather_overlay

class WeatherVideoRenderer:
    def __init__(self, region_name: str, output_dir: str = "output"):
        self.region = region_name
        self.output_dir = output_dir
        self.weather_client = OpenMeteoClient()
        self.ffmpeg = FFMPEGBuilder()
        os.makedirs(output_dir, exist_ok=True)

    def fetch_weather_data(self):
        weather = self.weather_client.get_current_weather(self.region)
        print(f"Weather data for {self.region}: {weather}")
        return weather

    def generate_weather_overlay(self, weather_data):
        overlay_path = os.path.join(self.output_dir, f"{self.region}_weather_overlay.png")
        add_weather_overlay(weather_data, overlay_path)
        print(f"Overlay saved at: {overlay_path}")
        return overlay_path

    def render_video_with_weather(self, base_video_path: str):
        weather_data = self.fetch_weather_data()
        overlay_path = self.generate_weather_overlay(weather_data)
        output_video_path = os.path.join(self.output_dir, f"{self.region}_weather_video.mp4")
        self.ffmpeg.add_overlay(base_video_path, overlay_path, output_video_path)
        print(f"Final video saved at: {output_video_path}")
        return output_video_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Render video with weather overlay")
    parser.add_argument("--region", type=str, required=True, help="Region for weather")
    parser.add_argument("--video", type=str, required=True, help="Base video path")
    args = parser.parse_args()
    renderer = WeatherVideoRenderer(region_name=args.region)
    renderer.render_video_with_weather(base_video_path=args.video)