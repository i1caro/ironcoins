from www.tests.test_views import test_session, clean_db
from www.tests.files import inital_map_view
from game.models import Game

import pytest
import copy


@pytest.fixture()
def mock_mongo_connection(monkeypatch):
    monkeypatch.setattr('game.models.session', test_session)
    clean_db()


@pytest.fixture()
def save_games():
    new_map = copy.deepcopy(inital_map_view)
    new_map['_id'] = '1234'
    test_session.game.insert(new_map)


def test_load_game(mock_mongo_connection, save_games):
    game = Game.load('1234')
    assert len(game.players) == 4


def test_game():
    game = Game(inital_map_view)
    assert len(game.players) == 4

