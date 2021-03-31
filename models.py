"""SWAPI models."""
from utils import get


class Planet:
    """Representing a single Star Wars Planet"""

    def __init__(self, data: dict) -> None:
        self.name = data['name']
        self.population = data['population']
        self.population = data['population']
        self.orbital_period = data['orbital_period']
        self.rotation_period = data['rotation_period']

    def get_info(self) -> str:
        """Get the appropriate planet information."""
        try:
            year_fraction = int(self.orbital_period) / 365
            day_fraction = int(self.rotation_period) / 24
        except ValueError:
            # Unknown / missing planet info
            year_fraction = 0
            day_fraction = 0

        info = (
            '\nHomeworld\n'
            '---------\n'
            f'Name: {self.name}\n'
            f'Population: {self.population}'
        )
        if year_fraction and day_fraction:
            info += (
                f'\n\nOn {self.name}, '
                f'1 year on earth is {year_fraction:.2f} years and '
                f'1 day {day_fraction:.2f} days'
            )
        return info


class Person:
    """Representing a single person"""

    def __init__(self, data: dict) -> None:
        self.name = data['name']
        self.height = data['height']
        self.mass = data['mass']
        self.birth_year = data['birth_year']
        self.homeworld = data['homeworld']

    def get_homeworld(self) -> Planet:
        """Get Homeworld of Person object."""
        response = get(self.homeworld)
        return Planet(response.json()['result']['properties'])

    def get_info(self) -> str:
        """Get the appropriate person information."""
        info = (
            f'\nName: {self.name}\n'
            f'Height: {self.height}\n'
            f'Mass: {self.mass}\n'
            f'Birth Year: {self.birth_year}\n'
        )
        return info
