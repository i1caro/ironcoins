from main.models import ReadableObject

class MapChart(ReadableObject):
    name = None
    point_class = None
    size_x = None
    size_y = None

    def __init__(self, 
                name, 
                point_class,
                size_x,
                size_y):
        self.name = name
        self.point_class = point_class
        self.size_x = size_x
        self.size_y = size_y

    def __str__(self):
        return 'Map[%s](%s,%s)' % (
                        self.name,
                        self.size_x, 
                        self.size_y)

    def shortest_path(self, origin, destination):
        pass

    




