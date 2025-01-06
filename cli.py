from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from app.core.database import Base, engine
# from app.config.settings import settings
from app.core.log_config import configure_logging
from alembic.config import Config
from alembic import command
import structlog
import uuid

# Настройка логгирования
configure_logging()
logger = structlog.get_logger()

# Создание маршрутизатора для платежей
payments_router = APIRouter()


# Определение модели платежа
class PaymentCreate(BaseModel):
    amount: float
    currency: str


# Хранилище платежей (временное решение для хранения)
payments_db = {}


@payments_router.post("/")
async def create_payment(payment: PaymentCreate):
    """Обработчик запроса на создание платежа."""
    payment_id = str(uuid.uuid4())  # Генерация уникального ID платежа
    payments_db[payment_id] = {
        "amount": payment.amount,
        "currency": payment.currency,
        "status": "Pending"
    }
    logger.info(f"Создан платеж: {payment_id}")
    return {"payment_id": payment_id, "status": "Pending"}


@payments_router.get("/{payment_id}")
async def get_payment_status(payment_id: str):
    """Обработчик запроса на получение статуса платежа."""
    payment = payments_db.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    logger.info(f"Запрос статуса платежа: {payment_id}")
    return {"payment_id": payment_id, "status": payment["status"]}


async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения."""
    logger.info("Приложение запускается...")

    alembic_cfg = Config("alembic.ini")

    try:
        logger.info("Начало применения миграций...")
        command.upgrade(alembic_cfg, "head")
        logger.info("Миграции успешно применены.")
    except Exception as e:
        logger.error("Ошибка при применении миграций", error=str(e))
        raise

    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Все необходимые таблицы успешно созданы.")
    except Exception as e:
        logger.error("Ошибка при создании таблиц", error=str(e))
        raise

    yield


# Инициализация приложения FastAPI с указанной функцией lifespan
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    """Обработчик корневого запроса."""
    logger.info("Запрос к корневому эндпоинту.")
    return {"message": "Это МОК API service"}


# Подключение маршрутизатора для платежей с префиксом
app.include_router(payments_router, prefix="/payments", tags=["payments"])

if __name__ == "__main__":
    import uvicorn

    logger.info("Запуск приложения на http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
