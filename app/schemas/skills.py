from pydantic import BaseModel


class Skill(BaseModel):
    category: str
    skills: list[str]
