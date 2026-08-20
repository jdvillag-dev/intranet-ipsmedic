"""
Schemas Pydantic para validación de datos
"""
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.schemas.news import NewsCreate, NewsResponse, NewsCommentCreate
from app.schemas.area import AreaResponse, MacroprocessResponse

__all__ = [
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "NewsCreate",
    "NewsResponse",
    "NewsCommentCreate",
    "AreaResponse",
    "MacroprocessResponse",
]
