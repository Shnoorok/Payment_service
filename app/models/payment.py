from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
import uuid
from app.core.database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)  # Убедитесь, что String импортирован
    status = Column(String, default='Pending')  # Можно оставить или сделать optional в PaymentCreate

class PaymentCreate(BaseModel):
    amount: float
    currency: str
    status: str = 'Pending'  # Значение по умолчанию для создания платежа

class PaymentResponse(BaseModel):
    id: str
    status: str

    class Config:
        orm_mode = True  # Позволяет Pydantic работать с SQLAlchemy моделями