from langgraph.graph import StateGraph
from app.nodes.validate_input import validate_input
from app.nodes.check_eligibility import check_eligibility
from app.nodes.route_decision import route_decision as route_decision_node
from app.nodes.notify_user import notify_user
from app.nodes.admin_override import admin_override
from app.nodes.log_result import log_result
from app.schema import LoanState

def build_graph():
    builder = StateGraph(LoanState)

    # Add nodes
    builder.add_node("validate_input", validate_input)
    builder.add_node("check_eligibility", check_eligibility)
    builder.add_node("route_decision", route_decision_node)
    builder.add_node("notify_user", notify_user)
    builder.add_node("admin_override", admin_override)
    builder.add_node("log_result", log_result)

    # Entry point
    builder.set_entry_point("validate_input")

    # Direct edges
    builder.add_edge("validate_input", "check_eligibility")
    builder.add_edge("check_eligibility", "route_decision")

    # Conditional routing from route_decision
    def route_router(state: dict) -> str:
        if state.get("user_role") == "admin":
            return "admin_override"
        elif state.get("eligible"):
            return "notify_user"
        else:
            return "log_result"

    builder.add_conditional_edges("route_decision", route_router)

    return builder.compile()
