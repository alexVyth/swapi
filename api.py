"""API Calls for Star Wars API searching"""
from models import People
from utils import get

BASE_URL = 'https://www.swapi.tech/api'


def _query(resource: str, resource_id: str):
    result, cached, cached_time = get(f'{BASE_URL}/{resource}/{resource_id}')
    return result, cached, cached_time


def search_people(search_term):
    """Get person"""
    search_str = f'?name={search_term}'
    results, cached, cached_time = _query('people', search_str)
    results = results.json()['result']
    return (
        list(map(lambda x: People(x['properties']), results)),
        cached,
        cached_time,
    )
