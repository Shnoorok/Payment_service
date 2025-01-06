from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.core.database import Base
import logging

# Ваши настройки базы данных
DATABASE_URL = "postgresql://user:password@127.0.0.1:5432/payments"

# Настройка объекта конфигурации Alembic
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Настройка metadata для автогенерации
target_metadata = Base.metadata

logger = logging.getLogger("alembic.env")

def run_migrations_offline() -> None:
    logger.info("Running migrations in offline mode.")
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

    logger.info("Migrations completed successfully.")

def run_migrations_online() -> None:
    logger.info("Running migrations in online mode.")
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

    logger.info("Migrations completed successfully.")

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()