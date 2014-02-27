class WrongOwner(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ('Piece expected to be in a different owner').format(repr(self.value))

