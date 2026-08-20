"""
Endpoints de Dashboard
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import News, User, Area
from app.security import get_current_user

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/summary")
async def get_dashboard_summary(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtener resumen del dashboard"""
    user = db.query(User).filter(User.id == user_id).first()
    
    # Noticias recientes
    recent_news = db.query(News).filter(
        News.is_published == True
    ).order_by(News.published_at.desc()).limit(5).all()
    
    # Estadísticas
    total_news = db.query(News).filter(News.is_published == True).count()
    total_areas = db.query(Area).count()
    
    return {
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "area_id": user.area_id
        },
        "recent_news": recent_news,
        "statistics": {
            "total_news": total_news,
            "total_areas": total_areas
        }
    }
