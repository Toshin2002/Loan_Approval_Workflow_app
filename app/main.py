from fastapi import FastAPI
from pydantic import BaseModel
from app.langgraph_runner import build_graph

app = FastAPI()
graph_executor = build_graph()

class WorkflowInput(BaseModel):
    user_id: str
    loan_amount: float
    income: float
    user_role: str

@app.post("/run-workflow")
async def run_workflow(payload: WorkflowInput):
    result =  graph_executor.invoke(payload.model_dump())
    return result
