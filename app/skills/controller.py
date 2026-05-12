from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.core import get_db
from app.skills.model import SkillCreate, SkillResponse
from app.skills import service

router = APIRouter(prefix="/skills", tags=["skills"])


@router.post("/", response_model=SkillResponse, status_code=201)
async def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    return service.create_skill(skill, db)


@router.get("/", response_model=List[SkillResponse])
async def get_skills(db: Session = Depends(get_db)):
    return service.get_skills(db)
