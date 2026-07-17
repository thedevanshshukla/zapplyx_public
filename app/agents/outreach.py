from app.agents.base import BaseAgent
from typing import Dict, Any

class OutreachAgent(BaseAgent):
    """Outreach template generation interface."""
    
    async def generate_personal_drafts(
        self,
        candidate_profile: Dict[str, Any],
        founder_background: Dict[str, Any]
    ) -> Dict[str, str]:
        """Drafts personalized cold emails and LinkedIn messages matching backgrounds."""
        pass
