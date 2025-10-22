"""
Upload Model
Tracks file uploads and parsing status
"""
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
import enum
from app.database import Base


class ParsingStatus(str, enum.Enum):
    """Enum for parsing status"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Upload(Base):
    __tablename__ = "uploads"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # File metadata
    filename = Column(String(255), nullable=False)
    file_type = Column(String(10), nullable=False)
    file_size = Column(Integer, nullable=False)
    
    # Parsing
    parsing_status = Column(
        Enum(ParsingStatus),
        default=ParsingStatus.PENDING,
        nullable=False,
        index=True
    )
    parsing_error = Column(String(500), nullable=True)
    transactions_parsed = Column(Integer, default=0)
    
    # Timestamps
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<Upload {self.filename} - {self.parsing_status}>"
