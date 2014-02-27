from cards.base import movement
from cards.exceptions import WrongOwner
from pieces.models import Figure
from mapchart.models import Player
from mapchart.models import HexMap as Map
from mapchart.constants import GRASS

import pytest


@pytest.fixture
def clean_map():
    clean_map = [[GRASS for y in range(5)]
                 for x in range(5)]
    return Map('clean_map', clean_map)


@pytest.fixture
def player():
    return Player('Player Naruto', 'B')


@pytest.fixture
def figure():
    this_figure = Figure('Naruto', 'B')
    clean_map().put_piece(this_figure, (1, 1))
    return this_figure


@pytest.fixture
def path():
    return Figure('Naruto', 'B')


def test_movement(clean_map, player, figure, path):
    expected = {
        'now': [
            [Figure, 'Naruto', ['stats', 'movement', 'turn_add'], [-2]]
        ],
        'end_turn': [
            [Figure, 'Naruto', ['move'], [(1, 2), (1, 3)]]
        ]
    }
    response = movement(player, figure, path)
    assert response == expected


def test_movement_creature_from_another_owner(clean_map, player, path):
    other_owner_figure = Figure('Naruto', 'A')
    with pytest.raises(WrongOwner):
        movement(player, other_owner_figure, path)


