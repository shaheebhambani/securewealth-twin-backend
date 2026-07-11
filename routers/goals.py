from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.goal import Goal
from schemas.goal import GoalCreate

router = APIRouter(
    prefix="/goals",
    tags=["Goals"]
)


@router.post("/create")
def create_goal(data: GoalCreate, db: Session = Depends(get_db)):

    goal = Goal(
        goal_name=data.goal_name,
        target_amount=data.target_amount,
        saved_amount=0,
        user_id=1
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal


@router.get("/")
def get_goals(db: Session = Depends(get_db)):

    goals = db.query(Goal).all()

    result = []

    for goal in goals:

        percentage = 0

        if goal.target_amount > 0:
            percentage = round(
                (goal.saved_amount / goal.target_amount) * 100,
                2
            )

        result.append(
            {
                "id": goal.id,
                "goal_name": goal.goal_name,
                "target_amount": goal.target_amount,
                "saved_amount": goal.saved_amount,
                "progress": f"{percentage}%"
            }
        )

    return result