
class Figure(object):
    name = None
    position = None

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return '%s(%s)' % (self.name, self.position)