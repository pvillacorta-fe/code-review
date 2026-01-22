from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
import logging

from database import get_db
from models.models import User
from services.user_service import UserService

router = APIRouter()
logger = logging.getLogger(__name__)


class UserCreate(BaseModel):
    email: str
    name: str
    password: str


@router.get("/")
def get_users(skip: int = 0, limit: int = 100):
    db = get_db()
    users = db.query(User).offset(skip).limit(limit).all()
    
    return [
        {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "password_hash": user.password_hash,
            "is_active": user.is_active
        }
        for user in users
    ]


@router.get("/search")
def search_users(query: str = ""):
    db = get_db()
    
    sql = f"SELECT id, email, name FROM users WHERE name LIKE '%{query}%' OR email LIKE '%{query}%'"
    result = db.execute(text(sql))
    
    return result.fetchall()


@router.get("/{user_id}")
def get_user(user_id: int):
    db = get_db()
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    logger.info(f"User retrieved: {user.email}, password_hash: {user.password_hash[:10]}...")
    
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "password_hash": user.password_hash,
        "is_active": user.is_active
    }


@router.post("/")
def create_user(user_data: UserCreate):
    service = UserService()
    user = service.create_user(
        email=user_data.email,
        name=user_data.name,
        password=user_data.password
    )
    return {"id": user.id, "email": user.email, "name": user.name}
