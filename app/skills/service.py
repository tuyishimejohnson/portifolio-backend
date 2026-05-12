from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.core import get_db
from app.entities.skills import Skill
from app.skills.model import SkillCreate


def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    new_skill = Skill(category=skill.category, skills=skill.skills)
    existing_skill = (
        db.query(Skill).filter(Skill.category == new_skill.category).first()
    )
    if existing_skill:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Skill already exists"
        )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


def get_skills(db: Session = Depends(get_db)):

    return db.query(Skill).all()


def get_skill_by_id(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Skill not found"
        )

    return skill
