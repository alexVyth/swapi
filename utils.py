"""Basic utilities for other modules."""
import requests
from diskcache import Cache

CACHE_FILE = '.cache'


def get(url: str) -> requests.Response:
    """HTTP GET request on given url."""
    response = requests.get(url)
    assert response.status_code == 200, 'Resource not available.'

    return response


def add_to_cache(key: tuple[str, bool], value: str) -> None:
    """Add key, value pair to cache."""
    with Cache(CACHE_FILE) as cache:
        cache.add(key, value)


def key_in_cache(key: tuple[str, bool]) -> bool:
    """Checks if key exists in cache."""
    with Cache(CACHE_FILE) as cache:
        return key in cache


def get_cache_value(key: tuple[str, bool]) -> str:
    """Get cache value, given its key."""
    with Cache(CACHE_FILE) as cache:
        return cache.get(key)


def clear_cache() -> None:
    """Clear everything from cache."""
    with Cache(CACHE_FILE) as cache:
        cache.clear()


def get_cache_keys() -> list[Cache.iterkeys]:
    """Get every key from cache."""
    with Cache(CACHE_FILE) as cache:
        return list(cache.iterkeys())
