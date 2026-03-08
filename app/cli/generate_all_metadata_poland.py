import json
from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.publishing.metadata_builder import build_metadata
import os

def generate_metadata_for_all_poland():
    with open("weather-reels-system/config/regions/regions_poland.json", "r", encoding="utf-8") as f:
        regions = json.load(f)
    for region_id in regions.keys():
        weather_data = fetch_weather_for_region(region_id)
        forecast_type = classify_forecast(weather_data)
        metadata = build_metadata(region_id, weather_data, forecast_type)
        metadata_path = os.path.join("weather-reels-system/data", f"metadata_{region_id}.json")
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        print(f"{region_id} -> Metadata saved: {metadata_path}")

if __name__ == "__main__":
    generate_metadata_for_all_poland()