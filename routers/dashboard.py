from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models.account import Account
from models.transaction import Transaction

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):

    total_income = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.transaction_type == "income"
    ).scalar() or 0

    total_expense = db.query(
        func.sum(Transaction.amount)
    ).filter(
        Transaction.transaction_type == "expense"
    ).scalar() or 0

    total_balance = total_income - total_expense

    total_accounts = db.query(Account).count()

    recent_transactions = (
        db.query(Transaction)
        .order_by(Transaction.id.desc())
        .limit(5)
        .all()
    )

    return {
        "total_balance": total_balance,
        "total_income": total_income,
        "total_expense": total_expense,
        "total_accounts": total_accounts,
        "recent_transactions": recent_transactions
    }