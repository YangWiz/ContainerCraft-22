from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/list/{list_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/list/all")
def read_list_all():
    return {"item_id": 1}

@app.post("/list/add")
def add_item(item: Item):
    return {"name": item.name, "content": item.content}

@app.delete("/list/delete/{list_id}")
def delete_item(item_id: int):
    return item_id

@app.put("/list/update")
def update_item(item_id: int, item: Item):
    return {item_id, item}
