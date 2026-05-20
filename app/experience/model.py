import datetime
from enum import Enum

from pydantic import BaseModel, model_validator


class ExperienceStatus(str, Enum):
    current = "current"
    former = "former"


class ExperienceBase(BaseModel):
    status: ExperienceStatus
    company: str
    role: str
    description: str
    start_time: datetime.date
    end_time: datetime.date | None = None


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceResponse(ExperienceBase):
    id: int

    model_config = {"from_attributes": True}
