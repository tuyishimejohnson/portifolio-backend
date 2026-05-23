from sqlalchemy import Column, Integer, JSON, String

from app.database.core import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    period = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tags = Column(JSON, nullable=False)
