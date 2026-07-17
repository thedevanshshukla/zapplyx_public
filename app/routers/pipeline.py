from fastapi import APIRouter, Depends, Query, Response
from typing import List, Optional
from app.models.founder import Founder
from app.models.user import User
from app.routers.auth import get_current_user_from_token_or_query

router = APIRouter()

@router.get("/founders", response_model=List[Founder])
async def list_founders(
    response: Response,
    company: Optional[str] = Query(None),
    batch: Optional[List[str]] = Query(None),
    is_scraped: Optional[bool] = Query(None),
    is_enriched: Optional[bool] = Query(None),
    is_resume_generated: Optional[bool] = Query(None),
    skip: int = 0,
    limit: int = 50,
    current_user: User = Depends(get_current_user_from_token_or_query)
):
    """
    Query and return listing of founder profiles.
    Implementation handles database-level sorting, skip/limit pagination, and search matching.
    """
    pass

@router.post("/batch/enrich")
async def trigger_batch_enrichment(
    founder_ids: List[str],
    current_user: User = Depends(get_current_user_from_token_or_query)
):
    """Enqueues batch contact details lookup to background tasks queue."""
    pass
