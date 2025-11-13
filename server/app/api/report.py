"""
Report API Endpoints
Generate loan-ready financial reports from M-Pesa statements
"""
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, Query, UploadFile, status
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
from datetime import date
import csv
import io

from app.database import get_db
from app.models.transaction import Transaction
from app.services.categorization_service import categorisation_service
from app.services.pdf_service import pdf_parser
from app.services.report_service import report_service
from app.services.summary_service import summary_service


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
        "categories": categories
    }


@router.post("/generate")
async def generate_loan_report(
    file: UploadFile = File(..., description="M-Pesa PDF statement"),
    password: Optional[str] = Form(None, description="PDF password (usually ID number)"),
    member_name: str = Form(..., description="Member name for report header"),
    mobile: str = Form(..., description="Mobile number"),
    email: Optional[str] = Form(None, description="Email address"),
    notes: Optional[str] = Form(None, description="Optional note for report footer"),
) -> FileResponse:
    """
    Generate a loan-ready financial report from an M-Pesa PDF statement.
    
    **Process:**
    1. Parse PDF → extract transactions
    2. Categorize → business vs. personal, income vs. expense
    3. Summarize → 6-month window, loan capacity calculation
    4. Generate → professional PDF report with verification code
    
    **Returns:** PDF file download
    """
    
    # Validate file type
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    # Save uploaded file temporarily
    temp_path = Path(f"/tmp/{file.filename}")
    output_path = None
    
    try:
        with temp_path.open("wb") as f:
            content = await file.read()
            f.write(content)
        
        # Step 1: Parse PDF
        try:
            transactions, metadata = pdf_parser.parse_pdf(str(temp_path), password=password)
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"PDF parsing failed: {str(e)}")
        
        if not transactions:
            raise HTTPException(status_code=422, detail="No transactions found in PDF")
        
        # Step 2: Categorize transactions
        categorised = categorisation_service.categorise_transactions(transactions)
        
        # Step 3: Generate financial summary
        summary = summary_service.generate_summary(categorised)
        
        # Step 4: Build report metadata
        report_metadata = {
            "member_name": member_name,
            "mobile": mobile,
            "email": email or "-",
            "notes": notes,
            "statement_type": metadata.get("statement_type"),
            "pages": metadata.get("total_pages"),
        }
        
        # Step 5: Generate PDF report
        output_path = f"/tmp/report_{file.filename}"
        report_service.build_report(summary, report_metadata, output_path)
        
        # Return PDF as download
        return FileResponse(
            path=output_path,
            media_type="application/pdf",
            filename=f"M-Recon_Report_{member_name.replace(' ', '_')}.pdf",
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {str(e)}")
    
    finally:
        # Cleanup temporary input file
        if temp_path.exists():
            temp_path.unlink()

