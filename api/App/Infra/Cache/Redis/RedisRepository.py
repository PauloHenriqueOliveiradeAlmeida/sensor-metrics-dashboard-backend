from typing import List, cast

from App.Core.Shared.Repositories.Cache.ICacheRepository import ICacheRepository
from App.Infra.Cache.Redis.RedisClient import RedisClient


class RedisRepository(ICacheRepository):
    client = RedisClient()

    def create(self, key: str, value: float):
        operation = self.client.makeOperation(lambda client: client.rpush(key, value))
        if operation is None:
            return False
        return True

    def get(self, key: str) -> List[float] | None:
        values = self.client.makeOperation(lambda client: client.lrange(key, 0, -1))
        if values is not None:
            return list(map(float, cast(list[bytes], values)))
        return values
