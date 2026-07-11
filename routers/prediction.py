from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models.transaction import Transaction

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.get("/next-month")
def predict_next_month(db: Session = Depends(get_db)):

    income = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.transaction_type == "income"
    ).scalar() or 0

    expense = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.transaction_type == "expense"
    ).scalar() or 0

    predicted_income = round(income * 1.05, 2)

    predicted_expense = round(expense * 1.08, 2)

    predicted_savings = round(
        predicted_income - predicted_expense,
        2
    )

    return {
        "predicted_income": predicted_income,
        "predicted_expense": predicted_expense,
        "predicted_savings": predicted_savings,
        "message": "Prediction based on current spending trend."
    }