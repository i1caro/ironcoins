from mathematical.trigonometry import Hex
from mapchart.constants import TERRAIN_COSTS
import functools
import sys


@functools.total_ordering
class Stat(object):
    def __init__(self, stat):
        self.born_stat = stat
        self.turn_stat = 0

    def __eq__(self, other):
        return (self.value == other.value)

    def __lt__(self, other):
        return (self.value < other.value)

    def __repr__(self):
        return str(self.value)

    def set(self, value):
        self.born_stat = value

    def turn_add(self, value):
        self.turn_stat = self.turn_stat + value
        if -self.turn_stat > self.born_stat:
            self.turn_stat = -self.born_stat

    def regenerate(self):
        self.turn_stat = 0

    @property
    def value(self):
        return self.add_function(self.born_stat, self.turn_stat)

    @staticmethod
    def add_function(first, second):
        return first + second


class FigureStats(object):
    def __init__(self, **kargs):
        for name, value in kargs.items():
            setattr(self, name, value)

    def regenerate(self):
        for stat in self.__dict__.values():
            try:
                stat.regenerate()
            except AttributeError:
                pass

    def items(self):
        return self.__dict__.items()


class Figure(object):
    MAX_MOVEMENT = sys.maxint
    square_type = Hex
    default_stats = {
        'life': 0,
        'ranged_power': 0,
        'melle_power': 0,
        'infernal_power': 0,
        'movement': 0
    }

    def __init__(self, name, side, stats=None):
        self.movement_cost = TERRAIN_COSTS
        self.name = name
        self.side = side
        self.is_dead = False
        self.stats = FigureStats(**self._clean_stats(stats))

    def _clean_stats(self, stats):
        result = dict()
        if not stats:
            stats = dict()

        for key, default in self.default_stats.items():
            value = stats.get(key, default)
            result[key] = Stat(value)
        return result

    def __str__(self):
        return '%s(%s)' % (self.name, self.side)

    def __repr__(self):
        return self.__str__()

    def set(self, name, value):
        getattr(self.stats, name).set(value)

    def end_turn(self):
        self.stats.regenerate()

    def die(self):
        self.is_dead = True

    def move(self, movement_cost):
        if self.stats.movement.value < movement_cost:
            raise ValueError(
                ('Movement cost {} exceeds available movement {}'
                 '').format(self.stats.movement, movement_cost))
        self.stats.movement.turn_add(-movement_cost)

    def get_movement_cost(self, terrain_type):
        return self.movement_cost.get(terrain_type,
                                      self.MAX_MOVEMENT)

    def get(self, name):
        return getattr(self.stats, name).value

    def damage(self, value):
        self.stats.life.turn_add(-value)
        if self.stats.life.value <= 0:
            self.die()

    def regenerate(self):
        for key, stat in self.stats.items():
            stat.regenerate()



