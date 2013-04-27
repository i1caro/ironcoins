from mapchart.utils import ShortestDistance
from mapchart.utils import is_node_within
from mapchart.constants import IMPASSABLE
from mapchart.constants import TERRAIN_COSTS
from mapchart.exceptions import OverWriteError
import functools


class Plot(object):
    def __init__(self, terrain_type=None):
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

    def get_piece(self):
        return self.piece

    def put_piece(self, piece):
        if self.is_full():
            raise OverWriteError(self)
        self.piece = piece

    def clear_piece(self):
        self.piece = None

    def __str__(self):
        return 'Piece %s %s' % (self.piece, self.type)


class MapMatrix(object):
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.map = self.create_map(width, height)
        self.is_inside_map = functools.partial(
                                func=is_node_within, 
                                width=width, 
                                height=height)
        self._shortest_path_function = ShortestDistance(self.is_inside_map, self.cost)


    def create_map(self, width, height):
        return [[ Plot(GRASS) for y in range(height)] 
                            for x in range(width)]

    def shortest_path(self, origin, destination):
        return self._shortest_path_function.cost(origin, destination)

    def cost(self, node):
        plot = self.get_plot(node)
        return plot.cost()

    def put_piece(self, piece, node):
        plot = self.get_plot(node)
        plot.put_piece(piece)

    def clear_piece(self, node):
        plot = self.get_plot(node)
        plot.clear_piece()

    def get_plot(self, node):
        return self.map[node.x][node.y]

    def __str__(self):
        return 'Map[%s](%s,%s)' % (
                        self.name,
                        self.width, 
                        self.height)





