import logging
from typing import Dict

class BaseAgent:
    """Base design interface for LLM Agents."""
    def __init__(self, api_keys: Dict[str, str], user_id: str = None):
        self.api_keys = api_keys
        self.user_id = user_id
        self.logger = logging.getLogger(self.__class__.__name__)

    async def execute_gemini_call(self, prompt: str) -> str:
        """Executes structured query call against Google Gemini LLM API."""
        pass

    async def execute_openai_call(self, prompt: str) -> str:
        """Executes fallback query call against OpenAI GPT LLM API."""
        pass
