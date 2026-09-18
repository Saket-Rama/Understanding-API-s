from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()
BASE_DIR = Path(__file__).parent


dt = {
    "1": "Saket",   
    "2": "Rama",
    "3": "Krishna",
    "4": "Vishnu"
}


class Item(BaseModel):
    key: str
    value: str


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(BASE_DIR / "index.html")

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