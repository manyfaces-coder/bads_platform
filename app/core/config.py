from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / "project-root" / ".env"

# Параметры для запуска приложения
class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        case_sensitive=False, # регистр неважен
        env_nested_delimiter="__", # разделитель
        env_prefix="APP_CONFIG__",
        extra="ignore",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

settings = Settings()
