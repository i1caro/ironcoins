#!flask/bin/python
from flask.ext.restful import Api
from flask import Flask
from flask.ext.mongokit import MongoKit
# from flask.ext.httpauth import HTTPBasicAuth

#Application
# auth = HTTPBasicAuth()

app = Flask(__name__)
app.config.from_object('www.settings')
api = Api(app)
db = MongoKit(app)


if __name__ == '__main__':
    app.run()
