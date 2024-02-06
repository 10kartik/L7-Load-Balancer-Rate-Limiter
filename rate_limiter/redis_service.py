from redis import StrictRedis
from constants import REDIS_HOST, REDIS_PORT

class RedisService:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=0):
        self.client = StrictRedis(host=host, port=port, db=db)

    def get_client(self):
        return self.client