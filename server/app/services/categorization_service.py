"""Rule-based categorisation for M-Pesa transactions.

The PDF parser produces raw transaction dictionaries.  This service enriches
those records with semantic information (business vs personal, income vs
expense, category, subcategory, confidence level) so downstream services can
create financial summaries and loan-ready reports.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CategorisationResult:
    """Lightweight container for the enriched classification output."""

    type: str
    category: str
    subcategory: str
    is_business: Optional[bool]
    confidence: str


class CategorisationService:
    """Applies a deterministic set of heuristics to classify transactions."""

    # Keyword groups tuned for the common M-Pesa statement vocabulary.
    BUSINESS_INCOME_KEYWORDS = (
        "customer payment",
        "business payment",
        "business to customer",
        "till number",
        "business till",
        "paybill payment",
        "goods and services",
        "received from till",
        "funds received from",
    )

    PERSONAL_INCOME_KEYWORDS = (
        "received from",
        "transfer from",
        "funds received",
        "mpesa received",
    )

    BUSINESS_EXPENSE_KEYWORDS = (
        "pay bill",
        "paybill",
        "buy goods",
        "business payment",
        "customer payment",
        "till number",
        "till payment",
        "goods and services",
        "m-pesa till",
        "kcb mtaani",
        "supplier",
    )

    PERSONAL_EXPENSE_KEYWORDS = (
        "customer transfer",
        "send money",
        "personal",
        "to mom",
        "to dad",
        "to wife",
        "to husband",
        "to brother",
        "to sister",
        "to friend",
        "airtime",
        "bundle",
        "bet",
    )

    CASH_WITHDRAWAL_KEYWORDS = (
        "withdrawal",
        "agent withdrawal",
        "atm withdrawal",
        "m-pesa agent",
        "withdraw",
    )

    FEE_KEYWORDS = (
        "charge",
        "fee",
        "transaction cost",
        "commission",
        "excise duty",
    )

    REVERSAL_KEYWORDS = (
        "reversal",
        "reversed",
        "refund",
    )

    BUSINESS_TRANSFER_THRESHOLD = Decimal("5000")

    def categorise_transactions(self, transactions: List[Dict]) -> List[Dict]:
        """Return a new list of transaction dictionaries with enrichment fields."""

        enriched: List[Dict] = []
        for txn in transactions:
            result = self._categorise_single(txn)
            enriched.append({**txn, **result})
        return enriched

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _categorise_single(self, txn: Dict) -> Dict:
        amount: Decimal = Decimal(txn.get("amount", 0))
        description = (txn.get("description") or "").strip()
        description_lower = description.lower()

        direction = self._resolve_direction(amount)
        base_result = CategorisationResult(
            type="OTHER",
            category="Uncategorised",
            subcategory="Unknown",
            is_business=None,
            confidence="low",
        )

        if direction == "INFLOW":
            result = self._categorise_inflow(description_lower)
        elif direction == "OUTFLOW":
            result = self._categorise_outflow(description_lower, amount)
        else:
            result = self._categorise_neutral(description_lower)

        # Merge with defaults to guarantee all keys.
        merged = {
            "direction": direction,
            "type": result.type or base_result.type,
            "category": result.category or base_result.category,
            "subcategory": result.subcategory or base_result.subcategory,
            "is_business": result.is_business,
            "confidence": result.confidence or base_result.confidence,
        }
        return merged

    @staticmethod
    def _resolve_direction(amount: Decimal) -> str:
        if amount > 0:
            return "INFLOW"
        if amount < 0:
            return "OUTFLOW"
        return "NEUTRAL"

    def _categorise_inflow(self, description: str) -> CategorisationResult:
        # Rule 1: Strong business keywords
        if any(keyword in description for keyword in self.BUSINESS_INCOME_KEYWORDS):
            return CategorisationResult(
                type="INCOME",
                category="Business Income",
                subcategory="Customer Payment",
                is_business=True,
                confidence="high",
            )

        # Rule 2: Generic income references → assume personal unless phone-like pattern.
        if any(keyword in description for keyword in self.PERSONAL_INCOME_KEYWORDS):
            is_business = "254" in description or "business" in description
            return CategorisationResult(
                type="INCOME",
                category="Business Income" if is_business else "Personal Income",
                subcategory="Transfer" if not is_business else "Business Transfer",
                is_business=is_business,
                confidence="medium" if is_business else "low",
            )

        # Default fallback for inflows.
        return CategorisationResult(
            type="INCOME",
            category="Personal Income",
            subcategory="Unclassified",
            is_business=False,
            confidence="low",
        )

    def _categorise_outflow(self, description: str, amount: Decimal) -> CategorisationResult:
        absolute_amount = abs(amount)

        # Fees first (they should not be double-counted as expenses).
        if any(keyword in description for keyword in self.FEE_KEYWORDS):
            return CategorisationResult(
                type="FEE",
                category="Transaction Fee",
                subcategory="M-Pesa Fee",
                is_business=None,
                confidence="high",
            )

        # Cash withdrawals.
        if any(keyword in description for keyword in self.CASH_WITHDRAWAL_KEYWORDS):
            return CategorisationResult(
                type="EXPENSE",
                category="Cash Withdrawal",
                subcategory="Agent/ATM",
                is_business=False,
                confidence="medium",
            )

        # Business expenses via known channels.
        if any(keyword in description for keyword in self.BUSINESS_EXPENSE_KEYWORDS):
            return CategorisationResult(
                type="EXPENSE",
                category="Business Expense",
                subcategory="Operations",
                is_business=True,
                confidence="high",
            )

        # Personal expenses by keyword.
        if any(keyword in description for keyword in self.PERSONAL_EXPENSE_KEYWORDS):
            return CategorisationResult(
                type="EXPENSE",
                category="Personal Expense",
                subcategory="Household",
                is_business=False,
                confidence="medium",
            )

        # Heuristic: generic transfer/unknown descriptions.
        if "customer transfer" in description or "transfer" in description or "send money" in description:
            is_business = absolute_amount >= self.BUSINESS_TRANSFER_THRESHOLD
            return CategorisationResult(
                type="EXPENSE",
                category="Business Expense" if is_business else "Personal Expense",
                subcategory="Supplier Payment" if is_business else "Personal Transfer",
                is_business=is_business,
                confidence="medium" if is_business else "low",
            )

        # Airtime / utilities.
        if "airtime" in description or "bundle" in description:
            return CategorisationResult(
                type="EXPENSE",
                category="Personal Expense",
                subcategory="Airtime/Data",
                is_business=False,
                confidence="medium",
            )

        # Catch-all expense classification.
        return CategorisationResult(
            type="EXPENSE",
            category="Business Expense" if absolute_amount >= self.BUSINESS_TRANSFER_THRESHOLD else "Personal Expense",
            subcategory="Operations" if absolute_amount >= self.BUSINESS_TRANSFER_THRESHOLD else "General",
            is_business=absolute_amount >= self.BUSINESS_TRANSFER_THRESHOLD,
            confidence="low",
        )

    def _categorise_neutral(self, description: str) -> CategorisationResult:
        if any(keyword in description for keyword in self.REVERSAL_KEYWORDS):
            return CategorisationResult(
                type="REVERSAL",
                category="Reversal",
                subcategory="Transaction Reversal",
                is_business=None,
                confidence="medium",
            )

        return CategorisationResult(
            type="OTHER",
            category="Uncategorised",
            subcategory="Unknown",
            is_business=None,
            confidence="low",
        )


categorisation_service = CategorisationService()
