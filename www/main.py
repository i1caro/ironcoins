#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.httpauth import HTTPBasicAuth

import json

auth = HTTPBasicAuth()
app = Flask(__name__)


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def map_view():
    with open('./ironcoins/www/tests/map_view.json') as data_file:
        data = json.load(data_file)
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
