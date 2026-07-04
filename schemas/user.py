from pydantic import BaseModel, EmailStr


class UserSignup(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str
    monthly_income: float
    monthly_savings: float


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    monthly_income: float
    monthly_savings: float
    risk_profile: str

    class Config:
        from_attributes = True