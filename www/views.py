from flask.ext.restful import reqparse, Resource

from www.main import session


class GameDisplay(Resource):
    def get(self):
        map_data = session.map.find_one()
        map_data.pop('_id')
        players = dict()
        for player in session.player.find():
            _id = player.pop('_id')
            players[str(_id)] = player
        return {
            'map': map_data,
            'players': players
        }


card_args = reqparse.RequestParser()
card_args.add_argument('targets', type=str, action='append')
card_args.add_argument('card', type=str)
card_args.add_argument('player', type=str)


class PlayCard(Resource):
    def post(self):
        args = card_args.parse_args()
        input_data = {
            'borders': 'clear',
            'cards': ['123444', '123444', '555444', '664446'],
            'creatures': {'123': {'card': '123444',
                                    'cards': ['122222', '233222', None],
                                    'name': 'Soldier',
                                    'side': 'stemput',
                                    'stats': {'life': [10, 0],
                                            'melle_power': [20, 0],
                                            'movement': [2, 0]}},
                            '233': {'card': '124444',
                                     'cards': [None, None, None],
                                     'name': 'Guard',
                                     'side': 'stemput',
                                     'stats': {'life': [12, -8],
                                                'melle_power': [10, 5],
                                                'movement': [2, 0]}}},
            'name': 'Nosferatu',
            'played': [{'card': '444444',
                        'creature': [5, 5],
                        'map': [[5, 4], [5, 3]]}],
            'resources': {'dark': 1,
                           'fire': 5,
                           'ichor': 1,
                           'prestige': 200,
                           'souls': 2},
            'side': 'stemput'
        }
        # data = session.player.find({'_id': args.get('player')}).next()
        # data['cards'].remove(args.get('card'))
        # data.update(input_data)
        session.player.update({'_id': args.get('player')}, input_data)
        return 201
