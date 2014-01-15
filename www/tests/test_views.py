from .main import MapView
import pytest


def test_map_view():
    result = {
        'player': {
            id: 111111,
            'side': 'stemput',
            'borders': 'clear',
            'name': 'Nosferatu',
            'cards': [123444, 123444, 444444, 555444, 664446],
            'resources': {
                'souls': 2, 'fire': 5, 'ichor': 1, 'dark': 1, 'prestige': 200,
            },
            'creatures': {
                123: {
                    'card': 123444,
                    'name': 'Soldier',
                    'side': 'stemput',
                    'stats': {'life': (10, 0), 'melle_power': (20, 0), 'movement': (2, 0)},
                    'cards': [122222, 233222, None ]
                },
                233: {
                    'card': 124444,
                    'name': 'Guard',
                    'side': 'stemput',
                    'stats': {'life': (12, -8), 'melle_power': (10, 5), 'movement': (2, 0)},
                    'cards': [None, None, None]
                }
            }
        },
        'opponents': {
            'player1': {
                id: 222222,
                'side': 'snake',
                'borders': 'double',
                'name': 'Papaladum',
                'cards': [000002, 000002, 000002, 000002, 000002],
                'resources': {
                    'souls': 0, 'fire': 0, 'ichor': 0, 'dark': 0, 'prestige': 0,
                },
                'creatures': {}
            },
            'player2': {
                id: 232222,
                'side': 'dragon',
                'borders': 'convex',
                'name': 'Krover',
                'cards': [000002, 000002, 000002, 000002, 000002],
                'resources': {
                    'souls': 0, 'fire': 0, 'ichor': 0, 'dark': 0, 'prestige': 0,
                },
                'creatures': {
                    333: {
                        'card': None,
                        'name': 'Fortress',
                        'side': 'dragon',
                        'stats': {'life': (12, 0), 'melle_power': (10, 0)},
                        'cards': [000002, 000002]
                    }
                }
            }
        },
        'map':
    }
    player_id = 12345
    assert MapView().get(player_id) == result
