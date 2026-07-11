from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    role: str

    class Config:
        from_attributes = True