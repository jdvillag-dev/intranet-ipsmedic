"""
Modelo de Usuario
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
    """Modelo de Usuario de la intranet"""
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    role = Column(String, default="user")  # admin, gerente, user
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Relaciones
    area = relationship("Area", back_populates="users")
    news_created = relationship("News", back_populates="created_by_user")
    comments = relationship("NewsComment", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")
