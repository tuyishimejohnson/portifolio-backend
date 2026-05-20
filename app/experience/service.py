from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.entities.experience import Experience
from app.experience.model import ExperienceCreate


def create_experience(experience_data: ExperienceCreate, db: Session):
    experience = Experience(
        status=experience_data.status,
        company=experience_data.company,
        role=experience_data.role,
        description=experience_data.description,
        start_time=experience_data.start_time,
        end_time=experience_data.end_time,
    )
    db.add(experience)
    db.commit()
    db.refresh(experience)
    return experience


def get_all_experiences(db: Session):
    return db.query(Experience).all()


def get_experience_by_id(experience_id: int, db: Session):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )
    return experience


def update_experience(experience_id: int, experience_data: ExperienceCreate, db: Session):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )
    experience.status = experience_data.status
    experience.company = experience_data.company
    experience.role = experience_data.role
    experience.description = experience_data.description
    experience.start_time = experience_data.start_time
    experience.end_time = experience_data.end_time
    db.commit()
    db.refresh(experience)
    return experience


def delete_experience(experience_id: int, db: Session):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found"
        )
    db.delete(experience)
    db.commit()
