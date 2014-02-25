from flask.ext.restful import reqparse, Resource
from bson.objectid import ObjectId

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
            'played': {
                'card': '444444',
                'map': [[5, 4], [5, 3]],
                'creature': [5, 5]
            }
        }
        data = session.player.find({'_id': args.get('player')}).next()
        data['cards'].remove(args.get('card'))
        data.update(input_data)
        session.player.update({'_id': args.get('player')}, data)
        return 201
