from app.weather.aggregator import fetch_weather_for_region
import json

def fetch_and_save(region_id):
    weather_data = fetch_weather_for_region(region_id)
    with open(f"weather-reels-system/data/weather_{region_id}.json", "w", encoding="utf-8") as f:
        json.dump(weather_data, f, ensure_ascii=False, indent=2)
    print(f"Weather data saved for {region_id}")

if __name__ == "__main__":
    test_region = "warszawa"
    fetch_and_save(test_region)