import os

from redis.client import Redis

REDIS = Redis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    db=int(os.getenv('REDIS_DB')),
    password=os.getenv('REDIS_PASSWORD')
)

DEFAULT_TIMEOUT_SECONDS = 10
