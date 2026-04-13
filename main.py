from fastapi import FastAPI
from app.routers import skills
import uvicorn

app = FastAPI()

app.include_router(skills.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
