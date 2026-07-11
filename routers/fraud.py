from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/fraud",
    tags=["Fraud Detection"]
)


class FraudRequest(BaseModel):
    amount: float
    category: str
    transaction_type: str


@router.post("/check")
def check_fraud(data: FraudRequest):

    risk = "Low"
    reason = []

    if data.amount > 100000:
        risk = "High"
        reason.append("Very high transaction amount.")

    elif data.amount > 50000:
        risk = "Medium"
        reason.append("Large transaction detected.")

    if data.category.lower() == "cash withdrawal":
        reason.append("Cash withdrawals are considered risky.")

    if data.transaction_type.lower() == "expense" and data.amount > 75000:
        reason.append("Unusually large expense.")

    if len(reason) == 0:
        reason.append("Transaction appears normal.")

    return {
        "risk_level": risk,
        "reasons": reason
    }