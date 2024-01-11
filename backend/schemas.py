from pydantic import BaseModel

class Item(BaseModel):
    name: str
    content: str
    complete: bool
