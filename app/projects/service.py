from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.entities.projects import Project
from app.projects.model import ProjectCreate


def create_project(project_data: ProjectCreate, db: Session):
    project = Project(
        title=project_data.title,
        period=project_data.period,
        description=project_data.description,
        tags=project_data.tags,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_all_projects(db: Session):
    return db.query(Project).all()


def get_project_by_id(project_id: int, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return project


def update_project(project_id: int, project_data: ProjectCreate, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    project.title = project_data.title
    project.period = project_data.period
    project.description = project_data.description
    project.tags = project_data.tags
    db.commit()
    db.refresh(project)
    return project


def delete_project(project_id: int, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    db.delete(project)
    db.commit()
