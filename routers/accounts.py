from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.account import Account
from models.user import User
from schemas.account import AccountCreate
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post("/create")
def create_account(
    data: AccountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    account = Account(
        account_name=data.account_name,
        account_type=data.account_type,
        balance=data.balance,
        currency=data.currency,
        user_id=current_user.id
    )

    db.add(account)
    db.commit()
    db.refresh(account)

    return account


@router.get("/")
def get_accounts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    accounts = db.query(Account).filter(
        Account.user_id == current_user.id
    ).all()

    return accounts