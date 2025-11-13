"""Financial summary generation for categorised M-Pesa transactions."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional

from dateutil.relativedelta import relativedelta


DECIMAL_ZERO = Decimal("0")
DECIMAL_TWO_PLACES = Decimal("0.01")


@dataclass(frozen=True)
class MonthlyAggregate:
    income: Decimal = DECIMAL_ZERO
    expenses: Decimal = DECIMAL_ZERO
    fees: Decimal = DECIMAL_ZERO
    net: Decimal = DECIMAL_ZERO


class SummaryService:
    """Aggregates categorised transactions into a loan-ready summary."""

    WINDOW_MONTHS = 6

    def generate_summary(self, transactions: List[Dict]) -> Dict[str, Any]:
        processed = self._prepare_transactions(transactions)
        if not processed:
            return self._empty_summary()

        period_start = min(txn["date"] for txn in processed)
        period_end = max(txn["date"] for txn in processed)
        period_months = self._month_span(period_start, period_end)

        # Restrict to the most recent WINDOW_MONTHS months for the loan view.
        window_start_month = self._window_start(period_end)
        filtered = [
            txn
            for txn in processed
            if self._month_floor(txn["date"]) >= window_start_month
        ]
        if not filtered:
            filtered = processed
            window_start_month = self._month_floor(period_start)

        window_months = self._month_span(window_start_month, self._month_floor(period_end))

        aggregates = self._aggregate(filtered)
        monthly_breakdown = self._monthly_breakdown(filtered, window_start_month, period_end)
        trend = self._evaluate_trend(monthly_breakdown)
        loan_capacity = self._calculate_loan_capacity(aggregates, window_months)

        summary: Dict[str, Any] = {
            "period": {
                "start": period_start.isoformat(),
                "end": period_end.isoformat(),
                "months": period_months,
            },
            "window": {
                "start": window_start_month.isoformat(),
                "end": self._month_floor(period_end).isoformat(),
                "months": window_months,
            },
            "income": {
                "business": self._q2(aggregates["income_business"]),
                "personal": self._q2(aggregates["income_personal"]),
                "other": self._q2(aggregates["income_other"]),
                "total": self._q2(aggregates["income_total"]),
                "monthly_average": self._monthly_average(aggregates["income_total"], window_months),
            },
            "expenses": {
                "business": self._q2(aggregates["expense_business"]),
                "personal": self._q2(aggregates["expense_personal"]),
                "withdrawals": self._q2(aggregates["cash_withdrawals"]),
                "fees": self._q2(aggregates["fees"]),
                "total": self._q2(aggregates["expense_total"]),
                "monthly_average": self._monthly_average(aggregates["expense_total"], window_months),
            },
            "cashflow": {
                "net": self._q2(aggregates["net_cashflow"]),
                "monthly_average": self._monthly_average(aggregates["net_cashflow"], window_months),
                "business_net": self._q2(aggregates["business_net"]),
                "trend": trend,
            },
            "loan_capacity": loan_capacity,
            "monthly_breakdown": [
                {
                    "month": month,
                    "income": self._q2(data.income),
                    "expenses": self._q2(data.expenses + data.fees),
                    "fees": self._q2(data.fees),
                    "net": self._q2(data.net),
                }
                for month, data in monthly_breakdown
            ],
        }
        return summary

    # ------------------------------------------------------------------
    # Data preparation & aggregation
    # ------------------------------------------------------------------
    @staticmethod
    def _prepare_transactions(transactions: List[Dict]) -> List[Dict]:
        prepared: List[Dict] = []
        for txn in transactions:
            date_value = txn.get("date")
            amount = txn.get("amount")
            if not date_value or amount is None:
                continue
            try:
                parsed_date = datetime.strptime(str(date_value), "%Y-%m-%d").date()
                parsed_amount = Decimal(amount)
            except (ValueError, TypeError, ArithmeticError):
                continue

            prepared.append(
                {
                    "date": parsed_date,
                    "amount": parsed_amount,
                    "type": txn.get("type", "OTHER"),
                    "category": txn.get("category", "Uncategorised"),
                    "is_business": txn.get("is_business"),
                    "direction": txn.get("direction"),
                }
            )
        return prepared

    def _aggregate(self, transactions: List[Dict]) -> Dict[str, Decimal]:
        totals = defaultdict(Decimal)

        for txn in transactions:
            amount: Decimal = txn["amount"]
            txn_type = txn.get("type", "OTHER").upper()
            is_business = txn.get("is_business")
            category = (txn.get("category") or "").lower()

            if txn_type == "INCOME":
                if is_business:
                    totals["income_business"] += amount
                elif is_business is False:
                    totals["income_personal"] += amount
                else:
                    totals["income_other"] += amount
                totals["income_total"] += amount
            elif txn_type == "EXPENSE":
                absolute_amount = abs(amount)
                if category == "cash withdrawal":
                    totals["cash_withdrawals"] += absolute_amount
                if is_business:
                    totals["expense_business"] += absolute_amount
                else:
                    totals["expense_personal"] += absolute_amount
                totals["expense_total"] += absolute_amount
            elif txn_type == "FEE":
                fee_amount = abs(amount)
                totals["fees"] += fee_amount
                totals["expense_total"] += fee_amount
            elif txn_type == "REVERSAL":
                totals["income_other"] += amount
                totals["income_total"] += amount

        totals.setdefault("income_business", DECIMAL_ZERO)
        totals.setdefault("income_personal", DECIMAL_ZERO)
        totals.setdefault("income_other", DECIMAL_ZERO)
        totals.setdefault("income_total", DECIMAL_ZERO)
        totals.setdefault("expense_business", DECIMAL_ZERO)
        totals.setdefault("expense_personal", DECIMAL_ZERO)
        totals.setdefault("cash_withdrawals", DECIMAL_ZERO)
        totals.setdefault("fees", DECIMAL_ZERO)
        totals.setdefault("expense_total", DECIMAL_ZERO)

        totals["net_cashflow"] = totals["income_total"] - totals["expense_total"]
        totals["business_net"] = totals["income_business"] - (totals["expense_business"] + totals["fees"])
        return totals

    def _monthly_breakdown(
        self, transactions: List[Dict], window_start: date, period_end: date
    ) -> List[tuple[str, MonthlyAggregate]]:
        month_cursor = self._month_floor(window_start)
        end_month = self._month_floor(period_end)
        month_map: Dict[str, MonthlyAggregate] = {}

        while month_cursor <= end_month:
            key = month_cursor.strftime("%Y-%m")
            month_map[key] = MonthlyAggregate()
            month_cursor += relativedelta(months=1)

        for txn in transactions:
            key = self._month_floor(txn["date"]).strftime("%Y-%m")
            stats = month_map.get(key)
            if not stats:
                continue
            income = stats.income
            expenses = stats.expenses
            fees = stats.fees
            amount = txn["amount"]
            txn_type = txn.get("type", "OTHER").upper()

            if txn_type == "INCOME":
                income += amount
            elif txn_type == "EXPENSE":
                expenses += abs(amount)
            elif txn_type == "FEE":
                fee_amount = abs(amount)
                fees += fee_amount

            month_map[key] = MonthlyAggregate(
                income=income,
                expenses=expenses,
                fees=fees,
                net=income - (expenses + fees),
            )

        # Preserve chronological order.
        ordered = sorted(month_map.items(), key=lambda item: item[0])
        return ordered

    def _evaluate_trend(self, monthly_breakdown: List[tuple[str, MonthlyAggregate]]) -> str:
        if len(monthly_breakdown) < 4:
            # Not enough data for a meaningful trend.
            return "insufficient"

        midpoint = len(monthly_breakdown) // 2
        first_half = monthly_breakdown[:midpoint]
        second_half = monthly_breakdown[midpoint:]

        sum_first = sum(entry[1].income for entry in first_half)
        sum_second = sum(entry[1].income for entry in second_half)

        if sum_first == DECIMAL_ZERO:
            return "growing" if sum_second > DECIMAL_ZERO else "insufficient"

        growth_ratio = (sum_second - sum_first) / abs(sum_first)
        if growth_ratio >= Decimal("0.10"):
            return "growing"
        if growth_ratio <= Decimal("-0.10"):
            return "declining"
        return "stable"

    def _calculate_loan_capacity(self, aggregates: Dict[str, Decimal], months: int) -> Dict[str, Any]:
        months = max(months, 1)
        business_net = aggregates["business_net"]
        monthly_business_net = business_net / Decimal(months)

        if monthly_business_net <= DECIMAL_ZERO:
            return {
                "available_monthly": self._q2(DECIMAL_ZERO),
                "recommended_amount": self._q2(DECIMAL_ZERO),
                "confidence": "low",
                "notes": "Business income does not exceed expenses in the assessment window.",
            }

        available = monthly_business_net * Decimal("0.40")
        recommended = available * Decimal("20")

        confidence = "medium"
        if monthly_business_net >= Decimal("20000"):
            confidence = "high"
        elif monthly_business_net <= Decimal("5000"):
            confidence = "low"

        return {
            "available_monthly": self._q2(available),
            "recommended_amount": self._q2(recommended),
            "confidence": confidence,
            "notes": "Calculated from business net income using a conservative 40% servicing ratio.",
        }

    # ------------------------------------------------------------------
    # Utility helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _month_floor(value: date) -> date:
        return date(value.year, value.month, 1)

    def _month_span(self, start: date, end: date) -> int:
        start_month = self._month_floor(start)
        end_month = self._month_floor(end)
        return (end_month.year - start_month.year) * 12 + (end_month.month - start_month.month) + 1

    def _window_start(self, period_end: date) -> date:
        return self._month_floor(period_end) - relativedelta(months=self.WINDOW_MONTHS - 1)

    @staticmethod
    def _q2(amount: Decimal) -> Decimal:
        return amount.quantize(DECIMAL_TWO_PLACES)

    @staticmethod
    def _monthly_average(amount: Decimal, months: int) -> Decimal:
        months = max(months, 1)
        return (amount / Decimal(months)).quantize(DECIMAL_TWO_PLACES)

    def _empty_summary(self) -> Dict[str, Any]:
        return {
            "period": {"start": None, "end": None, "months": 0},
            "window": {"start": None, "end": None, "months": 0},
            "income": {
                "business": DECIMAL_ZERO,
                "personal": DECIMAL_ZERO,
                "other": DECIMAL_ZERO,
                "total": DECIMAL_ZERO,
                "monthly_average": DECIMAL_ZERO,
            },
            "expenses": {
                "business": DECIMAL_ZERO,
                "personal": DECIMAL_ZERO,
                "withdrawals": DECIMAL_ZERO,
                "fees": DECIMAL_ZERO,
                "total": DECIMAL_ZERO,
                "monthly_average": DECIMAL_ZERO,
            },
            "cashflow": {
                "net": DECIMAL_ZERO,
                "monthly_average": DECIMAL_ZERO,
                "business_net": DECIMAL_ZERO,
                "trend": "insufficient",
            },
            "loan_capacity": {
                "available_monthly": DECIMAL_ZERO,
                "recommended_amount": DECIMAL_ZERO,
                "confidence": "low",
                "notes": "No transactions provided.",
            },
            "monthly_breakdown": [],
        }


summary_service = SummaryService()
