"""Basic utilities for other modules."""
import requests


def get(url: str):
    """HTTP GET request on given url."""
    result = requests.get(url)
    assert result.status_code == 200, 'Resource not available.'

    cached = result.from_cache
    cached_time = result.created_at

    return result, cached, cached_time
