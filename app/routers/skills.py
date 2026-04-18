from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import models
from app.schemas.skills import SkillCreate, SkillResponse

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("/", response_model=SkillResponse, status_code=201)
async def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = models.Skill(category=skill.category, skills=skill.skills)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


@router.get("/", response_model=List[SkillResponse])
async def get_skills(db: Session = Depends(get_db)):

    return db.query(models.Skill).all()
