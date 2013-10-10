
class PlotIsFullError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ('PlotIsFullError a piece already'
         'existed in this plot {}').format(repr(self.value))


class NoMoreActionsError(IndexError):
    pass


class PieceDoesNotExist(KeyError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ('The piece {} could not '
                'be found in this map').format(repr(self.value))


