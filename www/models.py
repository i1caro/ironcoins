from mongokit import Document


class Map(Document):
    __collection__ = 'map'

    structure = {
        'map_matrix': list,
        'creatures': list,
        'borders': list,
        'moves': list
    }
    required_fields = ['map_matrix']
    default_values = {
        'creatures': [],
        'borders': [],
        'moves': []
    }


class Player(Document):
    __collection__ = 'player'

    structure = {
        'id': str,
        'side': str,
        'borders': str,
        'name': unicode,
        'cards': list,
        'resources': {
            'souls': int,
            'fire': int,
            'ichor': int,
            'dark': int,
            'prestige': int
        },
        'creatures': dict
    }
    required_fields = [
        'id', 'side', 'name'
    ]
    default_values = {
        'cards': [],
        'resources.souls': 0,
        'resources.fire': 0,
        'resources.ichor': 0,
        'resources.dark': 0,
        'resources.prestige': 0,
        'creatures': {}
    }


class Creature(Document):
    __collection__ = 'creature'

    structure = {
        'map': str,
        'card': str,
        'name': str,
        'side': str,
        'stats': dict,
        'cards': list
    }
    required_fields = [
        'id', 'card', 'name', 'side', 'stats', 'cards'
    ]
