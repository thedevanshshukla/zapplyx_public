from pydantic import BaseModel, EmailStr
from typing import Optional, Dict
from datetime import datetime

class CandidateProfile(BaseModel):
    name: str
    email: EmailStr
    experience_summary: str
    work_preferences: str
    academic_history: Optional[str] = None
    technical_skills: list[str] = []

class User(BaseModel):
    user_id: str
    username: str
    hashed_password: str
    created_at: datetime
    candidate_profile: Optional[CandidateProfile] = None
    subscription_tier: str = "free"
    credits: Dict[str, int] = {}
