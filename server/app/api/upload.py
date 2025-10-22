"""
Upload API Endpoints
Handles file uploads and parsing
"""
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import os
import tempfile
from datetime import datetime

from app.database import get_db
from app.models.upload import Upload, ParsingStatus
from app.models.transaction import Transaction
from app.schemas.upload import ParseResponse, UploadResponse
from app.schemas.transaction import TransactionResponse
from app.services.parser_service import parser_service
from app.config import settings

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/", response_model=ParseResponse, status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload and parse M-Pesa statement (PDF or CSV)
    
    Returns:
        Parsed transactions
    """
    # Validate file type
    file_extension = file.filename.split(".")[-1].lower()
    if file_extension not in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type not allowed. Allowed types: {', '.join(settings.ALLOWED_FILE_TYPES)}"
        )
    
    # Read file
    contents = await file.read()
    file_size = len(contents)
    
    # Validate file size
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size: {settings.MAX_UPLOAD_SIZE / 1024 / 1024}MB"
        )
    
    # Create upload record
    upload = Upload(
        filename=file.filename,
        file_type=file_extension,
        file_size=file_size,
        parsing_status=ParsingStatus.PROCESSING
    )
    db.add(upload)
    db.commit()
    db.refresh(upload)
    
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp_file:
        tmp_file.write(contents)
        tmp_file_path = tmp_file.name
    
    try:
        # Parse file
        parsed_data = parser_service.parse_file(tmp_file_path, file_extension)
        
        if not parsed_data:
            upload.parsing_status = ParsingStatus.FAILED
            upload.parsing_error = "No transactions found in file"
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="No transactions found in file"
            )
        
        # Save transactions
        transactions = []
        for data in parsed_data:
            # Check if transaction already exists
            existing = db.query(Transaction).filter(
                Transaction.transaction_id == data["transaction_id"]
            ).first()
            
            if existing:
                # Skip duplicate
                continue
            
            transaction = Transaction(
                upload_id=upload.id,
                transaction_id=data["transaction_id"],
                date=data["date"],
                time=data.get("time"),
                description=data.get("description"),
                amount=data["amount"],
            )
            db.add(transaction)
            transactions.append(transaction)
        
        # Update upload status
        upload.parsing_status = ParsingStatus.COMPLETED
        upload.transactions_parsed = len(transactions)
        upload.processed_at = datetime.utcnow()
        
        db.commit()
        
        # Refresh to get all data
        for t in transactions:
            db.refresh(t)
        db.refresh(upload)
        
        # Calculate parsing confidence (simplified)
        confidence = min(len(transactions) / len(parsed_data), 1.0) if parsed_data else 0.0
        
        return ParseResponse(
            upload=UploadResponse.model_validate(upload),
            transactions=[TransactionResponse.model_validate(t) for t in transactions],
            success=True,
            message=f"Successfully parsed {len(transactions)} transactions",
            parsing_confidence=confidence
        )
    
    except Exception as e:
        # Update upload status to failed
        upload.parsing_status = ParsingStatus.FAILED
        upload.parsing_error = str(e)[:500]
        db.commit()
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Parsing failed: {str(e)}"
        )
    
    finally:
        # Clean up temp file
        try:
            os.unlink(tmp_file_path)
        except:
            pass


@router.get("/history", response_model=List[UploadResponse])
def get_upload_history(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get upload history
    
    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
    """
    uploads = db.query(Upload).order_by(Upload.uploaded_at.desc()).offset(skip).limit(limit).all()
    return [UploadResponse.model_validate(u) for u in uploads]


@router.get("/{upload_id}", response_model=UploadResponse)
def get_upload(upload_id: int, db: Session = Depends(get_db)):
    """Get upload details by ID"""
    upload = db.query(Upload).filter(Upload.id == upload_id).first()
    if not upload:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Upload not found"
        )
    return UploadResponse.model_validate(upload)
