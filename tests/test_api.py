# Simple tests require a running MongoDB instance and the server.
# This file is a placeholder showing how to test with httpx and pytest.
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "userId": "t1",
            "screenName": "scr1",
            "fileName": "f.py",
            "error": "err",
            "message": "msg",
            "type": "DEBUG"
        }
        r = await ac.post("/logs", json=payload)
        assert r.status_code == 201
        data = r.json()
        assert data["userId"] == "t1"
        lid = data["id"]
        r2 = await ac.get(f"/logs/{lid}")
        assert r2.status_code == 200
        data2 = r2.json()
        assert data2["id"] == lid
