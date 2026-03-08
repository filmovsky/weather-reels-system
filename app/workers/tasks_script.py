from app.workers.celery_app import celery_app
from app.scripting.generators.en import generate_script


@celery_app.task
def generate_weather_script(region_name: str, weather: dict):

    script = generate_script(region_name, weather)

    return {
        "region": region_name,
        "script": script
    }