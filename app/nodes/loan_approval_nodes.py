def validate_input(state: dict) -> dict:
    state["validated"] = True
    return state

def check_eligibility(state: dict) -> dict:
    income = state.get("income", 0)
    loan_amount = state.get("loan_amount", 0)
    state["eligible"] = income >= loan_amount * 0.5
    return state

def route_decision(state: dict) -> dict:
    return state

def notify_user(state: dict) -> dict:
    state["notification"] = "Loan approved and user notified."
    return state

def admin_override(state: dict) -> dict:
    state["override"] = True
    state["notification"] = "Loan overridden by admin."
    return state

def log_result(state: dict) -> dict:
    state["notification"] = "Loan rejected. Logged for review."
    return state
