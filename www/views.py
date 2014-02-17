from flask.ext.restful import reqparse, Resource

from www.main import session


targets_args = reqparse.RequestParser()
targets_args.add_argument('target', type=str, action='append')


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


class PlayCard(Resource):
    def post(card_id):
        args = targets_args.parse_args()
        # parse args
        # get creature from database because of id
        #
        return 201
