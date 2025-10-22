"""
Transaction Schemas
Pydantic models for API request/response
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time, datetime
from decimal import Decimal


class TransactionBase(BaseModel):
    """Base transaction schema"""
    transaction_id: str = Field(..., description="M-Pesa transaction ID")
    date: date = Field(..., description="Transaction date")
    time: Optional[time] = Field(None, description="Transaction time")
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
    id: int
    upload_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
