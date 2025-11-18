from pydantic import BaseModel, Field, validator
from typing import Optional
from enum import Enum
from datetime import datetime

class LogType(str, Enum):
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class LogIn(BaseModel):
    userId: str = Field(..., example="user123")
    screenName: str = Field(..., example="HomeScreen")
    fileName: Optional[str] = Field(None, example="main.py")
    error: Optional[str] = Field(None, example="Traceback ...")
    message: Optional[str] = Field(None, example="Something happened")
    createdAt: Optional[datetime] = None
    type: LogType

    @validator("createdAt", pre=True, always=True)
    def set_created_at(cls, v):
        if v is None:
            return datetime.utcnow()
        return v

class LogOut(LogIn):
    id: str
