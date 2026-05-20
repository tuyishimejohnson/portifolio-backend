from typing import List

from fastapi import APIRouter

from app.database.core import DbSession
from app.skills.model import SkillCategory, SkillCreate, SkillResponse
from app.skills import service

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("/categories", response_model=List[str])
async def get_categories():
    return [c.value for c in SkillCategory]


@router.post("/", response_model=SkillResponse, status_code=201)
async def create_skill(skill: SkillCreate, db: DbSession):
    return service.create_skill(skill, db)


@router.get("/", response_model=List[SkillResponse])
async def get_skills(db: DbSession):
    return service.get_skills(db)


@router.get("/{skill_id}", response_model=SkillResponse)
async def get_skill_by_id(skill_id: int, db: DbSession):
    return service.get_skill_by_id(skill_id, db)


@router.put("/{skill_id}", response_model=SkillResponse)
async def update_skill(skill_id: int, skill_data: SkillCreate, db: DbSession):
    return service.update_skill(skill_id, skill_data, db)


@router.delete("/{skill_id}", status_code=204)
async def delete_skill(skill_id: int, db: DbSession):
    return service.delete_skill(skill_id, db)
