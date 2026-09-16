from fastapi import FastAPI, Request

app = FastAPI()


dict = {
    "1": "Saket",   
    "2": "Rama",
    "3": "Krishna",
    "4": "Vishnu"
}

@app.get("/message")
def read_root():
    return dict

@app.get("/name")
def read_root():
    return {"Hello":"Rama"}

@app.post("/getname")
def read_root(request: Request):
    return {"Hello":"Vikram"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Command to run the fastapi in the terminal or powershell is fastapi dev main.py