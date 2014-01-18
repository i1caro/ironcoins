#!flask/bin/python
from www.tests.files import inital_map_view
from flask.ext.restful import reqparse, Resource, Api
from flask import Flask
# from flask.ext.httpauth import HTTPBasicAuth


# auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

targets_args = reqparse.RequestParser()
targets_args.add_argument('target', type=str, action='append')


class MapView(Resource):
    def get(self):
        return inital_map_view


class PlayCard(Resource):
    def post(card_id):
        args = targets_args.parse_args()
        return 201


api.add_resource(MapView, '/map', endpoint='map_view')
api.add_resource(PlayCard, '/card', endpoint='play_card')


if __name__ == '__main__':
    app.run(debug=True)
