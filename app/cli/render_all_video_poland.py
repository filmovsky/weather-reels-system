import json
from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.video.video_pipeline import render_video_pipeline

def render_video_for_all_poland():
    with open("weather-reels-system/config/regions/regions_poland.json", "r", encoding="utf-8") as f:
        regions = json.load(f)
    for region_id in regions.keys():
        weather_data = fetch_weather_for_region(region_id)
        forecast_type = classify_forecast(weather_data)
        audio_path = f"weather-reels-system/output/voice_{region_id}.wav"
        video_path = render_video_pipeline(region_id, audio_path, weather_data, forecast_type)
        print(f"{region_id} -> Video generated: {video_path}")

if __name__ == "__main__":
    render_video_for_all_poland()