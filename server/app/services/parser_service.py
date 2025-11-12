"""
Parser Service
Handles different file types and orchestrates parsing
"""
import csv
from typing import List, Dict
from decimal import Decimal
from datetime import datetime
from app.services.pdf_service import pdf_parser


class ParserService:
    """Main parser service for all file types"""
    
    def parse_file(self, file_path: str, file_type: str) -> List[Dict]:
        """
        Parse file based on type
        
        Args:
            file_path: Path to file
            file_type: File extension (pdf, csv)
            
        Returns:
            List of transaction dictionaries
        """
        if file_type.lower() == "pdf":
            parsed = pdf_parser.parse_pdf(file_path)
            if isinstance(parsed, tuple):
                transactions, _metadata = parsed
            else:
                transactions = parsed
            return transactions
        elif file_type.lower() == "csv":
            return self._parse_csv(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    
    def _parse_csv(self, file_path: str) -> List[Dict]:
        """Parse CSV file"""
        transactions = []
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    transaction = self._extract_transaction_from_csv_row(row)
                    if transaction:
                        transactions.append(transaction)
            
            return transactions
        
        except Exception as e:
            raise Exception(f"CSV parsing failed: {str(e)}")
    
    def _extract_transaction_from_csv_row(self, row: Dict) -> Dict:
        """Extract transaction from CSV row"""
        # Column name mapping (flexible)
        def get_column(names: List[str]) -> str:
            """Get first matching column name"""
            for name in names:
                if name in row:
                    return row[name]
            return ""
        
        transaction_id = get_column([
            "Receipt No.", "Receipt", "Transaction ID", "transaction_id"
        ])
        
        date_str = get_column([
            "Completion Time", "Date", "Transaction Date", "date"
        ])
        
        amount_str = get_column([
            "Paid In", "Withdrawn", "Amount", "amount"
        ])
        
        description = get_column([
            "Details", "Transaction Details", "Description", "description"
        ])
        
        if not transaction_id or not date_str or not amount_str:
            return None
        
        # Parse date
        parsed_date = self._parse_date(date_str)
        if not parsed_date:
            return None
        
        # Parse amount
        amount = self._parse_amount(amount_str)
        if amount == 0:
            return None
        
        return {
            "transaction_id": transaction_id.strip(),
            "date": parsed_date,
            "time": None,  # Extract from date_str if available
            "description": description.strip() or None,
            "amount": amount,
        }
    
    def _parse_amount(self, amount_str: str) -> Decimal:
        """Parse amount string"""
        try:
            cleaned = amount_str.replace(",", "").replace("KSh", "").strip()
            return Decimal(cleaned) if cleaned else Decimal("0")
        except:
            return Decimal("0")
    
    def _parse_date(self, date_str: str) -> str:
        """Parse date string"""
        try:
            # M-Pesa format: "22/10/2025 10:30:45"
            if " " in date_str:
                date_str = date_str.split(" ")[0]
            
            formats = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"]
            
            for fmt in formats:
                try:
                    dt = datetime.strptime(date_str, fmt)
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    continue
            
            return None
        except:
            return None


# Global instance
parser_service = ParserService()
