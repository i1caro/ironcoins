class Base(Exception):
    def __init__(self, value):
        self.value = value


class ErrorCreatureOwner(Base):
    def __str__(self):
        return ('Piece expected to be in a different owner: {}').format(repr(self.value))


class CreatureNotFound(Base):
    def __str__(self):
        return ('Creature not on map: {}').format(repr(self.value))


class InvalidParameter(Base):
    def __str__(self):
        return ('Invalid card parameter: {}').format(repr(self.value))
