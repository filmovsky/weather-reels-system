from celery import Celery

celery_app = Celery(
    "weather_reels",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "app.workers.tasks_weather.*": {"queue": "queue_weather"},
    "app.workers.tasks_analysis.*": {"queue": "queue_analysis"},
    "app.workers.tasks_script.*": {"queue": "queue_script"},
    "app.workers.tasks_audio.*": {"queue": "queue_tts"},
    "app.workers.tasks_video.*": {"queue": "queue_render"},
    "app.workers.tasks_publish.*": {"queue": "queue_publish"},
}