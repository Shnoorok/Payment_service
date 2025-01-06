from pydantic import BaseModel
from uuid import UUID

class PaymentBase(BaseModel):
    amount: float
    status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: UUID

    class Config:
        orm_mode = True