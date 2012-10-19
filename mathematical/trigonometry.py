
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, 
                    self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, 
                    self.y - other.y)

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def __isub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def distance(self, other):
        dist = (other.x - self.x)**2
        dist+= (other.y - self.y)**2
        return dist

    def in_distance(self, other, distance):
        item_d = self - other
        distance_d = distance ** 2
        if item_d <= distance_d:
            return True
        return False

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

class Vector(Point):
    pass
