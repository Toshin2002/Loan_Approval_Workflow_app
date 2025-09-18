# 🧠 Workflow Orchestration Engine with LangGraph + FastAPI

This project is a modular, YAML-driven orchestration engine built using [LangGraph](https://github.com/langchain-ai/langgraph), [FastAPI](https://fastapi.tiangolo.com/), and [NetworkX](https://networkx.org/). It enables dynamic execution of multiple workflows with conditional routing, reusable node logic, and visual graph rendering.

---

## 🚀 Features

- ✅ **Multi-Workflow Support**: Easily switch between workflows like loan approval and support ticket routing
- ✅ **YAML-Based Configuration**: Define workflows declaratively using simple YAML files
- ✅ **Modular Node Logic**: Each workflow has its own node module for clean separation
- ✅ **Conditional Routing**: Branch logic based on state values with fallback support
- ✅ **Graph Visualization**: Render workflow graphs using NetworkX and Matplotlib
- ✅ **FastAPI Endpoints**: Dedicated POST routes for each workflow with input validation

---

## 📁 Project Structure

<img width="425" height="179" alt="image" src="https://github.com/user-attachments/assets/cbf33044-f31e-4d0b-8eb3-c9cd270a056d" />


---

## 🧪 Example Workflows

### 🔹 Loan Approval

```json
POST /run-loan-approval
{
  "user_id": "U001",
  "loan_amount": 50000,
  "income": 30000,
  "user_role": "applicant"
}

POST /run-support-ticket
{
  "user_id": "U1001",
  "issue": "I can't log into my account"
}
```
## 📊 Visualize Workflow Graphs  
Render and save PNGs of your workflows:

```bash
python show_graph.py loan_approval
python show_graph.py support_ticket --show

```
## 🛠️ Requirements
See requirements.txt for full list.

## 👨‍💻 Author
Built by Toshin Ghosh — aspiring software developer and workflow architect.
