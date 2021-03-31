"""API Calls for Star Wars API searching"""

import requests

from models import Person
from utils import get

BASE_URL = 'https://www.swapi.tech/api'


def _query(resource: str, resource_id: str) -> requests.Response:
    """SWAPI query given resource type and id. Instead of id
    search term could be given with the appropriate form."""
    response = get(f'{BASE_URL}/{resource}/{resource_id}')
    return response


def search_people(search_term: str) -> list[Person]:
    """Search for people data on SWAPI"""
    search_str = f'?name={search_term}'

    response = _query('people', search_str)
    results = response.json()['result']

    return list(map(lambda x: Person(x['properties']), results))
