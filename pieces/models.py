class ReadableObject(object):
    def __repr__(self):
        return '%s<%s>'  % (self.__class__.name
            , self.__str__)

class Figure(ReadableObject):
    name = None
    position = None

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return '%s(%s)' % (self.name, self.position)