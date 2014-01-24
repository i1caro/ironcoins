from www.main import api
from www import views
# from www import models

# register routes
api.add_resource(views.GameDisplay, '/game', endpoint='game_view')
api.add_resource(views.PlayCard, '/card', endpoint='play_card')
