from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


dt = {
    "1": "Saket",   
    "2": "Rama",
    "3": "Krishna",
    "4": "Vishnu"
}


class Item(BaseModel):
    key: str
    value: str

@app.get("/message")
def read_root():
    return dt

@app.get("/name")
def read_root():
    return {"Hello":"Rama"}

@app.post("/postname")
def add_item(item: Item):
    dt[item.key] = item.value
    return dt

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Command to run the fastapi in the terminal or powershell is fastapi dev main.py