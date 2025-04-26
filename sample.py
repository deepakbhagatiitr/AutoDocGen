from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def list_users():
    return {"users": []}

@app.post("/items")
async def create_item(item_id: int):
    return {"item_id": item_id}
