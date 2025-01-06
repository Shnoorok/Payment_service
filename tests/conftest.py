import pytest_asyncio
import pytest
from httpx import AsyncClient
# from main import app
from app.core.database import SessionLocal, engine, Base

@pytest.fixture(scope="module")
def test_db():
    # Создание тестовой базы данных
    Base.metadata.create_all(bind=engine)  # Создаем все таблицы
    yield
    Base.metadata.drop_all(bind=engine)  # Удаляем их после завершения тестов

@pytest_asyncio.fixture  # Эта часть важна! Инструктируем Pytest использовать asyncio.
async def async_client(test_db):  # Используем test_db как зависимость
    async with AsyncClient(base_url="http://localhost:8000") as client:
        yield client  # Возвращаем сам клиент

@pytest.fixture(scope="function")
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()