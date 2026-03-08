from celery.schedules import crontab


beat_schedule = {
    "morning_forecast_jobs": {
        "task": "app.workers.tasks_weather.fetch_weather",
        "schedule": crontab(hour=5, minute=50),
        "args": ()
    },
    "evening_forecast_jobs": {
        "task": "app.workers.tasks_weather.fetch_weather",
        "schedule": crontab(hour=17, minute=50),
        "args": ()
    }
}