"""
Modelos de Áreas y Macroprocesos
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Macroprocess(Base):
    """Modelo de Macroproceso (nivel superior)"""
    
    __tablename__ = "macroprocesses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    code = Column(String, unique=True)
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    areas = relationship("Area", back_populates="macroprocess")


class Area(Base):
    """Modelo de Área"""
    
    __tablename__ = "areas"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    code = Column(String, unique=True)
    macroprocess_id = Column(Integer, ForeignKey("macroprocesses.id"))
    google_drive_folder_id = Column(String, nullable=True)  # ID de carpeta en Google Drive
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones
    macroprocess = relationship("Macroprocess", back_populates="areas")
    users = relationship("User", back_populates="area")
