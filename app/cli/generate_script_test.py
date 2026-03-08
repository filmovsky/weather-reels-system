from app.weather.aggregator import fetch_weather_for_region
from app.intelligence.forecast_classifier import classify_forecast
from app.scripting.generators import generate_script_for_region

def generate_script(region_id):
    weather_data = fetch_weather_for_region(region_id)
    forecast_type = classify_forecast(weather_data)
    script_text = generate_script_for_region(region_id, weather_data, forecast_type)
    with open(f"weather-reels-system/data/script_{region_id}.txt", "w", encoding="utf-8") as f:
        f.write(script_text)
    print(f"Script saved for {region_id}")

if __name__ == "__main__":
    test_region = "warszawa"
    generate_script(test_region)