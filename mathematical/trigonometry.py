
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
        norm_distance = distance ** 2
        if self.distance(other) >= norm_distance:
            return True
        return False

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

class Vector(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x, self.y = self.calculate_vector()
        self.norm = self.calculate_norm()

    def calculate_vector(self):
        point_dist = self.b - self.a
        return point_dist.x, point_dist.y

    def calculate_norm(self):
        return self.x**2 + self.y**2        

    def __add__(self, other):
        return Vector(Point(0,0), 
            Point(self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Vector(Point(0,0), 
            Point(self.x - other.x, self.y - other.y))

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.norm = self.calculate_norm()

    def __isub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.norm = self.calculate_norm()

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

