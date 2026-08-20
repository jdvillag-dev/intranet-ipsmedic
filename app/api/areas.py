"""
Endpoints de Áreas y Macroprocesos
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Area, Macroprocess, User
from app.schemas import AreaResponse, MacroprocessResponse

router = APIRouter(prefix="/api/areas", tags=["areas"])


@router.get("/macroprocesses", response_model=list[MacroprocessResponse])
async def get_macroprocesses(db: Session = Depends(get_db)):
    """Obtener todos los macroprocesos con sus áreas"""
    macroprocesses = db.query(Macroprocess).order_by(Macroprocess.order).all()
    return macroprocesses


@router.get("/{area_id}", response_model=AreaResponse)
async def get_area(area_id: int, db: Session = Depends(get_db)):
    """Obtener área específica"""
    area = db.query(Area).filter(Area.id == area_id).first()
    if not area:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Área no encontrada"
        )
    return area


@router.get("/user/current/area", response_model=AreaResponse)
async def get_user_area(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Obtener el área del usuario actual"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user or not user.area:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no tiene área asignada"
        )
    return user.area
