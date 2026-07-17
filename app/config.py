from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Pydantic Settings interface resolving environment configurations."""
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "jobhunt"
    REDIS_URL: str = "redis://localhost:6379"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # Generic API Keys config interfaces
    GEMINI_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    EXPLORIUM_API_KEY: str = ""
    APOLLO_API_KEYS: list = []
    LUSHA_API_KEY: str = ""

    # SMTP configuration interfaces
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_SENDER: str = ""

    # Billing & redirect links
    UPI_ID: str = ""
    UPI_PAYEE_NAME: str = ""
    APP_BASE_URL: str = "http://localhost:8000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
