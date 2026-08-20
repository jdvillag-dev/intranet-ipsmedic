"""
Endpoints de Administración
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Area, AuditLog
from app.schemas import UserResponse, UserUpdate
from app.security import get_current_user

router = APIRouter(prefix="/api/admin", tags=["admin"])


def check_admin(user_id: int, db: Session):
    """Verificar si el usuario es admin"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tiene permisos de administrador"
        )
    return user


@router.get("/users", response_model=list[UserResponse])
async def get_all_users(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtener todos los usuarios (admin)"""
    await check_admin(user_id, db)
    users = db.query(User).all()
    return users


@router.put("/users/{target_user_id}", response_model=UserResponse)
async def update_user(
    target_user_id: int,
    user_data: UserUpdate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Actualizar usuario (admin)"""
    await check_admin(user_id, db)
    
    user = db.query(User).filter(User.id == target_user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    if user_data.full_name:
        user.full_name = user_data.full_name
    if user_data.area_id is not None:
        user.area_id = user_data.area_id
    if user_data.role:
        user.role = user_data.role
    
    db.commit()
    db.refresh(user)
    
    return user


@router.delete("/users/{target_user_id}")
async def delete_user(
    target_user_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Eliminar usuario (admin)"""
    await check_admin(user_id, db)
    
    user = db.query(User).filter(User.id == target_user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    db.delete(user)
    db.commit()
    
    return {"message": "Usuario eliminado"}


@router.get("/audit-logs")
async def get_audit_logs(
    skip: int = 0,
    limit: int = 100,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtener logs de auditoría (admin)"""
    await check_admin(user_id, db)
    logs = db.query(AuditLog).order_by(
        AuditLog.timestamp.desc()
    ).offset(skip).limit(limit).all()
    return logs
