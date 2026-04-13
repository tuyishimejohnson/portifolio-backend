from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    skills = Column(String)
