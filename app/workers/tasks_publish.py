from app.workers.celery_app import celery_app
from app.publishing.publish_router import publish


@celery_app.task
def publish_video(platform: str, video_path: str, title: str, description: str = ""):

    result = publish(platform, video_path, title, description)

    return result