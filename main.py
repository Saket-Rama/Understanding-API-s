from fastapi import FastAPI

app = FastAPI()


@app.get("/message")
def read_root():
    return {"Hello": "Saket"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Command to run the fastapi in the terminal or powershell is fastapi dev main.py