from main.models import ReadableObject
import math
import copy

class Point(ReadableObject):
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

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

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

class Hex(Point):
    @property
    def side_north_west(self):
        return Hex(self.x-1,self.y)
    @property
    def side_north(self):
        return Hex(self.x,self.y+1)
    @property
    def side_north_east(self):
        return Hex(self.x+1,self.y)
    @property
    def side_south_east(self):
        return Hex(self.x+1,self.y-1)
    @property
    def side_south(self):
        return Hex(self.x,self.y-1)
    @property
    def side_south_west(self):
        return Hex(self.x-1,self.y-1)

    def children(self):
        yield self.side_north_west
        yield self.side_north
        yield self.side_north_east
        yield self.side_south_east
        yield self.side_south
        yield self.side_south_west

class Vector(ReadableObject):
    def __init__(self, origin, destination=None):
        if origin and destination:
            self.origin = origin
            self.destination = destination
        else:
            self.origin = Point(0,0)
            self.destination = origin
        self.x, self.y = self.calculate_vector()
        self.norm = self.calculate_norm()

    def calculate_vector(self):
        point_dist = self.destination - self.origin
        return point_dist.x, point_dist.y

    def calculate_norm(self):
        return self.x**2 + self.y**2        

    def __add__(self, other):
        return Vector(Point(self.x + other.x, 
                    self.y + other.y))

    def __sub__(self, other):
        return Vector(Point(self.x - other.x, 
                    self.y - other.y))

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

# makes sence if hexes are used
class VancouverDistance(Vector):
    def abs(self, point):
        new_point = copy.copy(point)
        new_point.x = abs(point.x)
        new_point.y = abs(point.y)
        return new_point

    def is_odd(self, num):
        if num % 2 == 1:
            return True
        return False

    def compare_axis_y(self):
        if self.origin.y < self.destination.y:
            return -1
        elif self.origin.y == self.destination.y:
            return 0
        else:
            return 1

    def correction(self):
        y_comparison = self.compare_axis_y()
        if self.is_odd(self.x) or y_comparison == 0:
            correction = 0
        else:
            if y_comparison < 0:
                correction = self.origin.x % 2
            elif y_comparison > 0:
                correction = self.destination.x % 2
        return correction

    def calculate_vector(self):
        point_dist = self.destination - self.origin
        point_dist_abs = self.abs(point_dist)
        return point_dist_abs.x, point_dist_abs.y

    def get_vancouver_max(self):
        return max(0, self.y - math.floor(self.x/2))

    def calculate_norm(self):
        correction = self.correction()
        vancouver_max = self.get_vancouver_max()
        total = vancouver_max + self.x - correction
        return int(total)
        










