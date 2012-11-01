class ReadableObject(object):
    def __repr__(self):
        return '%s<%s>'  % (self.__class__.name
            , self.__str__)

