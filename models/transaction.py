from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func

from database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable=False)

    transaction_type = Column(String, nullable=False)

    category = Column(String)

    description = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    account_id = Column(Integer, ForeignKey("accounts.id"))

    user_id = Column(Integer, ForeignKey("users.id"))