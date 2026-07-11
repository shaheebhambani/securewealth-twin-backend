from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models.transaction import Transaction

router = APIRouter(
    prefix="/ai",
    tags=["AI Insights"]
)


@router.get("/summary")
def ai_summary(db: Session = Depends(get_db)):

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

    balance = total_income - total_expense

    top_category = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount).label("total")
        )
        .filter(Transaction.transaction_type == "expense")
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount).desc())
        .first()
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "top_expense_category": top_category[0] if top_category else None,
        "top_expense_amount": top_category[1] if top_category else 0
    }

@router.get("/tips")
def ai_tips(db: Session = Depends(get_db)):

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

    balance = total_income - total_expense

    tips = []

    if total_expense > total_income * 0.7:
        tips.append(
            "⚠️ Your expenses are more than 70% of your income."
        )

    if balance > 0:
        tips.append(
            f"✅ Great! You saved ₹{balance:.2f}."
        )

    highest = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount).label("total")
        )
        .filter(Transaction.transaction_type == "expense")
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount).desc())
        .first()
    )

    if highest:
        tips.append(
            f"💸 Highest spending category: {highest[0]} (₹{highest[1]:.2f})"
        )

    if total_expense == 0:
        tips.append(
            "🎉 No expenses recorded yet!"
        )

    return {
        "tips": tips
    }

@router.get("/monthly")
def monthly_analysis(db: Session = Depends(get_db)):

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

    savings = total_income - total_expense

    if total_income > 0:
        saving_rate = round((savings / total_income) * 100, 2)
    else:
        saving_rate = 0

    return {
        "income": total_income,
        "expense": total_expense,
        "savings": savings,
        "saving_rate": f"{saving_rate}%"
    }

@router.get("/categories")
def category_breakdown(db: Session = Depends(get_db)):

    categories = (
        db.query(
            Transaction.category,
            func.sum(Transaction.amount).label("total")
        )
        .filter(Transaction.transaction_type == "expense")
        .group_by(Transaction.category)
        .all()
    )

    return [
        {
            "category": category,
            "amount": total
        }
        for category, total in categories
    ]

@router.get("/score")
def financial_score(db: Session = Depends(get_db)):

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

    if income == 0:
        score = 0
    else:
        ratio = expense / income

        if ratio < 0.3:
            score = 95
        elif ratio < 0.5:
            score = 85
        elif ratio < 0.7:
            score = 70
        else:
            score = 50

    return {
        "financial_score": score,
        "message": "Higher score means healthier spending habits."
    }