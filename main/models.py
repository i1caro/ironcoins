class ReadableObject(object):
    def __repr__(self):
        return self.__str__()
        # return '%s<%s>'  % (self.__class__.name
        #     , self.__str__())
# 
