#!/usr/bin/env python3
"""
M-Pesa PDF Parser Test Script
Quick validation of parser accuracy with real PDFs

Usage:
    python test_pdf_parser.py

Place your test PDFs in: server/test_pdfs/
"""

import os
import sys
from pathlib import Path
from app.services.pdf_service import pdf_parser
from tabulate import tabulate
from typing import List, Dict


# Test PDFs directory
TEST_PDFS_DIR = Path(__file__).parent / "test_pdfs"


def test_single_pdf(pdf_path: Path, password: str = None) -> Dict:
    """
    Test parsing a single PDF
    
    Returns:
        Dict with test results
    """
    print(f"\n{'='*80}")
    print(f"Testing: {pdf_path.name}")
    print(f"{'='*80}")
    
    try:
        # Parse PDF
        transactions, metadata = pdf_parser.parse_pdf(str(pdf_path), password)
        
        # Calculate stats
        total_transactions = len(transactions)
        unique_ids = len(set(t.get("transaction_id") for t in transactions if t.get("transaction_id")))
        
        # Print metadata
        print(f"\n📄 File: {pdf_path.name}")
        print(f"📏 Size: {pdf_path.stat().st_size / 1024:.2f} KB")
        print(f"📑 Pages: {metadata.get('total_pages', 'Unknown')}")
        print(f"🔍 Parsing Method: {metadata.get('parsing_method', 'Unknown')}")
        print(f"📝 Statement Type: {metadata.get('statement_type', 'Unknown')}")
        
        if metadata.get('errors'):
            print(f"\n⚠️  Errors:")
            for error in metadata['errors']:
                print(f"   - {error}")
        
        print(f"\n✅ Transactions Found: {total_transactions}")
        print(f"🔑 Unique Transaction IDs: {unique_ids}")
        
        # Show sample transactions
        if transactions:
            print(f"\n📊 Sample Transactions (first 5):")
            sample = transactions[:5]
            
            # Format for display
            table_data = []
            for txn in sample:
                table_data.append([
                    txn.get('date', 'N/A'),
                    txn.get('transaction_id', 'N/A')[:10] + '...',
                    txn.get('amount', 'N/A'),
                    (txn.get('description', 'N/A')[:40] + '...') if txn.get('description') and len(txn.get('description', '')) > 40 else txn.get('description', 'N/A'),
                ])
            
            print(tabulate(table_data, headers=['Date', 'Transaction ID', 'Amount', 'Description'], tablefmt='grid'))
        
        # Calculate accuracy estimate
        accuracy = calculate_accuracy_estimate(transactions, metadata)
        print(f"\n🎯 Estimated Accuracy: {accuracy:.1f}%")
        
        return {
            "file": pdf_path.name,
            "success": True,
            "transactions": total_transactions,
            "unique_ids": unique_ids,
            "accuracy": accuracy,
            "pages": metadata.get('total_pages', 0),
            "errors": len(metadata.get('errors', [])),
        }
    
    except Exception as e:
        print(f"\n❌ FAILED: {str(e)}")
        return {
            "file": pdf_path.name,
            "success": False,
            "error": str(e),
            "transactions": 0,
            "accuracy": 0,
        }


def calculate_accuracy_estimate(transactions: List[Dict], metadata: Dict) -> float:
    """
    Estimate parsing accuracy based on data completeness
    
    This is a rough estimate - manual validation needed for real accuracy
    """
    if not transactions:
        return 0.0
    
    total_score = 0
    max_score = 0
    
    for txn in transactions:
        # Check required fields
        max_score += 5
        
        if txn.get('transaction_id'):
            total_score += 1
        if txn.get('date'):
            total_score += 1
        amount_value = txn.get('amount')
        if amount_value is not None:
            try:
                numeric_amount = float(amount_value)
            except (TypeError, ValueError):
                numeric_amount = None
            if numeric_amount is not None and numeric_amount != 0.0:
                total_score += 2  # Amount is critical
        if txn.get('description'):
            total_score += 1
    
    return (total_score / max_score) * 100 if max_score > 0 else 0


def run_all_tests():
    """Run tests on all PDFs in test_pdfs directory"""
    
    # Check if test directory exists
    if not TEST_PDFS_DIR.exists():
        print(f"❌ Test directory not found: {TEST_PDFS_DIR}")
        print(f"\n📁 Creating directory: {TEST_PDFS_DIR}")
        TEST_PDFS_DIR.mkdir(parents=True, exist_ok=True)
        print(f"\n✅ Directory created. Please add your M-Pesa PDFs to:")
        print(f"   {TEST_PDFS_DIR.absolute()}")
        print(f"\n💡 Supported formats:")
        print(f"   - Personal M-Pesa Statement")
        print(f"   - Business M-Pesa Statement")
        print(f"   - Pochi la Biashara Statement")
        return
    
    # Find all PDFs
    pdf_files = list(TEST_PDFS_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print(f"❌ No PDF files found in: {TEST_PDFS_DIR}")
        print(f"\n📁 Please add your M-Pesa PDFs to:")
        print(f"   {TEST_PDFS_DIR.absolute()}")
        return
    
    print(f"🚀 M-PESA PDF PARSER TEST SUITE")
    print(f"{'='*80}")
    print(f"📁 Test Directory: {TEST_PDFS_DIR}")
    print(f"📄 Found {len(pdf_files)} PDF(s)")
    
    # Ask for password once (if needed)
    password = None
    use_password = input("\n🔐 Are any PDFs password-protected? (y/n): ").strip().lower()
    if use_password == 'y':
        password = input("Enter password (usually your ID number): ").strip()
    
    # Test each PDF
    results = []
    for pdf_file in pdf_files:
        result = test_single_pdf(pdf_file, password)
        results.append(result)
    
    # Summary
    print(f"\n\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}")
    
    summary_data = []
    total_transactions = 0
    successful_files = 0
    
    for result in results:
        summary_data.append([
            result['file'],
            '✅' if result['success'] else '❌',
            result.get('transactions', 0),
            f"{result.get('accuracy', 0):.1f}%",
            result.get('pages', 'N/A'),
        ])
        
        if result['success']:
            successful_files += 1
            total_transactions += result.get('transactions', 0)
    
    print(tabulate(summary_data, headers=['File', 'Status', 'Transactions', 'Accuracy', 'Pages'], tablefmt='grid'))
    
    print(f"\n✅ Successfully Parsed: {successful_files}/{len(results)} files")
    print(f"📈 Total Transactions: {total_transactions}")
    
    if results:
        avg_accuracy = sum(r.get('accuracy', 0) for r in results if r['success']) / max(successful_files, 1)
        print(f"🎯 Average Accuracy: {avg_accuracy:.1f}%")
        
        # Decision guidance
        print(f"\n{'='*80}")
        print(f"🧭 DECISION GUIDANCE (for Jan 27 GO/NO-GO):")
        print(f"{'='*80}")
        
        if avg_accuracy >= 90:
            print(f"✅ STRONG GO: {avg_accuracy:.1f}% accuracy exceeds 90% target!")
            print(f"   → Parser is ready for MVP build")
        elif avg_accuracy >= 85:
            print(f"✅ GO: {avg_accuracy:.1f}% accuracy meets 85% minimum target")
            print(f"   → Parser is usable, can improve in Phase 1")
        elif avg_accuracy >= 70:
            print(f"⚠️  YELLOW: {avg_accuracy:.1f}% accuracy below target")
            print(f"   → Need hybrid approach (auto-parse + manual review UI)")
        else:
            print(f"❌ RED: {avg_accuracy:.1f}% accuracy too low")
            print(f"   → Consider API-first approach or more parser development")
        
        print(f"\n💡 Next Steps:")
        print(f"   1. Manually validate sample transactions (check against actual PDF)")
        print(f"   2. Test with 17 more PDFs (target: 20 total for validation)")
        print(f"   3. Document edge cases (date formats, special characters, etc.)")
        print(f"   4. If accuracy <85%: Adjust parser logic or add manual review UI")


def main():
    """Main entry point"""
    
    # Check dependencies
    try:
        import pdfplumber
        import pikepdf
        import pandas
        from tabulate import tabulate
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print(f"\n📦 Install dependencies:")
        print(f"   cd server")
        print(f"   source venv/bin/activate")
        print(f"   pip install -r requirements.txt")
        print(f"   pip install tabulate  # For nice table output")
        sys.exit(1)
    
    run_all_tests()


if __name__ == "__main__":
    main()
