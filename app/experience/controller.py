from typing import List

from fastapi import APIRouter

from app.database.core import DbSession
from app.experience.model import ExperienceCreate, ExperienceResponse
from app.experience import service

router = APIRouter(prefix="/experience", tags=["experience"])


@router.post("/", response_model=ExperienceResponse, status_code=201)
async def create_experience(experience: ExperienceCreate, db: DbSession):
    return service.create_experience(experience, db)


@router.get("/", response_model=List[ExperienceResponse])
async def get_all_experiences(db: DbSession):
    return service.get_all_experiences(db)


@router.get("/{experience_id}", response_model=ExperienceResponse)
async def get_experience_by_id(experience_id: int, db: DbSession):
    return service.get_experience_by_id(experience_id, db)


@router.put("/{experience_id}", response_model=ExperienceResponse)
async def update_experience(
    experience_id: int, experience_data: ExperienceCreate, db: DbSession
):
    return service.update_experience(experience_id, experience_data, db)


@router.delete("/{experience_id}", status_code=204)
async def delete_experience(experience_id: int, db: DbSession):
    return service.delete_experience(experience_id, db)
