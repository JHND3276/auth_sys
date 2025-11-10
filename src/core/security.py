from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from ...config.settings import Config
from .redis import async_redis

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def veryfy_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password : str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expire_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta (minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days= Config.REFRESH_TOKEN_EXPIRE_DAYS)
    return jwt.encode({**data, "exp": expire}, Config.SECRET_KEY, algorithm= Config.ALGORITHM)

async def add_token_to_blacklist(token: str, expires_delta: timedelta):
    await async_redis.setex(f"blacklist:{token}", int(expires_delta.total_seconds()), "1")

async def is_token_blacklisted(token: str) -> bool:
    return await async_redis.exists(f"blacklist:{token}")