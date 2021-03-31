"""SWAPI models."""
from utils import get


class People:
    """Representing a single person"""

    def __init__(self, data):
        self.name = data['name']
        self.height = data['height']
        self.mass = data['mass']
        self.birth_year = data['birth_year']
        self.homeworld = data['homeworld']

    def get_homeworld(self):
        response, cached, cached_time = get(self.homeworld)
        return (
            Planet(response.json()['result']['properties']),
            cached,
            cached_time,
        )

    def get_info(self):
        info = (
            f'Name: {self.name}\nHeight: {self.height}\n'
            f'Mass: {self.mass}\nBirth Year: {self.birth_year}'
        )
        return info


class Planet:
    def __init__(self, data: dict):
        self.name = data['name']
        self.population = data['population']
        self.population = data['population']
        self.orbital_period = data['orbital_period']
        self.rotation_period = data['rotation_period']

    def get_info(self) -> str:
        try:
            year_fraction = int(self.orbital_period) / 365
            day_fraction = int(self.rotation_period) / 24
        except ValueError:
            year_fraction = None
            day_fraction = None

        info = (
            '\nHomeworld\n---------\n'
            f'Name: {self.name}\nPopulation: {self.population}'
        )
        if year_fraction and day_fraction:
            info += (
                f'\n\nOn {self.name}, '
                f'1 year on earth is {year_fraction:.2f} years and '
                f'1 day {day_fraction:.2f} days'
            )
        return info
