from flask.ext.restful import reqparse, Resource


targets_args = reqparse.RequestParser()
targets_args.add_argument('target', type=str, action='append')


class Map(Resource):
    def get(self):
        from www.tests.files import inital_map_view
        return inital_map_view


class PlayCard(Resource):
    def post(card_id):

        args = targets_args.parse_args()
        # parse args
        # get creature from database because of id
        #
        return 201
