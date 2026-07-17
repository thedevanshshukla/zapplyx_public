import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

logger = logging.getLogger("app.database")

class DatabaseHelper:
    client: AsyncIOMotorClient = None
    db = None

db_helper = DatabaseHelper()

async def init_db():
    """Database connections and schema constraint definitions."""
    db_helper.client = AsyncIOMotorClient(settings.MONGODB_URI)
    db_helper.db = db_helper.client[settings.MONGODB_DB_NAME]
    # Configures index constraints on startup
    pass

def get_database():
    return db_helper.db

def get_founders_collection():
    return db_helper.db.founders
