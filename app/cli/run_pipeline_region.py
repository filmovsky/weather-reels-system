import os
from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.scripting.generators import generate_script_for_region
from app.audio.elevenlabs_tts import generate_voice
from app.video.video_pipeline import render_video_pipeline
from app.publishing.metadata_builder import build_metadata

def run_pipeline(region_id):
    weather_data = fetch_weather_for_region(region_id)
    forecast_type = classify_forecast(weather_data)
    script_text = generate_script_for_region(region_id, weather_data, forecast_type)
    audio_path = generate_voice(region_id, script_text)
    video_path = render_video_pipeline(region_id, audio_path, weather_data, forecast_type)
    metadata = build_metadata(region_id, weather_data, forecast_type)
    print(f"{video_path}\n{audio_path}\n{metadata}")

if __name__ == "__main__":
    test_region = "warszawa"
    run_pipeline(test_region)