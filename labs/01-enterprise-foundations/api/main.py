from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from policy import determine_workflow

app = FastAPI()


class ProductRequest(BaseModel):
    request_type: Literal["feature", "bug", "security", "compliance"]
    description: str = Field(min_length=10, max_length=500)


@app.get("/")
def read_root():
    return {
        "service": "Enterprise AI Product Builder API",
        "status": "running"
    }


@app.post("/requests")
def create_request(request: ProductRequest):
    workflow = determine_workflow(request.request_type)
    return {
        "request_type": request.request_type,
        "description": request.description,
        "status": "received",
        "workflow": workflow
    }