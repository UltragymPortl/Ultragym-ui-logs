import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "logsdb")

client: AsyncIOMotorClient = None
_db = None

async def connect_to_mongo():
    global client, _db
    client = AsyncIOMotorClient(MONGO_URI)
    _db = client[DB_NAME]
    # Optionally ensure indexes
    await _db["logs"].create_index("createdAt")
    await _db["logs"].create_index("userId")

async def close_mongo_connection():
    global client
    if client:
        client.close()

def get_db():
    global _db
    if _db is None:
        raise RuntimeError("Database not initialised. Did you call connect_to_mongo()?")
    return _db
