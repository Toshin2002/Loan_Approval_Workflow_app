def validate_input(state: dict) -> dict:
    required_fields = ["user_id", "loan_amount", "income"]
    missing = [field for field in required_fields if field not in state]
    if missing:
        return {"error": f"Missing fields: {', '.join(missing)}"}
    return state
