"""
Modelos de Noticias
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class News(Base):
    """Modelo de Noticia"""
    
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    summary = Column(String)
    category = Column(String, default="general")  # general, importante, evento, etc
    created_by = Column(Integer, ForeignKey("users.id"))
    is_published = Column(Boolean, default=False)
    featured = Column(Boolean, default=False)
    views_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)
    
    # Relaciones
    created_by_user = relationship("User", back_populates="news_created")
    comments = relationship("NewsComment", back_populates="news", cascade="all, delete-orphan")


class NewsComment(Base):
    """Modelo de Comentario en Noticia"""
    
    __tablename__ = "news_comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    news_id = Column(Integer, ForeignKey("news.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    news = relationship("News", back_populates="comments")
    user = relationship("User", back_populates="comments")
