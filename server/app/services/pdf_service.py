"""PDF Parsing helpers for M-Recon.

Parses M-Pesa PDF statements (including password-protected ones) and returns
structured transaction data plus parsing metadata for downstream processing
and analytics.
"""
from __future__ import annotations

import io
import logging
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

import pandas as pd
import pdfplumber
import pikepdf


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ParsedTransaction:
    """Strongly typed representation of a single parsed transaction."""

    transaction_id: str
    date: str
    time: Optional[str]
    description: Optional[str]
    amount: Decimal


class PDFParserService:
    """Service responsible for parsing M-Pesa statements."""

    def __init__(self) -> None:
        # Regex fallbacks used when a statement does not expose table structures.
        self.transaction_patterns: Dict[str, str] = {
            "transaction_id": r"[A-Z0-9]{10,}",
            "amount": r"(?:KSh?\.?)?\s?[\d,]+\.?\d{0,2}",
            "date": r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def parse_pdf(
        self,
        file_path: str,
        password: Optional[str] = None,
        password_candidates: Optional[Sequence[str]] = None,
    ) -> Tuple[List[Dict], Dict[str, Any]]:
        """Parse a PDF file and return parsed transactions plus metadata."""

        pdf = self._open_pdf(file_path, password, password_candidates)
        transactions: List[ParsedTransaction] = []
        seen_ids: set[str] = set()
        page_methods: List[str] = []
        duplicates_skipped = 0

        total_pages = len(pdf.pages) if hasattr(pdf, "pages") else 0
        metadata: Dict[str, Any] = {
            "file_path": file_path,
            "total_pages": total_pages,
            "parsing_method": "unknown",
            "statement_type": "Unknown",
            "errors": [],
            "table_pages": 0,
            "text_pages": 0,
            "duplicates_skipped": 0,
        }

        try:
            for page_number, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables() or []
                text = page.extract_text() or ""

                if tables:
                    page_transactions = self._parse_tables(tables, page_number, metadata["errors"])
                    metadata["table_pages"] += 1
                    page_methods.append("table")
                else:
                    page_transactions = self._parse_text(text, page_number)
                    metadata["text_pages"] += 1
                    page_methods.append("text")

                if metadata["statement_type"] == "Unknown" and text:
                    detected = self._detect_statement_type(text)
                    if detected:
                        metadata["statement_type"] = detected

                for txn in page_transactions:
                    if txn.transaction_id in seen_ids:
                        duplicates_skipped += 1
                        continue
                    seen_ids.add(txn.transaction_id)
                    transactions.append(txn)
        finally:
            pdf.close()

        metadata["duplicates_skipped"] = duplicates_skipped
        metadata["total_transactions"] = len(transactions)
        metadata["unique_transaction_ids"] = len(seen_ids)
        metadata["parsing_method"] = self._resolve_parsing_method(page_methods)

        return [asdict(txn) for txn in transactions], metadata

    # ------------------------------------------------------------------
    # PDF opening and decryption helpers
    # ------------------------------------------------------------------
    def _open_pdf(
        self,
        file_path: str,
        password: Optional[str],
        password_candidates: Optional[Sequence[str]],
    ) -> pdfplumber.PDF:
        """Open a PDF, trying multiple passwords if supplied."""

        candidates: List[Optional[str]] = []
        if password:
            candidates.append(password)
        if password_candidates:
            candidates.extend(password_candidates)
        if None not in candidates:
            candidates.append(None)

        last_error: Optional[Exception] = None
        for candidate in self._dedupe_preserve_order(candidates):
            try:
                return pdfplumber.open(file_path, password=candidate)
            except pdfplumber.pdf.PDFPasswordError as exc:
                last_error = exc
                logger.debug("Password attempt failed", exc_info=exc)
            except TypeError:
                # Some protected PDFs require full decryption before pdfplumber can read them.
                decrypted_stream = self._decrypt_with_pikepdf(file_path, candidate)
                if decrypted_stream is None:
                    continue
                try:
                    return pdfplumber.open(decrypted_stream)
                except Exception as inner_exc:  # noqa: BLE001
                    last_error = inner_exc
                    logger.debug("Opening decrypted stream failed", exc_info=inner_exc)
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                logger.debug("PDF open error", exc_info=exc)

        message = "Unable to open PDF with supplied passwords" if last_error else "Unable to open PDF"
        raise ValueError(message) from last_error

    def _decrypt_with_pikepdf(
        self, file_path: str, password: Optional[str]
    ) -> Optional[io.BytesIO]:
        """Attempt to decrypt PDF using pikepdf and return an in-memory stream."""

        if not password:
            return None

        try:
            with pikepdf.open(file_path, password=password) as pdf_file:
                buffer = io.BytesIO()
                pdf_file.save(buffer)
                buffer.seek(0)
                return buffer
        except pikepdf.PasswordError:
            logger.debug("pikepdf password error")
            return None
        except Exception:  # noqa: BLE001
            logger.debug("pikepdf failed", exc_info=True)
            return None

    @staticmethod
    def _dedupe_preserve_order(values: Iterable[Optional[str]]) -> Iterator[Optional[str]]:
        seen: set[Optional[str]] = set()
        for value in values:
            if value in seen:
                continue
            seen.add(value)
            yield value

    # ------------------------------------------------------------------
    # Parsing helpers
    # ------------------------------------------------------------------
    def _parse_tables(
        self, tables: List, page_number: int, error_log: List[str]
    ) -> List[ParsedTransaction]:
        transactions: List[ParsedTransaction] = []

        for table in tables:
            if not table or len(table) < 2:
                continue

            df = pd.DataFrame(table[1:], columns=table[0]).replace({None: ""})
            df.columns = df.columns.str.lower().str.strip()

            column_mapping = {
                "receipt": "transaction_id",
                "receipt no": "transaction_id",
                "receipt no.": "transaction_id",
                "receipt number": "transaction_id",
                "transaction id": "transaction_id",
                "transaction number": "transaction_id",
                "trans id": "transaction_id",
                "date": "date",
                "completion time": "date_time",  # Combined date+time field
                "time": "time",
                "details": "description",
                "transaction details": "description",
                "description": "description",
                "narration": "description",
                "transaction status": "status",
                "status": "status",
                "paid in": "credit",
                "paid in (ksh)": "credit",
                "credit": "credit",
                "withdrawn": "debit",
                "withdrawn (ksh)": "debit",
                "debit": "debit",
                "amount": "amount",
            }

            for source, target in column_mapping.items():
                if source in df.columns:
                    df.rename(columns={source: target}, inplace=True)

            for _, row in df.iterrows():
                transaction = self._extract_transaction_from_row(row, page_number, error_log)
                if transaction:
                    transactions.append(transaction)

        return transactions

    def _extract_transaction_from_row(
        self, row: pd.Series, page_number: int, error_log: List[str]
    ) -> Optional[ParsedTransaction]:
        try:
            transaction_id = self._clean_string(row.get("transaction_id"))
            if not transaction_id:
                return None

            # Try combined date_time field first (for "Completion Time" column)
            date_value = self._clean_string(row.get("date_time"))
            if not date_value:
                date_value = self._clean_string(row.get("date"))
            
            # Parse date (may include time)
            parsed_date, parsed_time = self._parse_date_time(date_value)
            if not parsed_date:
                return None

            # Override time if separate time column exists
            time_value = self._clean_string(row.get("time"))
            if time_value:
                parsed_time = self._parse_time(time_value)

            amount = self._resolve_amount_from_row(row)
            if amount is None:
                return None

            description = self._clean_string(row.get("description")) or None

            return ParsedTransaction(
                transaction_id=transaction_id,
                date=parsed_date,
                time=parsed_time,
                description=description,
                amount=amount,
            )
        except Exception as exc:  # noqa: BLE001
            message = f"Row parsing failed on page {page_number}: {exc}"
            error_log.append(message)
            logger.debug(message, exc_info=exc)
            return None

    def _parse_text(self, text: str, page_number: int) -> List[ParsedTransaction]:
        transactions: List[ParsedTransaction] = []

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue

            transaction_id_match = re.search(self.transaction_patterns["transaction_id"], line)
            amount_match = re.search(self.transaction_patterns["amount"], line)
            date_match = re.search(self.transaction_patterns["date"], line)

            if not (transaction_id_match and amount_match and date_match):
                continue

            parsed_date = self._parse_date(date_match.group(0))
            amount = self._parse_amount(amount_match.group(0))
            if not parsed_date or amount is None:
                continue

            transactions.append(
                ParsedTransaction(
                    transaction_id=transaction_id_match.group(0),
                    date=parsed_date,
                    time=None,
                    description=line,
                    amount=amount,
                )
            )
        return transactions

    # ------------------------------------------------------------------
    # Low-level parsing utilities
    # ------------------------------------------------------------------
    def _resolve_amount_from_row(self, row: pd.Series) -> Optional[Decimal]:
        credit = self._parse_amount(row.get("credit"))
        debit = self._parse_amount(row.get("debit"))
        base_amount = self._parse_amount(row.get("amount"))

        if credit is not None and credit != Decimal("0"):
            return credit
        if debit is not None and debit != Decimal("0"):
            return -debit
        return base_amount if base_amount not in (None, Decimal("0")) else None

    def _parse_amount(self, value: object) -> Optional[Decimal]:
        if value is None:
            return None

        text = self._clean_string(value)
        if not text:
            return None

        cleaned = re.sub(r"[^\d.-]", "", text)
        try:
            return Decimal(cleaned)
        except (InvalidOperation, ValueError):
            logger.debug("Could not parse amount from value '%s'", value)
            return None

    def _parse_date(self, value: Optional[str]) -> Optional[str]:
        if not value:
            return None

        value = value.strip()
        # Split if combined date+time (e.g., "2025-08-19 11:36:34")
        if " " in value:
            value = value.split(" ")[0]
        
        formats = ["%Y-%m-%d", "%d/%m/%Y", "%d/%m/%y", "%d-%m-%Y"]
        for fmt in formats:
            try:
                parsed = datetime.strptime(value, fmt)
                return parsed.strftime("%Y-%m-%d")
            except ValueError:
                continue
        logger.debug("Could not parse date from value '%s'", value)
        return None

    def _parse_date_time(self, value: Optional[str]) -> tuple[Optional[str], Optional[str]]:
        """Parse combined date+time field, return (date, time) tuple."""
        if not value:
            return None, None

        value = value.strip()
        
        # Try combined datetime formats
        combined_formats = [
            "%Y-%m-%d %H:%M:%S",
            "%d/%m/%Y %H:%M:%S",
            "%d/%m/%y %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%d/%m/%Y %H:%M",
        ]
        
        for fmt in combined_formats:
            try:
                parsed = datetime.strptime(value, fmt)
                return parsed.strftime("%Y-%m-%d"), parsed.strftime("%H:%M:%S")
            except ValueError:
                continue
        
        # Fallback: try as date only
        date_only = self._parse_date(value)
        return date_only, None

    def _parse_time(self, value: Optional[str]) -> Optional[str]:
        if not value:
            return None

        formats = ["%H:%M:%S", "%H:%M", "%I:%M %p"]
        for fmt in formats:
            try:
                parsed = datetime.strptime(value, fmt)
                return parsed.strftime("%H:%M:%S")
            except ValueError:
                continue
        return None

    @staticmethod
    def _clean_string(value: object) -> str:
        if value is None:
            return ""
        return str(value).strip()

    @staticmethod
    def _resolve_parsing_method(page_methods: Sequence[str]) -> str:
        if not page_methods:
            return "unknown"
        unique_methods = {method for method in page_methods if method}
        if not unique_methods:
            return "unknown"
        if len(unique_methods) == 1:
            return unique_methods.pop()
        return "mixed"

    @staticmethod
    def _detect_statement_type(text: str) -> Optional[str]:
        upper_text = text.upper()
        if "M-PESA STATEMENT" in upper_text:
            return "M-Pesa Statement"
        if "POCHI LA BIASHARA" in upper_text:
            return "Pochi la Biashara Statement"
        if "LIPA NA M-PESA" in upper_text:
            return "Lipa na M-Pesa Statement"
        return None


pdf_parser = PDFParserService()
