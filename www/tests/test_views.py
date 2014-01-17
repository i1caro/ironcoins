from www.main import map_view
import pytest

import json


@pytest.fixture
def map_view_response():
    with open('./ironcoins/www/tests/map_view.json') as data_file:
        return json.load(data_file)


def test_map_view(map_view_response):
    # player_id = 12345
    assert map_view() == map_view_response
