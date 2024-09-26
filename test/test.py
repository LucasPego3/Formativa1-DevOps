# test_main.py
import pytest
from src.main import formativa1


def test_formativa1_success():
    # Call the function with a known Pokémon name
    result = formativa1('pikachu')

    # Check if the result is not None
    assert result is not None
    # Check if the name in the result matches 'pikachu'
    assert result['name'] == 'pikachu'
    # Check if the id in the result matches 25
    assert result['id'] == 25


def test_formativa1_failure():
    # Call the function with an invalid Pokémon name
    result = formativa1('invalid_pokemon')

    # Check if the result is None for an invalid Pokémon
    assert result is None
