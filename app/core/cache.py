import redis
from app.config import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)

def cache_set(key, value, ex=60):
    r.set(key, value, ex)

def cache_get(key):
    return r.get(key)
