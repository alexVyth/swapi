"""Star Wars API search simple implementation."""
from datetime import datetime

import click

import api
from utils import (
    add_to_cache,
    clear_cache,
    get_cache_keys,
    get_cache_value,
    key_in_cache,
)


@click.group()
def cli():
    """SWAPI CLI for searching Star Wars people
    and getting the appropriate information"""


@click.command()
@click.argument('search_term')
@click.option("--world", is_flag=True, default=False)
def search(search_term: str, world: bool) -> None:
    """CLI to search Star Wars characters from SWAPI."""
    key = (search_term, world)
    if key_in_cache(key):
        output, date = get_cache_value(key)
        output += f'\ncached: {date}'
    else:
        output = ''
        people = api.search_people(search_term)
        if people:
            for person in people:
                output += person.get_info()
                if world:
                    homeworld = person.get_homeworld()
                    output += homeworld.get_info()
        else:
            output = 'The force is not strong within you'
        add_to_cache(key, (output, datetime.now()))
    click.echo(output)


@click.command()
@click.option("--clean", is_flag=True, default=False)
@click.option("--output", is_flag=True, default=False)
def cache(clean, output) -> None:
    """Cache command to control output or clean cache memory"""
    if clean:
        clear_cache()
        click.echo('removed cache')

    if output:
        keys = get_cache_keys()
        for key in keys:
            output, date = get_cache_value(key)
            search_term, world = key
            click.echo(f'\nSearch Term: {search_term}')
            click.echo(f'Cache date: {date}')
            click.echo(f'World set to: {world}')
            click.echo(output)


cli.add_command(search)
cli.add_command(cache)

if __name__ == "__main__":
    cli()
