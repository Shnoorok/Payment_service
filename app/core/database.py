import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Загрузка URL базы данных из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@127.0.0.1:5432/payments")
print("Database URL: ", DATABASE_URL)

# Создание движка базы данных
engine = create_engine(DATABASE_URL)

# Создание локального класса сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса для декларативных моделей
Base = declarative_base()

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()