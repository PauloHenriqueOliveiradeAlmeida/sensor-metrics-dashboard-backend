from collections.abc import Callable
from typing import TypeVar, cast
from redis import Redis

from settings import settings

OperationReturn = TypeVar("OperationReturn")


class RedisClient:
    client = None

    def makeOperation[OperationReturn](
        self, operation: Callable[[Redis], OperationReturn]
    ) -> OperationReturn:
        if self.client is None:
            self.__connect()

        operation_result = operation(cast(Redis, self.client))
        self.__disconnect()
        return operation_result

    def __connect(self):
        self.client = Redis(
            host=settings.redis_host, port=settings.redis_port, db=settings.redis_db
        )

    def __disconnect(self):
        if self.client is None:
            return
        self.client.close()
