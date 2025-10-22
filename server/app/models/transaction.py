"""
Transaction Model
Represents a single M-Pesa transaction
"""
from sqlalchemy import Column, Integer, String, Numeric, Date, Time, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    upload_id = Column(Integer, ForeignKey("uploads.id", ondelete="CASCADE"), nullable=True)
    
    # M-Pesa Transaction Details
    transaction_id = Column(String(50), unique=True, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    time = Column(Time, nullable=True)
    description = Column(Text, nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
    
    # User-added metadata
    category = Column(String(50), nullable=True, index=True)
    notes = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Transaction {self.transaction_id} - {self.amount}>"
