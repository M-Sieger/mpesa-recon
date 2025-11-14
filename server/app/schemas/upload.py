"""
Upload Schemas
Pydantic models for file upload responses
"""
from pydantic import BaseModel, ConfigDict
from datetime import datetime


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


# ParseResponse removed due to circular import issues
# Not needed for report generation API (uses FileResponse instead)
