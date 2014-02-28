from cards.base import movement
from cards.exceptions import ErrorCreatureOwner
from cards.exceptions import CreatureNotFound
from cards.exceptions import InvalidParameter
from pieces.models import Figure

from cards.tests.test_base import clean_map, player, figure

import pytest


@pytest.fixture
def path():
    return [[1, 1], [1, 2], [1, 3]]


def test_movement(clean_map, player, figure, path):
    clean_map.put_piece(figure, (1, 1))
    expected = {
        'map': [[1, 2], [1, 3]],
        'creature': [1, 1]
    }
    response = movement(clean_map, player, figure, path)
    assert response == expected


def test_movement_creature_from_another_owner(clean_map, player, path):
    other_owner_figure = Figure('Naruto', 'A')
    with pytest.raises(ErrorCreatureOwner):
        movement(clean_map, player, other_owner_figure, path)


def test_movement_creature_not_on_map(clean_map, player, path):
    other_owner_figure = Figure('Naruto', 'B')
    with pytest.raises(CreatureNotFound):
        movement(clean_map, player, other_owner_figure, path)


def test_movement_not_broken_path(clean_map, figure, player, path):
    clean_map.put_piece(figure, (1, 1))
    with pytest.raises(InvalidParameter):
        movement(clean_map, player, figure, [(1, 1), (1, 4)])


