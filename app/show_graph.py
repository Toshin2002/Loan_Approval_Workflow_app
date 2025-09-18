import yaml
import networkx as nx
import matplotlib.pyplot as plt
import argparse
import os

def visualize_workflow(yaml_path: str, title: str = "Workflow Graph", save: bool = True):
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)

    G = nx.DiGraph()

    # Add nodes
    for node in config["nodes"]:
        G.add_node(node["id"])

    # Add edges with optional condition labels
    for edge in config["edges"]:
        label = edge.get("condition", "")
        G.add_edge(edge["from"], edge["to"], label=label)

    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color="#87CEFA", node_size=2000, font_size=10, arrows=True)
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8)

    plt.title(title)
    plt.tight_layout()

    if save:
        output_name = os.path.basename(yaml_path).replace(".yaml", "_graph.png")
        output_path = os.path.join("graphs", output_name)
        os.makedirs("graphs", exist_ok=True)
        plt.savefig(output_path)
        print(f"✅ Graph saved to: {output_path}")
    else:
        plt.show()

# ---------------- CLI Support ----------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a workflow graph from YAML")
    parser.add_argument("workflow", type=str, help="Workflow name (e.g. loan_approval or support_ticket)")
    parser.add_argument("--show", action="store_true", help="Show graph instead of saving")

    args = parser.parse_args()
    yaml_file = f"app/graph/{args.workflow}.yaml"

    if not os.path.exists(yaml_file):
        print(f"❌ Workflow YAML not found: {yaml_file}")
    else:
        visualize_workflow(yaml_file, title=f"{args.workflow.replace('_', ' ').title()} Workflow", save=not args.show)
