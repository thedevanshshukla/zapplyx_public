from typing import List, Dict, Any
from app.agents.base import BaseAgent

class ScraperAgent(BaseAgent):
    """Scraping crawler automation interface."""
    
    async def scrape_yc_company_page(self, company_url: str) -> Dict[str, Any]:
        """Asynchronously loads target company URL and scrapes profile links."""
        pass
