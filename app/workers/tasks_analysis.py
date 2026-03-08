from app.workers.celery_app import celery_app
from app.intelligence.forecast_classifier import classify_forecast


@celery_app.task
def analyze_weather(weather_data: dict):

    forecast_type = classify_forecast(weather_data)

    return {
        "forecast_type": forecast_type,
        "weather": weather_data
    }