from fastapi import APIRouter, Depends
from app.models.user import User
from app.routers.auth import get_current_user_from_token_or_query

router = APIRouter()

@router.get("/tasks/active")
async def list_active_celery_tasks(current_user: User = Depends(get_current_user_from_token_or_query)):
    """Returns active background worker task statuses."""
    pass

@router.post("/tasks/terminate")
async def terminate_active_task(
    task_id: str,
    current_user: User = Depends(get_current_user_from_token_or_query)
):
    """Sends cancellation signals to background workers."""
    pass
