import yaml
from langgraph.graph import StateGraph

from app.nodes.loan_approval_nodes import (
    validate_input, check_eligibility, route_decision,
    notify_user, admin_override, log_result
)

from app.nodes.support_ticket_nodes import (
    validate_ticket, categorize_issue, route_ticket,
    escalate_to_admin, assign_to_agent, close_ticket
)

NODE_MAP = {
    # Loan workflow
    "validate_input": validate_input,
    "check_eligibility": check_eligibility,
    "route_decision": route_decision,
    "notify_user": notify_user,
    "admin_override": admin_override,
    "log_result": log_result,
    # Support ticket workflow
    "validate_ticket": validate_ticket,
    "categorize_issue": categorize_issue,
    "route_ticket": route_ticket,
    "escalate_to_admin": escalate_to_admin,
    "assign_to_agent": assign_to_agent,
    "close_ticket": close_ticket
}

def load_graph_from_yaml(path: str):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    builder = StateGraph(dict)

    # Add nodes
    for node in config["nodes"]:
        builder.add_node(node["id"], NODE_MAP[node["id"]])

    # Set entry point
    builder.set_entry_point(config["nodes"][0]["id"])

    # Separate conditional edges
    conditional_edges = {}
    for edge in config["edges"]:
        if "condition" in edge:
            conditional_edges.setdefault(edge["from"], []).append((edge["to"], edge["condition"]))
        else:
            builder.add_edge(edge["from"], edge["to"])

    # Add conditional edges
    for from_node, targets in conditional_edges.items():
        def router(state, rules=targets):
            for to_node, cond in rules:
                if eval(cond, {}, {"state": state}):
                    return to_node
            return "close_ticket" 

        builder.add_conditional_edges(from_node, router)

    return builder.compile()
