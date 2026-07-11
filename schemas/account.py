from pydantic import BaseModel


class AccountCreate(BaseModel):
    account_name: str
    account_type: str


class AccountResponse(BaseModel):
    id: int
    account_name: str
    account_type: str
    balance: float
    currency: str

    class Config:
        from_attributes = True