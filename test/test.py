import pytest
from src.main import formativa1


def test_formativa1_success():
    result = formativa1('pikachu')

    assert result is not None
    assert result['name'] == 'pikachu'
    assert result['id'] == 25


def test_formativa1_fail():
    result = formativa1('invalid_pokemon')
    assert result is None
