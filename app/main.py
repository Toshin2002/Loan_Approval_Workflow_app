from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.yaml_graph_loader import load_graph_from_yaml

app = FastAPI()
graph_executor = load_graph_from_yaml()

class WorkflowInput(BaseModel):
    user_id: str
    loan_amount: float
    income: Optional[float] = None
    user_role: str

@app.post("/run-workflow")
async def run_workflow(payload: WorkflowInput):
    result = graph_executor.invoke(payload.model_dump())
    return result
