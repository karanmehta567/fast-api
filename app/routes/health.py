from fastapi import APIRouter
from app.db import db

router = APIRouter()

@router.get("/health")
async def health_check():
    try:
        await db.command("ping")
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "details": str(e)}