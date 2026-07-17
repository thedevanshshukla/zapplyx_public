import logging
from app.workers.queue import queue_app

logger = logging.getLogger("app.tasks")

@queue_app.task(bind=True, name="app.workers.tasks.batch_enrichment_task")
def batch_enrichment_task(self, user_id: str, founder_ids: list):
    """ Celery background worker wrapper executing batch lookups."""
    pass
