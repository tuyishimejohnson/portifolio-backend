from sqlalchemy import Column, Integer, String, JSON, UniqueConstraint

from app.database.core import Base


class Skill(Base):
    __tablename__ = "skills"
    __table_args__ = (UniqueConstraint("category", name="uq_skill_category"),)

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True, nullable=False)
    skills = Column(JSON)
