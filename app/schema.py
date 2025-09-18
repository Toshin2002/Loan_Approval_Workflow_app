from typing import TypedDict, Optional

class LoanState(TypedDict, total=False):
    user_id: str
    loan_amount: float
    income: float
    user_role: str
    eligible: bool
    override: bool
    notification: str
    error: Optional[str]
