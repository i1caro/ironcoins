
class PlotIsFullError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ('PlotIsFullError a piece already'
         'existed in this plot {}').format(repr(self.value))


class PlotIsImpassable(PlotIsFullError):
    def __str__(self):
        return ('PlotIsImpassable piece cant move there'
         '{}').format(repr(self.value))


class HexNotConnected(PlotIsFullError):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return ('HexNotConnected: {} not connected to {}'
         '{}').format(self.origin, self.destination)


class NoMoreActionsError(IndexError):
    pass


class PieceDoesNotExist(KeyError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ('The piece {} could not '
                'be found in this map').format(repr(self.value))


