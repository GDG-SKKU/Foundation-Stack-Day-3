from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    quantity: int = 0


@app.get("/")
def read_root():
    return {"message": "Hello, Foundation Stack!"}


@app.post("/items")
def create_item(item: Item):
    total = item.price * item.quantity
    return {"item": item.name, "total": total}
