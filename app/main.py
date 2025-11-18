from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from .models import LogIn, LogOut, LogType
from .db import get_db, connect_to_mongo, close_mongo_connection
from typing import List, Optional
from bson import ObjectId
import datetime

app = FastAPI(title="Logs Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

from fastapi import Response

@app.post("/logs", status_code=201)
async def create_log(payload: LogIn):
    db = get_db()
    await db["logs"].insert_one(payload.dict())
    return Response(status_code=201)

