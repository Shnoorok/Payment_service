from sqlalchemy.ext.asyncio import AsyncSession
from app.models.payment import Payment

class PaymentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_payment(self, payment: Payment):
        self.db.add(payment)  # Здесь db должен быть экземпляром AsyncSession
        await self.db.commit()  # Не забудьте выполнить коммит
        await self.db.refresh(payment)  # Свежее состояние объекта
        return payment.id

    class PaymentRepository:

        async def get_payment_status(self, payment_id):
            # код для получения статуса платежа
            async with self.db() as session:
                payment = await session.get(Payment, payment_id)
                if payment:
                    return payment.status
                return None

    async def get_payment_status(self, payment_id):
        pass