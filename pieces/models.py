from mathematical.trigonometry import Hex
import functools
import sys

# def Position(Hex):
#     def __init__(self, x, y, where):
#         self.where = where
#         super(Position, self).__init__(x, y)

#     def move(self, destination):
#         self.where.move(self, destination)


@functools.total_ordering
class FigureStat(object):
    def __init__(self, stat, turn_stat=None):
        self.stat = stat
        self.turn_stat = turn_stat

    def __eq__(self, other):
        return (self.value == other.value)

    def __lt__(self, other):
        return (self.value < other.value)

    def __repr__(self):
        return '%s' % self.value

    def add(self, value):
        self.stat = self.add_function(self.stat, value)

    def turn_add(self, value):
        self.turn_stat = self.add_function(self.turn_stat, value)

    def regenerate(self):
        self.turn_set(None)

    def set(self, value):
        self.stat = value

    def turn_set(self, value):
        self.turn_stat = value        

    def _value(self):
        return self.add_function(self.stat, self.turn_stat)
    value = property(_value)

    @staticmethod
    def add_function(first, second):
        if all((first, second)):
            result = first + second
        else:
            result = (first or second)
        return result


class FigureStats(objects):
    def __init__(self, **kargs):
        for name, value in kargs.items():
            self.create_stat(name, value)
            
    def create_stat(self, name, value):
        setattr(self, name, FigureStat(stat=value))

    def regenerate(self):
        for stat in self.__dict__.values():
            stat.regenerate()


class Figure(object):
    MAX_MOVEMENT = sys.maxint

    def __init__(self, name, position, map, movement, **kargs):
        self.name = name
        self.position = position
        if not kargs:
            kargs = dict()
        kargs[movement] = movement
        self.stats = FigureStats(**kargs)

    def __str__(self):
        return '%s(%s)' % (self.name, self.stats.position)

    def __repr__(self):
        return self.__str__()

    def end_turn(self):
        self.stats.regenerate()

    def die(self):
        pass

    def move(self, movement_cost, destination):
        if self.stats.movement < movement_cost:
            raise ValueError('Movement cost %s exceeds available movement %s.' % (self.stats.movement, movement_cost))
        self.map.move(self.position, destination)
        self.position = destination
        self.stats.movement.turn_add(-movement_cost)

    def get_movement_cost(self, point):
        point_type = self.chart.get_point_type(point)
        cost = self.get_terrain_movement_cost_for_type(point_type)
        if cost:
            return cost
        else:
            return self.MAX_MOVEMENT

    def get_terrain_movement_cost_for_type(self, point_type):
        return 1











