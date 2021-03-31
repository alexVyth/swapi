# The Star Wars Python API

Simple Python API implementation for searching [SWAPI](https://www.swapi.tech).

## Installation

Code is tested on a Linux machine with Python 3.9.

To install download the repository and install the python requirements.
Virtual environment creation is recommended.

```shell
git clone https://github.com/alexVyth/swapi.git
cd swapi

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Usage Guide

To search for Star Wars character use:

```shell
$ python main.py search 'luke sky'

Name: Luke Skywalker
Height: 172
Mass: 77
Birth Year: 19BBY
```

To return homeworld info of character use --world flag:

```shell
$ python main.py search 'luke sky' --world

Name: Luke Skywalker
Height: 172
Mass: 77
Birth Year: 19BBY

Homeworld
---------
Name: Tatooine
Population: 200000

On Tatooine, 1 year on earth is 0.83 years and 1 day 0.96 days
```

## Cache Management

The requested information are cached in sqlite using diskcache lib.

To inspect the cache use:

```raw
$ python main.py cache --output

Search Term: luke
Cache date: 2021-03-31 17:37:53.424728
World set to: True

Name: Luke Skywalker
Height: 172
Mass: 77
Birth Year: 19BBY

Homeworld
---------
Name: Tatooine
Population: 200000

On Tatooine, 1 year on earth is 0.83 years and 1 day 0.96 days


Search Term: yoda
Cache date: 2021-03-31 17:37:59.013830
World set to: False

Name: Yoda
Height: 66
Mass: 17
Birth Year: 896BBY
```

Also, to clean the cache use:

```shell
$ python main.py cache --clean

removed cache
```
