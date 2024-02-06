import logging

from oaemlib import Oaem

from app.config import OAEM_CACHE_SIZE

logger = logging.getLogger("root")


class SingletonMeta(type):
    """
    Metaclass for the Singleton pattern.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Cache(metaclass=SingletonMeta):
    """
    Base class for caches.
    The cache is implemented as a dictionary with a maximum size.
    If the maximum size is reached, the oldest item is removed from
    the cache.
    """

    def __init__(self):
        logger.info("Initializing cache")
        self.items = {}

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, key: str) -> bool:
        return key in self.items

    def __getitem__(self, key: str) -> Oaem:
        return self.items[key]

    def __setitem__(self, key: str, value: Oaem) -> None:
        if len(self.items) >= OAEM_CACHE_SIZE:
            self.items.popitem()

        self.items[key] = value

    def __delitem__(self, key: str) -> None:
        del self.items[key]

    def clear(self) -> None:
        self.items.clear()
