"""
Upload Schemas
Pydantic models for file upload responses
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.schemas.transaction import TransactionResponse


class UploadResponse(BaseModel):
    """Response after file upload"""
    id: int
    filename: str
    file_type: str
    file_size: int
    parsing_status: str
    transactions_parsed: int
    uploaded_at: datetime
    
    class Config:
        from_attributes = True


class ParseResponse(BaseModel):
    """Response after parsing"""
    upload: UploadResponse
    transactions: List[TransactionResponse]
    success: bool
    message: str
    parsing_confidence: Optional[float] = Field(
        None,
        description="Confidence score of parsing (0-1)"
    )
