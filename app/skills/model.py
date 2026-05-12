from pydantic import BaseModel


class SkillBase(BaseModel):
    category: str
    skills: list[str]


class SkillCreate(SkillBase):
    id: int
    category: str
    skills: list[str]


class SkillResponse(SkillBase):
    id: int

    model_config = {"from_attributes": True}
