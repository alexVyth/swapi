# The Star Wars Python API

Simple Python API implementation for searching [SWAPI](https://www.swapi.tech).

## Installation

Code is tested on a Linux machine with Python 3.9.

To install download the repository and install the python requirements.
Virtual environment creation is recommended.

    git clone https://github.com/alexVyth/swapi.git
    cd swapi
    
    python3 -m venv .venv
    source .venv/bin/activate
    
    pip install --upgrade pip
    pip install -r requirements.txt

## Usage

To search for Star Wars character use:

     python main.py search 'luke sky'

To return world use --world flag:

     python main.py search 'luke sky' --world

The requested information are cached in sqlite using diskcache lib.

To clean the cache use:

     python main.py cache --clean

Also, to inspect the cache use:

     python main.py cache --output
