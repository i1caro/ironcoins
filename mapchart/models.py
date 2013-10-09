from mapchart.utils import is_node_within
from mapchart.constants import IMPASSABLE
from mapchart.constants import TERRAIN_COSTS
from mapchart.exceptions import PlotIsFullError
import functools


class Plot(object):
    def __init__(self, terrain_type):
        self.piece = None
        self.type = terrain_type

    def cost(self):
        if self.is_full():
            return TERRAIN_COSTS[IMPASSABLE]
        else:
            return TERRAIN_COSTS[self.type]

    def is_full(self):
        if not self.piece:
            return False
        return True

    def put_piece(self, piece):
        if self.is_full():
            raise PlotIsFullError(self)
        self.piece = piece

    def clear(self):
        self.piece = None

    def __str__(self):
        return 'Piece %s->%s' % (self.type, self.piece)

    def __repr__(self):
        return str(self)


class MapMatrix(object):
    def __init__(self, name, map_matrix):
        self.name = name
        self.map = self.build_map(map_matrix)
        self.width = len(self.map)
        self.height = len(self.map[0])
        self.is_inside_map = functools.partial(is_node_within,
                                *(self.width, self.height))

    def build_map(self, map_matrix):
        return [[Plot(map_matrix[x][y]) for y in range(map_matrix[0])]
            for x in range(map_matrix)]

    def cost(self, where):
        plot = self._get_plot(where)
        return plot.cost()

    def put_piece(self, which, where):
        plot = self._get_plot(where)
        plot.put_piece(which)

    def clear_piece(self, where):
        plot = self._get_plot(where)
        plot.clear()

    def get_piece(self, where):
        plot = self._get_plot(where)
        return plot.piece

    def _get_plot(self, node):
        return self.map[node.x][node.y]

    def __str__(self):
        return 'Map[%s](%s,%s)' % (self.name, self.width, self.height)

    def __repr__(self):
        return str(self)





