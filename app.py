from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

# initialize app
app = FastAPI()

# create list to store task
tasks = []

# create object to convert data sent to json
class Task(BaseModel):
    # specify fields with data
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# create route and return data to user
@app.get("/")
def read():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)