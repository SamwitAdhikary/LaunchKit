import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/launchkit")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
