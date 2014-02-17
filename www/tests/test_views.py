from www.tests.files import inital_map_view, after_move_map_view
from www import main

from pymongo import MongoClient
from flask import url_for
import pytest
import json
import copy


@pytest.fixture
def flask_app():
    main.app.config['TESTING'] = True
    return main.app


def clean_db(session):
    for name in session.collection_names():
        if name == 'system.indexes':
            continue
        main.session.drop_collection(name)


@pytest.fixture(autouse=True)
def mock_mongo_connection(monkeypatch):
    new_session = MongoClient('mongodb://localhost:27017')['tests']
    monkeypatch.setattr(main.SingleConnection, '_instance', new_session)
    clean_db(main.session)


def base_url(*args, **kwargs):
    with flask_app().test_request_context():
        return url_for(*args, **kwargs)


def test_map_view(flask_app):
    insert_data = copy.deepcopy(inital_map_view)
    main.session.map.insert(insert_data['map'])
    players = []
    for key, player_data in insert_data['players'].items():
        player_data['_id'] = key
        players.append(player_data)
    main.session.player.insert(players)

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
