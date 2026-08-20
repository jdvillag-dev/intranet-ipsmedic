"""
Schemas de Áreas y Macroprocesos
"""
from pydantic import BaseModel
from typing import Optional, List


class AreaResponse(BaseModel):
    """Schema de respuesta de Área"""
    id: int
    name: str
    description: str
    code: str
    macroprocess_id: int
    google_drive_folder_id: Optional[str] = None
    
    class Config:
        from_attributes = True


class MacroprocessResponse(BaseModel):
    """Schema de respuesta de Macroproceso"""
    id: int
    name: str
    description: str
    code: str
    order: int
    areas: List[AreaResponse] = []
    
    class Config:
        from_attributes = True
