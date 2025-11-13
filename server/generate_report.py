#!/usr/bin/env python3
"""CLI helper to go from PDF → categorised transactions → summary → PDF report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from app.services.categorization_service import categorisation_service
from app.services.pdf_service import pdf_parser
from app.services.report_service import report_service
from app.services.summary_service import summary_service


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate loan-ready financial report from an M-Pesa PDF statement.")
    parser.add_argument("pdf", type=Path, help="Path to the M-Pesa PDF statement")
    parser.add_argument("--password", dest="password", default=None, help="PDF password (usually ID number)")
    parser.add_argument("--output", dest="output", default="loan_ready_report.pdf", help="Output PDF file path")
    parser.add_argument("--member-name", dest="member_name", default="Member", help="Member name for the report header")
    parser.add_argument("--mobile", dest="mobile", default="-", help="Mobile number for the report header")
    parser.add_argument("--email", dest="email", default="-", help="Email address for the report header")
    parser.add_argument("--notes", dest="notes", default=None, help="Optional note to include in the footer")
    parser.add_argument("--summary-json", dest="summary_json", default=None, help="Optional path to dump the financial summary as JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = args.pdf
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    transactions, metadata = pdf_parser.parse_pdf(str(pdf_path), password=args.password)
    categorised = categorisation_service.categorise_transactions(transactions)
    summary = summary_service.generate_summary(categorised)

    report_metadata: Dict[str, Any] = {
        "member_name": args.member_name,
        "mobile": args.mobile,
        "email": args.email,
        "notes": args.notes,
        "statement_type": metadata.get("statement_type"),
        "pages": metadata.get("total_pages"),
    }

    output_path = report_service.build_report(summary, report_metadata, args.output)
    print(f"✅ Report generated: {output_path}")

    if args.summary_json:
        Path(args.summary_json).write_text(json.dumps(summary, default=str, indent=2))
        print(f"📝 Summary JSON saved to: {args.summary_json}")


if __name__ == "__main__":
    main()
