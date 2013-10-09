
class PlotIsFullError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'PlotIsFullError a piece already existed in this plot %s' % repr(self.value)

class NoMoreActionsError(IndexError):
    pass