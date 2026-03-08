.\venv\Scripts\Activate.ps1

celery -A app.workers.celery_app worker --loglevel=info --pool=solo