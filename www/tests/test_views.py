from www.tests.files import inital_map_view, after_move_map_view
from www.main import app
from flask import url_for
import pytest
import json


@pytest.fixture
def flask_app():
    app.config['TESTING'] = True
    return app


def base_url(*args, **kwargs):
    with flask_app().test_request_context():
        return url_for(*args, **kwargs)


def test_map_view(flask_app):
    map_url = base_url('map_view')
    with flask_app.test_client() as client:
        view = client.get(map_url)
        view_response_dict = json.loads(view.response.next())
        assert view_response_dict == inital_map_view


def test_play_card(flask_app):
    card_url = base_url('play_card', card_id='444444')

    with flask_app.test_client() as client:
        view = client.post(card_url)
        assert view.status_code == 200


def test_map_url_after_card(flask_app):
    card_url = base_url('play_card', card_id='444444')
    map_url = base_url('map_view')
    data = {
        'targets': ['333', '1, 1', '1, 2']
    }
    with flask_app.test_client() as client:
        client.post(card_url, data=data)
        view = client.get(map_url)
        view_response_dict = json.loads(view.response.next())
        assert view_response_dict == after_move_map_view
