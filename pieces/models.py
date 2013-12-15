from mathematical.trigonometry import Hex
from mapchart.constants import TERRAIN_COSTS
import functools
import sys


@functools.total_ordering
class Stat(object):
    def __init__(self, stat, turn_stat=None):
        self.born_stat = stat
        self.turn_stat = turn_stat

    def __eq__(self, other):
        return (self.value == other.value)

    def __lt__(self, other):
        return (self.value < other.value)

    def __repr__(self):
        return '%s' % self.value

    def add(self, value):
        self.born_stat = self.add_function(self.born_stat, value)

    def turn_add(self, value):
        self.turn_stat = self.add_function(self.turn_stat, value)

    def regenerate(self):
        self.turn_stat = None

    def _value(self):
        return self.add_function(self.born_stat, self.turn_stat)
    value = property(_value)

    @staticmethod
    def add_function(first, second):
        if all((first, second)):
            result = first + second
        else:
            result = (first or second)
        return result


class FigureStats(object):
    def __init__(self, **kargs):
        for name, value in kargs.items():
            self.create_stat(name, value)

    def create_stat(self, name, value):
        setattr(self, name, value)

    def regenerate(self):
        for stat in self.__dict__.values():
            try:
                stat.regenerate()
            except AttributeError:
                pass


class Figure(object):
    MAX_MOVEMENT = sys.maxint
    square_type = Hex

    def __init__(self, name, side, movement, **kargs):
        self.movement_cost = TERRAIN_COSTS
        self.name = name
        self.side = side
        if not kargs:
            kargs = dict()
        kargs['movement'] = movement
        self.stats = FigureStats(**kargs)

    def __str__(self):
        return '%s(%s)' % (self.name, self.side)

    def __repr__(self):
        return self.__str__()

    def end_turn(self):
        self.stats.regenerate()

    def die(self):
        pass

    def move(self, movement_cost, destination):
        if self.stats.movement < movement_cost:
            raise ValueError(
                ('Movement cost {} exceeds available movement {}'
                 '').format(self.stats.movement, movement_cost))
        self.position = self.square_type(destination)
        self.stats.movement.turn_add(-movement_cost)

    def get_movement_cost(self, terrain_type):
        return self.movement_cost.get(terrain_type,
                                      self.MAX_MOVEMENT)


