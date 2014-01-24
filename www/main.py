#!flask/bin/python
from flask.ext.restful import Api
from flask import Flask
from ming import create_datastore, Session


# from flask.ext.httpauth import HTTPBasicAuth

#Application
# auth = HTTPBasicAuth()

app = Flask(__name__)
app.config.from_object('www.settings')
api = Api(app)

bind = create_datastore(
    '{}://{}:{}/{}'.format(
        app.config['MONGODB_CONNECTION'],
        app.config['MONGODB_HOST'],
        app.config['MONGODB_PORT'],
        app.config['MONGODB_DATABASE'],
    )
)
session = Session(bind)


if __name__ == '__main__':
    app.run()
