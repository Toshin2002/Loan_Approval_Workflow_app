def check_eligibility(state: dict) -> dict:
    income = state.get("income", 0)
    loan_amount = state.get("loan_amount", 0)
    state["eligible"] = income >= loan_amount * 0.5
    return state
