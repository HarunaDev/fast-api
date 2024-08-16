from fastapi import FastAPI, HTTPException
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

# create route to handle post 
@app.post("/tasks/", response_model=Task)
def createTask(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

# create route and return tasks to user
@app.get("/tasks/", response_model=List[Task])
def readTasks():
    return tasks

# create route to return specific task to user
@app.get("/tasks/{task_id}", response_model=Task)
def readTask(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Task not found")

# create route to update task
@app.put("/tasks/{task_id}", response_model=Task)
def updateTask(task_id: UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            # update task and exclude fields that data was not passed for update
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task

    raise HTTPException(status_code=404, detail="Task not found")
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)