from sqlalchemy import Column, Date, Integer, String, UniqueConstraint

from app.database.core import Base


class Experience(Base):
    __tablename__ = "experience"
    __table_args__ = (
        UniqueConstraint("company", "role", "start_time", name="uq_experience_company_role_start"),
    )

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(Date, nullable=False)
    end_time = Column(Date, nullable=True)
