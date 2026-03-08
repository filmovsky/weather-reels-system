from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.video.video_pipeline import render_video_pipeline

def render_video(region_id, audio_path):
    weather_data = fetch_weather_for_region(region_id)
    forecast_type = classify_forecast(weather_data)
    video_path = render_video_pipeline(region_id, audio_path, weather_data, forecast_type)
    print(f"Video generated at: {video_path}")
    return video_path

if __name__ == "__main__":
    test_region = "warszawa"
    audio_path = f"weather-reels-system/output/voice_{test_region}.wav"
    render_video(test_region, audio_path)