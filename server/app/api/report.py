"""
Report API Endpoints
Generate eTIMS-compliant reports
"""
from fastapi import APIRouter, HTTPException, Depends, Query, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
import csv
import io

from app.database import get_db
from app.models.transaction import Transaction

router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/csv")
def export_csv(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    category: Optional[str] = Query(None, description="Filter by category"),
    db: Session = Depends(get_db)
):
    """
    Export transactions as CSV for eTIMS submission
    
    Args:
        start_date: Filter from this date
        end_date: Filter until this date
        category: Filter by category
    """
    # Build query
    query = db.query(Transaction)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    if category:
        query = query.filter(Transaction.category == category)
    
    transactions = query.order_by(Transaction.date.desc()).all()
    
    if not transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No transactions found for the given filters"
        )
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow([
        "Date",
        "Transaction ID",
        "Description",
        "Amount (KSh)",
        "Category",
        "Notes"
    ])
    
    # Data
    for t in transactions:
        writer.writerow([
            t.date.strftime("%Y-%m-%d"),
            t.transaction_id,
            t.description or "",
            f"{t.amount:.2f}",
            t.category or "Uncategorized",
            t.notes or ""
        ])
    
    # Prepare response
    output.seek(0)
    filename = f"mpesa_transactions_{start_date or 'all'}_{end_date or 'all'}.csv"
    
    return StreamingResponse(
        io.BytesIO(output.getvalue().encode("utf-8")),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get("/summary")
def get_summary(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Get transaction summary (total income, expenses by category)
    
    Args:
        start_date: Filter from this date
        end_date: Filter until this date
    """
    query = db.query(Transaction)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    
    transactions = query.all()
    
    if not transactions:
        return {
            "total_transactions": 0,
            "total_amount": 0,
            "categories": {}
        }
    
    # Calculate summary
    total_amount = sum(t.amount for t in transactions)
    
    # Group by category
    categories = {}
    for t in transactions:
        cat = t.category or "Uncategorized"
        if cat not in categories:
            categories[cat] = {
                "count": 0,
                "total": 0
            }
        categories[cat]["count"] += 1
        categories[cat]["total"] += float(t.amount)
    
    return {
        "total_transactions": len(transactions),
        "total_amount": float(total_amount),
        "categories": categories,
        "date_range": {
            "start": start_date.isoformat() if start_date else None,
            "end": end_date.isoformat() if end_date else None
        }
    }
