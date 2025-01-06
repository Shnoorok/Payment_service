import logging
import structlog
import sys


def configure_logging():
    """Настройка структурированного логирования с помощью structlog."""
    # Настройка стандартного логгера
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
        level=logging.INFO,
    )

    # Настройка логирования для Alembic
    alembic_logger = logging.getLogger("alembic")
    alembic_logger.setLevel(logging.INFO)
    alembic_logger.handlers = logging.getLogger().handlers

    # Создание логгера с использованием structlog
    structlog.configure(
        context_class=dict,
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        processors=[
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.KeyValueRenderer(sort_keys=True),  # Читаемый формат
        ],
    )


# Создание логгера
logger = structlog.get_logger()