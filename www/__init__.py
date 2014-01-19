from www.main import api, db
from www import views
from www import models

# register routes
api.add_resource(views.Map, '/map', endpoint='map_view')
api.add_resource(views.PlayCard, '/card', endpoint='play_card')

# register models on the database
db.register([models.Map])
db.register([models.Player])
db.register([models.Creature])
