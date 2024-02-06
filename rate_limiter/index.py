# import redis_service class from rate_limiter/redis_service.py
# and implement the rate limiting logic for checking, incrementing and resetting the rate limit in the check_rate_limit method.
from rate_limiter.redis_service import RedisService
from constants import RATE_LIMIT_COUNT, RATE_LIMIT_EXPIRY

class RateLimiter:
    def __init__(self):
        self.redis_service = RedisService()
        self.client = self.redis_service.get_client()
        self.max_requests = RATE_LIMIT_COUNT
        self.duration = RATE_LIMIT_EXPIRY

    def check_rate_limit(self, ip):
        print(f'Checking rate limit for {ip}')
        key = f'rate_limit:{ip}'
        current = self.client.get(key)
        if current is None:
            self.client.setex(key, self.duration, 1)
            return True
        if int(current) < self.max_requests:
            self.client.incr(key)
            return True
        return False