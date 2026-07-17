from app.agents.base import BaseAgent
from typing import Dict, Any

class IntelligenceAgent(BaseAgent):
    """Personalization insight extractor interface."""
    
    async def analyze_company_summary(self, raw_bio: str) -> Dict[str, Any]:
        """Extracts value propositions and custom hooks using structured LLM calls."""
        pass
