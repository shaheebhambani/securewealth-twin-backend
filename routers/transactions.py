from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.transaction import Transaction
from models.account import Account
from schemas.transaction import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/add")
def add_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db)
):
    account = db.query(Account).filter(
        Account.id == data.account_id
    ).first()

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    transaction = Transaction(
        account_id=data.account_id,
        amount=data.amount,
        transaction_type=data.transaction_type,
        category=data.category,
        description=data.description,
        user_id=1
    )

    if data.transaction_type.lower() == "income":
        account.balance += data.amount

    elif data.transaction_type.lower() == "expense":
        account.balance -= data.amount

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()