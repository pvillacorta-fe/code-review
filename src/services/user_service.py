from fastapi import HTTPException
from datetime import datetime
import hashlib

from database import get_db
from models.models import User


class UserService:
    
    def create_user(
        self,
        email: str,
        name: str,
        password: str,
        created_at: datetime = datetime.now()
    ):
        db = get_db()
        
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        new_user = User(
            email=email,
            name=name,
            password_hash=password_hash,
            is_active=True,
            created_at=created_at
        )
        
        db.add(new_user)
        db.commit()
        
        return new_user
