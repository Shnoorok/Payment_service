from dynaconf import Dynaconf

DATABASE_URL = "postgresql://user:password@127.0.0.1:5432/payments"

settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
)