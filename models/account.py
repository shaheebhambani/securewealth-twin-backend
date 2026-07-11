from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    account_name = Column(String, nullable=False)

    account_type = Column(String, nullable=False)

    balance = Column(Float, default=0)

    currency = Column(String, default="INR")

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="accounts"
    )