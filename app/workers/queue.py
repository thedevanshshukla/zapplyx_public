from celery import Celery
from app.config import settings

# Initialize Celery app instance
queue_app = Celery(
    "pipeline_workers",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# Base queue and routing configurations
queue_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    timezone="UTC"
)
