from flask.ext.restful import reqparse, Resource
from www.models import Map, Player, Creature

targets_args = reqparse.RequestParser()
targets_args.add_argument('target', type=str, action='append')


class GameDisplay(Resource):
    def get(self):
        from www.tests.files import inital_map_view
        return inital_map_view
        # map_data = Map(inital_map_view['map'])
        # player0_data = Player(inital_map_view['player0'])
        # player1_data = Player(inital_map_view['player1'])
        # player2_data = Player(inital_map_view['player2'])
        # player3_data = Player(inital_map_view['player3'])
        # return {
        #     'map': map_data,
        #     'player0': player0_data,
        #     'player1': player1_data,
        #     'player2': player2_data,
        #     'player3': player3_data
        # }


class PlayCard(Resource):
    def post(card_id):

        args = targets_args.parse_args()
        # parse args
        # get creature from database because of id
        #
        return 201
