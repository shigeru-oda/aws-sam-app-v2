from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
import uuid

class RequestItem(BaseModel):
  name: str
  description: str = None
  price: float

class ResponseItem(BaseModel):
  id: str
  name: str
  description: str = None
  price: float


app = FastAPI()

@app.get("/item", status_code=200, response_model=ResponseItem)
async def read_item(id: str):
  return{
    "id": str(id),
    "name": "read_item+" + str(id),
    "description": "read_item+" + str(id),
    "price": 100.0
  }

@app.post("/item", status_code=201, response_model=ResponseItem)
async def create_item(item:RequestItem):
    create_item = {"id": str(uuid.uuid4())}
    create_item.update(item)
    return create_item

@app.put("/item/{id}", status_code=201, response_model=ResponseItem)
async def update_item(id:str):
  return{
    "id": id,
    "name": "update_item+" + str(id),
    "description": "update_item+" + str(id),
    "price": 200.0
  }

lambda_handler = Mangum(app)