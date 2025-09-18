from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.yaml_graph_loader import load_graph_from_yaml

app = FastAPI()

# ---------------- Loan Approval Workflow ----------------

class LoanInput(BaseModel):
    user_id: str
    loan_amount: float
    income: Optional[float] = None
    user_role: str

@app.post("/run-loan-approval")
async def run_loan_workflow(payload: LoanInput):
    graph_executor = load_graph_from_yaml("app/graph/loan_approval.yaml")
    result = graph_executor.invoke(payload.model_dump())
    return result

# ---------------- Support Ticket Workflow ----------------

class TicketInput(BaseModel):
    user_id: str
    issue: str

@app.post("/run-support-ticket")
async def run_support_ticket_workflow(payload: TicketInput):
    graph_executor = load_graph_from_yaml("app/graph/support_ticket.yaml")
    result = graph_executor.invoke(payload.model_dump())
    return result
