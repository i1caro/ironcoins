import math


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

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def distance(self, other):
        dist = (other.x - self.x)**2
        dist+= (other.y - self.y)**2
        return dist

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash('%s %s' % (self.x, self.y))


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

    def vancouver_distance(self, other):
        distance = VancouverDistance(origin, destination)
        return distance.calc()


class VancouverDistance(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.vector_x, self.vector_y = self.distance()

    def distance(self):
        point_dist = self.destination - self.origin
        return self.abs(point_dist)

    @staticmethod
    def abs(point):
        return abs(point.x), abs(point.y)

    def calc(self):
        correction = self.correction()
        vancouver_max = self.get_vancouver_max()
        total = vancouver_max + self.vector_x - correction
        return int(total)

    def get_vancouver_max(self):
        return max(0, self.vector_y - math.floor(self.vector_x/2))

    def correction(self):
        y_comparison = self.compare_axis_y()
        if self.is_odd(self.vector_x) or y_comparison == 0:
            correction = 0
        else:
            if y_comparison < 0:
                correction = self.origin.x % 2
            elif y_comparison > 0:
                correction = self.destination.x % 2
        return correction

    def compare_axis_y(self):
        if self.origin.y < self.destination.y:
            return -1
        elif self.origin.y == self.destination.y:
            return 0
        else:
            return 1

    @staticmethod
    def is_odd(num):
        if num % 2 == 1:
            return True
        return False

    def __str__(self):
        return '(%s,%s)' % (self.vector_x, self.vector_y)

    def __repr__(self):
        return '%s%s' % (self.__class__,self.__str__())

