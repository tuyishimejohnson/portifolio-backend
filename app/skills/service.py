from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.entities.skills import Skill
from app.skills.model import SkillCreate


def create_skill(skill: SkillCreate, db: Session):
    existing_skill = db.query(Skill).filter(Skill.category == skill.category).first()
    if existing_skill:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Skill already exists"
        )
    new_skill = Skill(category=skill.category, skills=skill.skills)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


def get_skills(db: Session):
    return db.query(Skill).all()


def get_skill_by_id(skill_id: int, db: Session):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    return skill


def update_skill(skill_id: int, skill_data: SkillCreate, db: Session):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    skill.category = skill_data.category
    skill.skills = skill_data.skills
    db.commit()
    db.refresh(skill)
    return skill


def delete_skill(skill_id: int, db: Session):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )
    db.delete(skill)
    db.commit()
