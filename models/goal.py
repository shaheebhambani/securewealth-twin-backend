from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)

    goal_name = Column(String, nullable=False)

    target_amount = Column(Float, nullable=False)

    saved_amount = Column(Float, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))