from http.client import HTTPException

from fastapi import APIRouter, HTTPException
from app.services.payment_service import PaymentService
from app.models.payment import PaymentCreate, PaymentResponse

router = APIRouter()
payment_service = PaymentService()

@router.post("/", response_model=PaymentResponse)
async def create_payment(payment: PaymentCreate):
    try:
        payment_id = await payment_service.create_payment(payment)
        return {"payment_id": str(payment_id), "status": "Pending"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment_status(payment_id: str):
    try:
        status = await payment_service.get_payment_status(payment_id)
        return {"payment_id": payment_id, "status": status}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
