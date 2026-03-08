from app.workers.celery_app import celery_app


@celery_app.task
def cleanup_temp_files(files: list):

    removed = []

    for path in files:
        try:
            import os
            os.remove(path)
            removed.append(path)
        except Exception:
            pass

    return {
        "removed_files": removed
    }