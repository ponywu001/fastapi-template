import os

from redis import StrictRedis as Redis
from typing import Generator
from src.database.database import SessionLocal


def get_redis_client() -> Generator[Redis, None, None]:
    r = Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', '6379')),
        decode_responses=True
    )
    try:
        yield r
    finally:
        r.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
