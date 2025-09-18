def validate_ticket(state: dict) -> dict:
    state["validated"] = True
    return state

def categorize_issue(state: dict) -> dict:
    issue = state.get("issue", "").lower()
    if "payment" in issue:
        state["category"] = "billing"
        state["priority"] = "high"
    elif "login" in issue:
        state["category"] = "authentication"
        state["priority"] = "medium"
    else:
        state["category"] = "general"
        state["priority"] = "low"
    # print(state)    
    return state

def route_ticket(state: dict) -> dict:
    return state

def escalate_to_admin(state: dict) -> dict:
    state["action"] = "Escalated to admin"
    return state

def assign_to_agent(state: dict) -> dict:
    state["action"] = "Assigned to support agent"
    # print("passed through agent")
    return state

def close_ticket(state: dict) -> dict:
    state["action"] = "Ticket closed automatically"
    # print(state)
    return state
