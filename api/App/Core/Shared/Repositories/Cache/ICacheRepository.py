from abc import abstractmethod
from typing import List, Protocol


class ICacheRepository(Protocol):
    @abstractmethod
    def create(self, key: str, value: float) -> bool:
        pass

    @abstractmethod
    def get(self, key: str) -> List[float] | None:
        pass
