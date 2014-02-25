from www.tests.files import inital_map_view, after_move_map_view, move_card_map_view
from www import main
from www import views

from pymongo import MongoClient
from flask import url_for
import pytest
import json
import copy


test_session = MongoClient('mongodb://localhost:27017')['tests']


@pytest.fixture(autouse=True)
def flask_app():
    main.app.config['TESTING'] = True
    return main.app


def base_url(*args, **kwargs):
    with flask_app().test_request_context():
        return url_for(*args, **kwargs)


def clean_db():
    for name in test_session.collection_names():
        if name == 'system.indexes':
            continue
        test_session.drop_collection(name)


@pytest.fixture(autouse=True)
def mock_mongo_connection(monkeypatch):
    monkeypatch.setattr(views, 'session', test_session)
    clean_db()


@pytest.fixture()
def initial_data(monkeypatch):
    insert_data = copy.deepcopy(inital_map_view)
    test_session.map.insert(insert_data['map'])
    players = []
    for key, player_data in insert_data['players'].items():
        player_data['_id'] = key
        players.append(player_data)
    test_session.player.insert(players)


def test_map_view(flask_app, initial_data):
    map_url = base_url('game_view')
    with flask_app.test_client() as client:
        view = client.get(map_url)
        view_response_dict = json.loads(view.response.next())
        assert view_response_dict == inital_map_view


def test_play_card(flask_app, initial_data):
    card_url = base_url('play_card')
    map_url = base_url('game_view')

    with flask_app.test_client() as client:
        view = client.post(card_url, data={
            'targets': ['123', '5', '3', '5', '4'],
            'card': '444444',
            'player': '111111'
            })

        assert view.status_code == 200

        map_view = client.get(map_url)
        import ipdb; ipdb.set_trace()
        map_view_response_dict = json.loads(map_view.response.next())
        assert map_view_response_dict == move_card_map_view


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
