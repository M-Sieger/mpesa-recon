"""
Upload Schemas
Pydantic models for file upload responses
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.transaction import TransactionResponse


class UploadResponse(BaseModel):
    """Response after file upload"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    file_type: str
    file_size: int
    parsing_status: str
    transactions_parsed: int
    uploaded_at: datetime


class ParseResponse(BaseModel):
    """Response after parsing"""
    upload: UploadResponse
    transactions: List["TransactionResponse"]  # Forward reference as string
    success: bool
    message: str
    parsing_confidence: Optional[float] = Field(
        None,
        description="Confidence score of parsing (0-1)"
    )
