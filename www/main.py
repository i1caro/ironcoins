from flask import Flask, request
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "Hello World!"


todos = {}
class MapView(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(MapView, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
