from mathematical.trigonometry import VancouverDistance
from main.models import ReadableObject
import sys
import pdb


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

    def set_map(self, terrain_map):
        self.terrain_map = terrain_map

    def __str__(self):
        return 'Map[%s](%s,%s)' % (
                        self.name,
                        self.size_x, 
                        self.size_y)

    def cost(self, location):
        cost = self.terrain_map[location.x][location.y]
        return cost + 3

    def children(self, node):
        for child in node.children():
            if self.is_inside_map(child) and self.has_path(child):
                yield child

    def has_path(self, node):
        if self.terrain_map[node.x][node.y] is 0:
            return False
        else:
            return True

    def is_inside_map(self, node):
        if node.x >= 0 and node.x < self.size_x and node.y >= 0 and node.y < self.size_y:
            return True
        return False

    def heuristic(self, origin, destination):
        vector = VancouverDistance(origin, 
                        destination)
        return vector.calculate_norm()


    def shortest_path(self, origin, destination):
        fringe = [origin,]
        cache = {str(origin) : (0, None)}

        flimit = self.heuristic(origin, destination)
        found = False

        while(found == False and len(fringe)):
            fmin = sys.maxint
            for node in fringe: 
                g = cache.get(str(node), (0, None))[0]
                fcost = g + self.heuristic(node, destination)
                if fcost > flimit:
                    fmin = min(fcost, fmin)
                    continue
                if node == destination:
                    found = True
                    break
                    # reversed(node)
                index_node = fringe.index(node)
                for child in self.children(node):
                    g_child = g + self.cost(child)
                    child_cache = cache.get(str(child), None) 
                    if child_cache != None:
                        g_cached = child_cache[0]
                        if g_child >= g_cached:
                            continue
                    if child in fringe:
                        fringe.remove(child)
                    fringe.insert(index_node+1, child)
                    cache[str(child)] = (g_child, node)
                fringe.remove(node)
            flimit = fmin

        path = False
        if found == True:
            path = self.reverse_path(cache, destination)
        return path

    def reverse_path(self, cache, destination):
        g, parent = cache[str(destination)]
        if parent:
            return [destination] + self.reverse_path(cache, parent)
        else:
            return [destination]




