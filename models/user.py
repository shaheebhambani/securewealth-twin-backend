from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    password = Column(String, nullable=False)

    phone = Column(String, nullable=True)

    monthly_income = Column(Float, default=0)

    monthly_savings = Column(Float, default=0)

    risk_profile = Column(String, default="Moderate")

    created_at = Column(DateTime, default=datetime.utcnow)