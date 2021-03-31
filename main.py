"""Star Wars API search simple implementation."""
import click
import requests_cache

import api

requests_cache.install_cache()


@click.group()
def cli():
    """SWAPI CLI function"""


@click.command()
@click.argument('search_term')
@click.option("--world", is_flag=True, default=False)
def search(search_term, world):
    """CLI search command."""
    people, cached, cached_time = api.search_people(search_term)
    if people:
        for i, person in enumerate(people, 1):
            click.echo(person.get_info())

            if world:
                homeworld, _, _ = person.get_homeworld()
                click.echo(homeworld.get_info())

            if cached:
                click.echo(f'\n\ncached: {cached_time}')

            # add empty space if not last item on list
            if not i == len(people):
                click.echo()
    else:
        click.echo('The force is not strong within you')


@click.command()
@click.option("--clean", is_flag=True, default=False)
@click.option("--display", is_flag=True, default=False)
def cache(clean, display):
    """CLI search command."""
    if clean:
        requests_cache.clear()

    if display:
        urls = requests_cache.core.get_cache().urls
        for url in urls:
            if 'people' in url:
                search_term = url.split('name=')[-1]
                people, _, cached_time = api.search_people(search_term)

                for i, person in enumerate(people, 1):
                    click.echo(f'Search Term:{search_term}')
                    click.echo(person.get_info())
                    click.echo(f'\ncached: {cached_time}\n')

                    # add empty space if not last item on list
                    if not i == len(people):
                        click.echo()


cli.add_command(search)
cli.add_command(cache)

if __name__ == "__main__":
    cli()
