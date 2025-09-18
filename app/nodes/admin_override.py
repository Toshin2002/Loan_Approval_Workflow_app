def admin_override(state: dict) -> dict:
    state["override"] = True
    state["notification"] = "Loan manually approved by admin."
    return state
