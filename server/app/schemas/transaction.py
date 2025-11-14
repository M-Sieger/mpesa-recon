"""
Transaction Schemas
Pydantic models for API request/response
"""
from datetime import date as date_type, time as time_type, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TransactionBase(BaseModel):
    """Base transaction schema"""
    transaction_id: str = Field(..., description="M-Pesa transaction ID")
    date: date_type = Field(..., description="Transaction date")
    time: Optional[time_type] = Field(None, description="Transaction time")
    description: Optional[str] = Field(None, description="Transaction details")
    amount: Decimal = Field(..., description="Transaction amount")
    category: Optional[str] = Field(None, description="User-defined category")
    notes: Optional[str] = Field(None, description="User notes")


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction"""
    upload_id: Optional[int] = None


class TransactionUpdate(BaseModel):
    """Schema for updating a transaction"""
    category: Optional[str] = None
    notes: Optional[str] = None


class TransactionResponse(TransactionBase):
    """Schema for transaction response"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    upload_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]
