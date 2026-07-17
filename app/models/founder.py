from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CompanyDetails(BaseModel):
    website: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    team_size: Optional[int] = 0
    description: Optional[str] = None

class PipelineStatus(BaseModel):
    is_scraped: bool = False
    is_enriched: bool = False
    is_summarized: bool = False
    is_email_generated: bool = False
    is_resume_generated: bool = False
    is_approved: bool = False
    is_email_sent: bool = False

class Founder(BaseModel):
    founder_id: str
    name: str
    role: str
    company: str
    batch: str
    linkedin_url: Optional[str] = None
    yc_url: Optional[str] = None
    twitter_url: Optional[str] = None
    company_data: Optional[CompanyDetails] = None
    pipeline_status: PipelineStatus = PipelineStatus()
    created_at: datetime
