from app.workers.celery_app import celery_app
from app.weather.providers.open_meteo import get_forecast


@celery_app.task
def fetch_weather(latitude: float, longitude: float):

    data = get_forecast(latitude, longitude)

    return data