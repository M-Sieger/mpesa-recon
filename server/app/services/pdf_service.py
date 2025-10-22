"""
PDF Parsing Service
Extracts M-Pesa transactions from PDF statements
"""
import pdfplumber
import re
from typing import List, Dict, Optional
from datetime import datetime
from decimal import Decimal
import pandas as pd


class PDFParserService:
    """Service for parsing M-Pesa PDF statements"""
    
    def __init__(self):
        # M-Pesa transaction patterns
        self.transaction_patterns = {
            "transaction_id": r"[A-Z0-9]{10,}",  # e.g., RKG7N5QWXT
            "amount": r"KSh?\s?[\d,]+\.?\d*",
            "date": r"\d{1,2}/\d{1,2}/\d{2,4}",
        }
    
    def parse_pdf(self, file_path: str) -> List[Dict]:
        """
        Parse M-Pesa PDF statement and extract transactions
        
        Args:
            file_path: Path to PDF file
            
        Returns:
            List of transaction dictionaries
        """
        transactions = []
        
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    # Extract text
                    text = page.extract_text()
                    
                    # Extract tables (M-Pesa statements often use tables)
                    tables = page.extract_tables()
                    
                    if tables:
                        transactions.extend(self._parse_tables(tables))
                    elif text:
                        transactions.extend(self._parse_text(text))
            
            return transactions
        
        except Exception as e:
            raise Exception(f"PDF parsing failed: {str(e)}")
    
    def _parse_tables(self, tables: List) -> List[Dict]:
        """Parse transactions from PDF tables"""
        transactions = []
        
        for table in tables:
            if not table or len(table) < 2:
                continue
            
            # Convert to DataFrame for easier processing
            df = pd.DataFrame(table[1:], columns=table[0])
            
            # Common M-Pesa column names (case-insensitive matching)
            column_mapping = {
                "receipt": "transaction_id",
                "receipt no": "transaction_id",
                "transaction id": "transaction_id",
                "date": "date",
                "completion time": "time",
                "details": "description",
                "transaction details": "description",
                "paid in": "amount",
                "withdrawn": "amount",
                "amount": "amount",
            }
            
            # Rename columns
            df.columns = df.columns.str.lower().str.strip()
            for old_name, new_name in column_mapping.items():
                if old_name in df.columns:
                    df.rename(columns={old_name: new_name}, inplace=True)
            
            # Extract transactions
            for _, row in df.iterrows():
                transaction = self._extract_transaction_from_row(row)
                if transaction:
                    transactions.append(transaction)
        
        return transactions
    
    def _parse_text(self, text: str) -> List[Dict]:
        """Parse transactions from plain text (fallback)"""
        transactions = []
        lines = text.split("\n")
        
        for line in lines:
            # Try to extract transaction from line
            transaction = self._extract_transaction_from_text(line)
            if transaction:
                transactions.append(transaction)
        
        return transactions
    
    def _extract_transaction_from_row(self, row: pd.Series) -> Optional[Dict]:
        """Extract transaction data from DataFrame row"""
        try:
            # Required fields
            if "transaction_id" not in row or "date" not in row or "amount" not in row:
                return None
            
            transaction_id = str(row.get("transaction_id", "")).strip()
            if not transaction_id or transaction_id.lower() in ["nan", "none", ""]:
                return None
            
            # Parse amount
            amount_str = str(row.get("amount", "0"))
            amount = self._parse_amount(amount_str)
            if amount == 0:
                return None
            
            # Parse date
            date_str = str(row.get("date", ""))
            parsed_date = self._parse_date(date_str)
            if not parsed_date:
                return None
            
            return {
                "transaction_id": transaction_id,
                "date": parsed_date,
                "time": self._parse_time(str(row.get("time", ""))),
                "description": str(row.get("description", "")).strip() or None,
                "amount": amount,
            }
        
        except Exception as e:
            print(f"Error parsing row: {e}")
            return None
    
    def _extract_transaction_from_text(self, text: str) -> Optional[Dict]:
        """Extract transaction from text line (simplified)"""
        # This is a basic implementation - can be enhanced
        transaction_id_match = re.search(self.transaction_patterns["transaction_id"], text)
        amount_match = re.search(self.transaction_patterns["amount"], text)
        date_match = re.search(self.transaction_patterns["date"], text)
        
        if transaction_id_match and amount_match and date_match:
            return {
                "transaction_id": transaction_id_match.group(0),
                "date": self._parse_date(date_match.group(0)),
                "time": None,
                "description": text.strip(),
                "amount": self._parse_amount(amount_match.group(0)),
            }
        
        return None
    
    def _parse_amount(self, amount_str: str) -> Decimal:
        """Parse amount string to Decimal"""
        try:
            # Remove currency symbols and whitespace
            cleaned = re.sub(r"[^\d,.]", "", amount_str)
            # Remove thousands separators
            cleaned = cleaned.replace(",", "")
            return Decimal(cleaned) if cleaned else Decimal("0")
        except:
            return Decimal("0")
    
    def _parse_date(self, date_str: str) -> Optional[str]:
        """Parse date string to ISO format (YYYY-MM-DD)"""
        try:
            date_str = date_str.strip()
            
            # Try common formats
            formats = ["%d/%m/%Y", "%d/%m/%y", "%Y-%m-%d", "%d-%m-%Y"]
            
            for fmt in formats:
                try:
                    dt = datetime.strptime(date_str, fmt)
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    continue
            
            return None
        except:
            return None
    
    def _parse_time(self, time_str: str) -> Optional[str]:
        """Parse time string to HH:MM:SS format"""
        try:
            time_str = time_str.strip()
            if not time_str or time_str.lower() in ["nan", "none"]:
                return None
            
            # Try common formats
            formats = ["%H:%M:%S", "%H:%M", "%I:%M %p"]
            
            for fmt in formats:
                try:
                    dt = datetime.strptime(time_str, fmt)
                    return dt.strftime("%H:%M:%S")
                except ValueError:
                    continue
            
            return None
        except:
            return None


# Global instance
pdf_parser = PDFParserService()
