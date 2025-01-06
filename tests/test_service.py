from app.models.payment import PaymentCreate
from app.repositories import payment_repository
from app.services.payment_service import PaymentService
from app.repositories.payment_repository import PaymentRepository


def test_payment_service_create_payment(db_session):
    payment_service = PaymentService(payment_repository)
    payment_create = PaymentCreate(amount=300.0, currency="USD")

    payment_id = payment_service.create_payment(payment_create)
    assert payment_id is not None

    payment_repo = PaymentRepository(db_session)
    saved_payment = payment_repo.get_payment_status(payment_id)
    assert saved_payment
