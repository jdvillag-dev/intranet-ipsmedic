"""
Schemas de Usuario
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    """Schema para crear usuario"""
    email: EmailStr
    full_name: str
    password: str
    area_id: Optional[int] = None


class UserLogin(BaseModel):
    """Schema para login"""
    email: str
    password: str


class UserResponse(BaseModel):
    """Schema de respuesta de usuario"""
    id: int
    email: str
    full_name: str
    role: str
    area_id: Optional[int] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """Schema para actualizar usuario"""
    full_name: Optional[str] = None
    area_id: Optional[int] = None
    role: Optional[str] = None
