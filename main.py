from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="FastAPI",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
