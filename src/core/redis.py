import redis.asyncio as redis
from ...config.settings import Config

async_redis = redis.from_url(Config.REDIS_URL, decode_responses= True)