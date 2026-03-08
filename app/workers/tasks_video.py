from app.workers.celery_app import celery_app
from app.video.renderer import render_video


@celery_app.task
def render_weather_video(audio_path: str, output_path: str):

    video = render_video(audio_path, output_path)

    return {
        "audio_path": audio_path,
        "video_path": video
    }