from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")

async def get_current_user_from_token_or_query(token: str = Depends(oauth2_scheme)) -> User:
    """Resolves active user session model from request tokens."""
    pass

@router.post("/token")
async def login_for_access_token():
    """Issues JWT access token matching user credentials."""
    pass
