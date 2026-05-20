from enum import Enum

from pydantic import BaseModel


class SkillCategory(str, Enum):
    languages = "Languages and Frameworks"
    machine_learning = "Machine Learning and Data Science"
    web_development = "Websites and Styling"
    devops = "Tools and DevOps"
    soft_skills = "Soft Skills"


class SkillBase(BaseModel):
    category: SkillCategory
    skills: list[str]


class SkillCreate(SkillBase):
    pass


class SkillResponse(SkillBase):
    id: int

    model_config = {"from_attributes": True}
