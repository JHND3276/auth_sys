from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    #App
    DOMAIN: str
    DEBUG: bool = False
    PORT: int = 8000

    #Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    EMAIL_VERIFICATION_TOKEN_EXPIRE_HOURS: int = 24

    DATABASE_URL: str

    #Email
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_SERVER: str
    MAIL_PORT: int = 587
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    #Redis
    REDIS_URL: str

    #RabbitMQ
    RABBITMQ_URL: str

    #Cors
    FRONTEND_URL: str

    class Config:
        env_file= ".env"

Config = Settings()