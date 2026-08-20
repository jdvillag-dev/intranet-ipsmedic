"""
Endpoints de Noticias
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models import News, NewsComment, User
from app.schemas import NewsCreate, NewsUpdate, NewsResponse, NewsCommentCreate
from app.security import get_current_user

router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/", response_model=list[NewsResponse])
async def get_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtener noticias publicadas"""
    news = db.query(News).filter(
        News.is_published == True
    ).order_by(News.published_at.desc()).offset(skip).limit(limit).all()
    return news


@router.get("/{news_id}", response_model=NewsResponse)
async def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    """Obtener una noticia específica"""
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Noticia no encontrada"
        )
    
    # Incrementar contador de vistas
    news.views_count += 1
    db.commit()
    
    return news


@router.post("/", response_model=NewsResponse)
async def create_news(
    news_data: NewsCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Crear una noticia (solo admin)"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para crear noticias"
        )
    
    new_news = News(
        title=news_data.title,
        content=news_data.content,
        summary=news_data.summary,
        category=news_data.category,
        created_by=user_id,
        is_published=news_data.featured,
        featured=news_data.featured,
        published_at=datetime.utcnow() if news_data.featured else None
    )
    
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    
    return new_news


@router.put("/{news_id}", response_model=NewsResponse)
async def update_news(
    news_id: int,
    news_data: NewsUpdate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Actualizar una noticia (solo admin o autor)"""
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Noticia no encontrada"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if user.role != "admin" and news.created_by != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para editar esta noticia"
        )
    
    if news_data.title:
        news.title = news_data.title
    if news_data.content:
        news.content = news_data.content
    if news_data.summary:
        news.summary = news_data.summary
    if news_data.category:
        news.category = news_data.category
    if news_data.featured is not None:
        news.featured = news_data.featured
    if news_data.is_published is not None:
        news.is_published = news_data.is_published
        if news_data.is_published and not news.published_at:
            news.published_at = datetime.utcnow()
    
    db.commit()
    db.refresh(news)
    
    return news


@router.delete("/{news_id}")
async def delete_news(
    news_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Eliminar una noticia (solo admin)"""
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Noticia no encontrada"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permiso para eliminar noticias"
        )
    
    db.delete(news)
    db.commit()
    
    return {"message": "Noticia eliminada"}


@router.post("/{news_id}/comments")
async def add_comment(
    news_id: int,
    comment_data: NewsCommentCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Agregar comentario a una noticia"""
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Noticia no encontrada"
        )
    
    new_comment = NewsComment(
        content=comment_data.content,
        news_id=news_id,
        user_id=user_id
    )
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment
