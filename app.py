from fastapi import FastAPI

# initialize app
app = FastAPI()

# create route and return data to user
@app.get("/")
def read():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)