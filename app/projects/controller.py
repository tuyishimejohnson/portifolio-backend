from typing import List

from fastapi import APIRouter

from app.database.core import DbSession
from app.projects.model import ProjectCreate, ProjectResponse
from app.projects import service

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=ProjectResponse, status_code=201)
async def create_project(project: ProjectCreate, db: DbSession):
    return service.create_project(project, db)


@router.get("/", response_model=List[ProjectResponse])
async def get_all_projects(db: DbSession):
    return service.get_all_projects(db)


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project_by_id(project_id: int, db: DbSession):
    return service.get_project_by_id(project_id, db)


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, project_data: ProjectCreate, db: DbSession):
    return service.update_project(project_id, project_data, db)


@router.delete("/{project_id}", status_code=204)
async def delete_project(project_id: int, db: DbSession):
    return service.delete_project(project_id, db)
