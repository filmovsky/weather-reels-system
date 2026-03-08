import json
from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.scripting.generators import generate_script_for_region
from app.audio.elevenlabs_tts import generate_voice

def generate_audio_for_all_poland():
    with open("weather-reels-system/config/regions/regions_poland.json", "r", encoding="utf-8") as f:
        regions = json.load(f)
    for region_id in regions.keys():
        weather_data = fetch_weather_for_region(region_id)
        forecast_type = classify_forecast(weather_data)
        script_text = generate_script_for_region(region_id, weather_data, forecast_type)
        audio_path = generate_voice(region_id, script_text)
        print(f"{region_id} -> Audio generated: {audio_path}")

if __name__ == "__main__":
    generate_audio_for_all_poland()