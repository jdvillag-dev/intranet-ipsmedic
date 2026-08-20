"""
Modelos de la base de datos
"""
from app.models.user import User
from app.models.area import Area, Macroprocess
from app.models.news import News, NewsComment
from app.models.audit import AuditLog
from app.models.google_drive_config import GoogleDriveConfig

__all__ = [
    "User",
    "Area",
    "Macroprocess",
    "News",
    "NewsComment",
    "AuditLog",
    "GoogleDriveConfig",
]
