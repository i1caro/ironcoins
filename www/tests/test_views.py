from www.tests.files import inital_map_view, after_move_map_view
from www.models import Map, Player, Creature
from www.main import app
from ming import create_datastore
from ming import Session
from flask import url_for
import pytest
import json


@pytest.fixture
def flask_app():
    app.config['TESTING'] = True
    return app


@pytest.fixture(autouse=True)
def mock_mongo_connection(monkeypatch):
    new_bind = create_datastore('min://localhost:27017/ironcoins')
    monkeypatch.setattr(Session, 'db', new_bind.db)


def base_url(*args, **kwargs):
    with flask_app().test_request_context():
        return url_for(*args, **kwargs)


def test_map_view(flask_app):
    # import ipdb; ipdb.set_trace()

    m = Map(inital_map_view['map'])
    m.m.insert()
    for key, player_data in inital_map_view['players'].items():
        Player(player_data).m.insert()

    map_url = base_url('game_view')
    with flask_app.test_client() as client:
        view = client.get(map_url)
        view_response_dict = json.loads(view.response.next())
        assert view_response_dict == inital_map_view


# def test_play_card(flask_app):
#     card_url = base_url('play_card', card_id='444444')

#     with flask_app.test_client() as client:
#         view = client.post(card_url)
#         assert view.status_code == 200


# def test_map_url_after_card(flask_app, data_store):
#     card_url = base_url('play_card', card_id='444444')
#     map_url = base_url('map_view')
#     data = {
#         'targets': ['333', '1, 1', '1, 2']
#     }
#     with flask_app.test_client() as client:
#         client.post(card_url, data=data)
#         view = client.get(map_url)
#         view_response_dict = json.loads(view.response.next())
#         assert view_response_dict == after_move_map_view
