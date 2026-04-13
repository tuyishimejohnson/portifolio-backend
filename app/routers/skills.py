from fastapi import APIRouter
from app.schemas.skills import Skill

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("/")
async def get_skills(response_model=Skill):
    return Skill(
        category="Programming", skills=["Python", "FastAPI", "SQLAlchemy", "Docker"]
    )


@router.post("/")
async def create_skill(skill: str):
    return {"message": f"Skill '{skill}' created successfully!"}
