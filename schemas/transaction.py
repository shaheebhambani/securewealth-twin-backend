from pydantic import BaseModel


class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    transaction_type: str
    category: str
    description: str


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: float
    transaction_type: str
    category: str
    description: str

    class Config:
        from_attributes = True