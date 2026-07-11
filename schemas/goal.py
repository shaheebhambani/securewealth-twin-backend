from pydantic import BaseModel


class GoalCreate(BaseModel):
    goal_name: str
    target_amount: float


class GoalResponse(BaseModel):
    id: int
    goal_name: str
    target_amount: float
    saved_amount: float

    class Config:
        from_attributes = True