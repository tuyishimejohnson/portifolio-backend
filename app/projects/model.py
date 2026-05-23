from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    period: str
    description: str
    tags: list[str]


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int

    model_config = {"from_attributes": True}
