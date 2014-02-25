#!flask/bin/python
from flask.ext.restful import Api
from flask import Flask
from pymongo import MongoClient
from www.settings import CONNECTION
from www.settings import MONGODB_DATABASE
# from flask.ext.httpauth import HTTPBasicAuth

#Application
# auth = HTTPBasicAuth()
app = Flask(__name__)
app.config.from_object('www.settings')
api = Api(app)


# class SingleConnection(MongoClient):
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(SingleConnection, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

session = MongoClient(CONNECTION)[MONGODB_DATABASE]

if __name__ == '__main__':
    app.run()
