from www.main import session


class Game():
    @classmethod
    def load(cls, id):
        data = session.game.find_one({'_id': id})
        return cls(data)

    def __init__(self, data):
        self.players = {id: Player(id, player) for id, player in data['players'].items()}


class Player():
    def __init__(self, name, side):
        self.name = name
        self.side = side

