from fastapi import FastAPI

from app.database.core import engine, Base
from app.skills import controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio Backend",
    description="REST API for my developer portfolio",
)

app.include_router(controller.router)
