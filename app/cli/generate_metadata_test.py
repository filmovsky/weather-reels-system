from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.publishing.metadata_builder import build_metadata
import json

def generate_metadata(region_id):
    weather_data = fetch_weather_for_region(region_id)
    forecast_type = classify_forecast(weather_data)
    metadata = build_metadata(region_id, weather_data, forecast_type)
    with open(f"weather-reels-system/data/metadata_{region_id}.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"Metadata saved for {region_id}")

if __name__ == "__main__":
    test_region = "warszawa"
    generate_metadata(test_region)