"""PDF report generation for loan-ready financial summaries."""
from __future__ import annotations

import secrets
import string
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


DEFAULT_OUTPUT = "loan_ready_report.pdf"


class ReportService:
    """Builds a professional, single-page PDF suitable for SACCO reviewers."""

    def build_report(
        self,
        summary: Dict,
        metadata: Optional[Dict] = None,
        output_path: str | Path = DEFAULT_OUTPUT,
    ) -> str:
        metadata = metadata or {}
        output_path = str(output_path)

        # Generate unique verification code
        verification_code = self._generate_verification_code()
        metadata["verification_code"] = verification_code

        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            topMargin=1.8 * cm,
            bottomMargin=1.6 * cm,
            leftMargin=1.9 * cm,
            rightMargin=1.9 * cm,
        )

        styles = self._build_styles()
        story: List = []

        # Header with verification badge
        story.append(Paragraph("M-Recon Financial Summary Report", styles["ReportTitle"]))
        story.append(Spacer(1, 0.2 * cm))
        story.append(
            Paragraph(
                '<font color="#0B7285">✓</font> <i>This report can be verified</i>',
                styles["VerificationBadge"],
            )
        )
        story.append(Spacer(1, 0.4 * cm))

        story.extend(self._build_metadata_section(summary, metadata, styles))
        story.append(Spacer(1, 0.6 * cm))

        story.extend(self._build_income_section(summary, styles))
        story.append(Spacer(1, 0.4 * cm))
        story.extend(self._build_expense_section(summary, styles))
        story.append(Spacer(1, 0.4 * cm))
        story.extend(self._build_cashflow_section(summary, styles))
        story.append(Spacer(1, 0.4 * cm))
        story.extend(self._build_monthly_breakdown(summary, styles))
        story.append(Spacer(1, 0.5 * cm))
        story.extend(self._build_footer(metadata, styles))

        # Attach verification code to doc for footer callback
        doc._verification_code = metadata.get("verification_code", "N/A")
        doc.build(story, onFirstPage=self._add_page_footer, onLaterPages=self._add_page_footer)
        return output_path

    # ------------------------------------------------------------------
    # Section builders
    # ------------------------------------------------------------------
    def _build_metadata_section(self, summary: Dict, metadata: Dict, styles: StyleSheet1) -> List:
        info_table_data = [
            ["Member", metadata.get("member_name", "[Not Provided]"), "Generated", self._format_date(datetime.utcnow())],
            [
                "Statement Period",
                self._format_period(summary.get("period")),
                "Assessment Window",
                self._format_period(summary.get("window")),
            ],
            ["Mobile", metadata.get("mobile"), "Email", metadata.get("email", "-")],
        ]

        table = Table(info_table_data, colWidths=[3.6 * cm, 7.0 * cm, 3.6 * cm, 4.0 * cm])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                    ("BACKGROUND", (0, 1), (-1, 1), colors.whitesmoke),
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1F2933")),
                    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 0), (-1, -1), 9),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD2D9")),
                    ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD2D9")),
                ]
            )
        )
        return [table]

    def _build_income_section(self, summary: Dict, styles: StyleSheet1) -> List:
        income = summary.get("income", {})
        data = [
            ["Income Analysis", "KES"],
            ["Business Income", self._fmt_currency(income.get("business"))],
            ["Personal Income", self._fmt_currency(income.get("personal"))],
            ["Other Income", self._fmt_currency(income.get("other"))],
            ["Total Income", self._fmt_currency(income.get("total"))],
            ["Average Monthly Income", self._fmt_currency(income.get("monthly_average"))],
        ]
        table = Table(data, colWidths=[8.2 * cm, 8.5 * cm])
        table.setStyle(self._section_table_style())
        return [Paragraph("Income Analysis", styles["SectionHeading"]), table]

    def _build_expense_section(self, summary: Dict, styles: StyleSheet1) -> List:
        expenses = summary.get("expenses", {})
        data = [
            ["Expense Analysis", "KES"],
            ["Business Expenses", self._fmt_currency(expenses.get("business"))],
            ["Personal Expenses", self._fmt_currency(expenses.get("personal"))],
            ["Cash Withdrawals", self._fmt_currency(expenses.get("withdrawals"))],
            ["Transaction Fees", self._fmt_currency(expenses.get("fees"))],
            ["Total Expenses", self._fmt_currency(expenses.get("total"))],
            ["Average Monthly Expenses", self._fmt_currency(expenses.get("monthly_average"))],
        ]
        table = Table(data, colWidths=[8.2 * cm, 8.5 * cm])
        table.setStyle(self._section_table_style())
        return [Paragraph("Expense Analysis", styles["SectionHeading"]), table]

    def _build_cashflow_section(self, summary: Dict, styles: StyleSheet1) -> List:
        cashflow = summary.get("cashflow", {})
        loan = summary.get("loan_capacity", {})
        data = [
            ["Metric", "Value"],
            ["Net Cashflow (Window)", self._fmt_currency(cashflow.get("net"))],
            ["Monthly Net Cashflow", self._fmt_currency(cashflow.get("monthly_average"))],
            ["Business Net Income", self._fmt_currency(cashflow.get("business_net"))],
            ["Income Trend", (cashflow.get("trend") or "-" ).title()],
            ["Available for Loan (per month)", self._fmt_currency(loan.get("available_monthly"))],
            ["Recommended Loan Amount", self._fmt_currency(loan.get("recommended_amount"))],
            ["Confidence", (loan.get("confidence") or "-" ).title()],
        ]

        table = Table(data, colWidths=[8.2 * cm, 8.5 * cm])
        table.setStyle(self._section_table_style())
        notes = loan.get("notes")
        notes_para = []
        if notes:
            notes_para.append(Spacer(1, 0.1 * cm))
            notes_para.append(Paragraph(f"<i>Note:</i> {notes}", styles["NormalSmall"]))
        return [Paragraph("Cashflow & Loan Capacity", styles["SectionHeading"]), table, *notes_para]

    def _build_monthly_breakdown(self, summary: Dict, styles: StyleSheet1) -> List:
        breakdown = summary.get("monthly_breakdown", [])
        if not breakdown:
            return []

        data = [["Month", "Income", "Outflows", "Net"]]
        for item in breakdown[-6:]:  # display last 6 months for brevity
            data.append(
                [
                    item.get("month"),
                    self._fmt_currency(item.get("income")),
                    self._fmt_currency(item.get("expenses")),
                    self._fmt_currency(item.get("net")),
                ]
            )

        table = Table(data, colWidths=[4.0 * cm, 4.0 * cm, 4.0 * cm, 4.7 * cm])
        table_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F0F4F8")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#102A43")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, 0), 9),
                ("FONTSIZE", (0, 1), (-1, -1), 8.5),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD2D9")),
            ]
        )
        table.setStyle(table_style)
        return [Paragraph("Monthly Performance (last 6 months)", styles["SectionHeading"]), table]

    def _build_footer(self, metadata: Dict, styles: StyleSheet1) -> List:
        elements: List = []
        notes = metadata.get("notes")
        if notes:
            elements.append(Paragraph(f"<i>Member Note:</i> {notes}", styles["NormalSmall"]))
            elements.append(Spacer(1, 0.2 * cm))
        elements.append(
            Paragraph(
                "Report generated automatically by M-Recon from the member's M-Pesa statement."
                " All figures are estimates provided for credit-assessment support.",
                styles["NormalSmall"]
            )
        )
        return elements

    # ------------------------------------------------------------------
    # Styling helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _build_styles() -> StyleSheet1:
        styles = getSampleStyleSheet()
        styles.add(
            ParagraphStyle(
                name="SectionHeading",
                parent=styles["Heading2"],
                fontName="Helvetica-Bold",
                fontSize=12,
                textColor=colors.HexColor("#102A43"),
                spaceAfter=6,
            )
        )
        styles.add(
            ParagraphStyle(
                name="NormalSmall",
                parent=styles["BodyText"],
                fontName="Helvetica",
                fontSize=8.5,
                leading=10.5,
                textColor=colors.HexColor("#243B53"),
            )
        )
        styles.add(
            ParagraphStyle(
                name="ReportTitle",
                parent=styles["Title"],
                fontName="Helvetica-Bold",
                fontSize=16,
                textColor=colors.HexColor("#0B7285"),
                alignment=1,
            )
        )
        styles.add(
            ParagraphStyle(
                name="VerificationBadge",
                parent=styles["BodyText"],
                fontName="Helvetica",
                fontSize=9,
                textColor=colors.HexColor("#014D40"),
                alignment=1,
            )
        )
        return styles

    @staticmethod
    def _section_table_style() -> TableStyle:
        return TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E6FFFA")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#014D40")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B6E0FE")),
            ]
        )

    # ------------------------------------------------------------------
    # Misc helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _fmt_currency(value: Optional[Decimal | float | str]) -> str:
        if value is None:
            return "KES 0.00"
        try:
            amount = Decimal(value)
        except (ArithmeticError, ValueError, TypeError):
            return "KES 0.00"
        sign = "-" if amount < 0 else ""
        amount = abs(amount)
        return f"KES {sign}{amount:,.2f}"

    @staticmethod
    def _format_date(value: datetime) -> str:
        return value.strftime("%d %b %Y, %H:%M")

    @staticmethod
    def _format_period(period: Optional[Dict]) -> str:
        if not period or not period.get("start") or not period.get("end"):
            return "-"
        return f"{period['start']} → {period['end']}"

    @staticmethod
    def _add_page_footer(canvas, doc):  # noqa: D401  (signature required by reportlab)
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#486581"))
        
        # Left: Generated by M-Recon
        canvas.drawString(1.9 * cm, 1.0 * cm, "Generated by M-Recon • Confidential")
        
        # Right: Page number
        canvas.drawRightString(A4[0] - 1.9 * cm, 1.0 * cm, f"Page {doc.page}")
        
        # Center: Verification info
        verification_code = getattr(doc, "_verification_code", "N/A")
        verification_text = f"Verification Code: {verification_code} | Verify at: *334# or m-recon.com/verify"
        canvas.setFont("Helvetica-Bold", 7.5)
        canvas.setFillColor(colors.HexColor("#0B7285"))
        canvas.drawCentredString(A4[0] / 2, 0.5 * cm, verification_text)
        
        canvas.restoreState()

    @staticmethod
    def _generate_verification_code() -> str:
        """Generate an 8-character alphanumeric verification code."""
        alphabet = string.ascii_uppercase + string.digits
        return "".join(secrets.choice(alphabet) for _ in range(8))


report_service = ReportService()
