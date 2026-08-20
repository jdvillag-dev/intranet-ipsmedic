"""
Configuración de la aplicación FastAPI
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    # FastAPI
    fastapi_env: str = "development"
    debug: bool = True
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Base de Datos
    database_url: str = "sqlite:///./intranet.db"
    
    # Google Drive
    google_client_id: str = ""
    google_client_secret: str = ""
    google_redirect_uri: str = "http://localhost:8000/api/auth/google/callback"
    
    # Email SMTP
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_from_email: str = "noreply@ipsmedic.com"
    smtp_from_name: str = "IPS Médic Intranet"
    
    # Configuración de Dominio
    allowed_email_domain: str = "ipsmedic.com"
    app_name: str = "Intranet IPS Médic"
    app_url: str = "http://localhost:8000"
    
    # Google Drive
    google_drive_folder_id: str = "root"
    google_drive_cache_expiry: int = 3600
    
    # CORS
    cors_origins: List[str] = ["http://localhost:8000", "http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
