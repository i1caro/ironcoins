from cards.base import play_card
# from cards.exceptions import ErrorCreatureOwner
# from cards.exceptions import CreatureNotFound
# from cards.exceptions import InvalidParameter
from pieces.models import Figure
from game.models import Player
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
    return Player('Player Nar', 'B')


@pytest.fixture
def figure():
    this_figure = Figure('Naruto', 'B')
    return this_figure


@pytest.fixture
def targets():
    return ['Naruto', '5', '3', '5', '4']


# def test_play_card(clean_map, player, figure, targets):
#     card = '444444'
#     clean_map.put_piece(figure, (1, 1))
#     expected = {
#         'card': '444444',
#         'map': [[1, 2], [1, 3]],
#         'creature': [1, 1]
#     }
#     response = play_card(clean_map, player, card, targets)
#     assert response == expected

