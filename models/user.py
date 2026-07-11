from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    password = Column(String, nullable=False)

    phone = Column(String, unique=True)

    role = Column(String, default="user")

    is_verified = Column(Boolean, default=False)

    accounts = relationship(
        "Account",
        back_populates="owner"
    )