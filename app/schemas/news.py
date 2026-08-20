"""
Schemas de Noticias
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class NewsCommentCreate(BaseModel):
    """Schema para crear comentario"""
    content: str


class NewsCommentResponse(BaseModel):
    """Schema de respuesta de comentario"""
    id: int
    content: str
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class NewsCreate(BaseModel):
    """Schema para crear noticia"""
    title: str
    content: str
    summary: str
    category: str = "general"
    featured: bool = False


class NewsUpdate(BaseModel):
    """Schema para actualizar noticia"""
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    category: Optional[str] = None
    featured: Optional[bool] = None
    is_published: Optional[bool] = None


class NewsResponse(BaseModel):
    """Schema de respuesta de noticia"""
    id: int
    title: str
    content: str
    summary: str
    category: str
    created_by: int
    is_published: bool
    featured: bool
    views_count: int
    created_at: datetime
    published_at: Optional[datetime] = None
    comments: List[NewsCommentResponse] = []
    
    class Config:
        from_attributes = True
