from fastapi import FastAPI

from app.database.core import engine, Base
from app.skills import controller as skills_controller
from app.experience import controller as experience_controller
from app.projects import controller as projects_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio Backend",
    description="REST API for my developer portfolio",
)

app.include_router(skills_controller.router)
app.include_router(experience_controller.router)
app.include_router(projects_controller.router)
