def log_result(state: dict) -> dict:
    state["notification"] = "Loan rejected. Logged for review."
    return state
