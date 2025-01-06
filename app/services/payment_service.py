from app.repositories.payment_repository import PaymentRepository
from app.models.payment import Payment, PaymentCreate

class PaymentService:
    def __init__(self, payment_repository: PaymentRepository):
        self.payment_repository = payment_repository

    async def create_payment(self, payment_create: PaymentCreate):
        payment = Payment(amount=payment_create.amount, currency=payment_create.currency)
        return await self.payment_repository.create_payment(payment)

    async def get_payment_status(self, payment_id: str):
        return await self.payment_repository.get_payment_status(payment_id)