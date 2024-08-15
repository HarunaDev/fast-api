from fastapi import FastAPI

# initialize app
app = FastAPI()

# create route and return data to user
@app.get("/")
def read():
    return {"hello": "world"}
