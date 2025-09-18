import yaml
from langgraph.graph import StateGraph
from app.schema import LoanState
from app.nodes.validate_input import validate_input
from app.nodes.check_eligibility import check_eligibility
from app.nodes.route_decision import route_decision
from app.nodes.notify_user import notify_user
from app.nodes.admin_override import admin_override
from app.nodes.log_result import log_result


NODE_MAP = {
    "validate_input": validate_input,
    "check_eligibility": check_eligibility,
    "route_decision": route_decision,
    "notify_user": notify_user,
    "admin_override": admin_override,
    "log_result": log_result
}

def load_graph_from_yaml(path: str = "app/graph/workflow.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    builder = StateGraph(LoanState)

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
            return None
        builder.add_conditional_edges(from_node, router)

    return builder.compile()
