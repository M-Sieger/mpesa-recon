"""
Application Configuration
Loads settings from environment variables
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:dev@localhost:5432/mpesa_recon"
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "M-Recon API"
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative port
    ]
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 10485760  # 10MB
    ALLOWED_FILE_TYPES: List[str] = ["pdf", "csv"]
    
    # Parsing
    MIN_PARSING_CONFIDENCE: float = 0.95
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
