"""
Modelo de Configuración de Google Drive
"""
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.database import Base


class GoogleDriveConfig(Base):
    """Configuración de Google Drive para áreas"""
    
    __tablename__ = "google_drive_configs"
    
    id = Column(Integer, primary_key=True, index=True)
    area_id = Column(Integer, unique=True)
    folder_id = Column(String, unique=True)
    folder_name = Column(String)
    permissions_json = Column(Text)  # JSON con permisos de usuarios
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
