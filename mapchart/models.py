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

    def __str__(self):
        return 'Map[%s](%s,%s)' % (
                        self.name,
                        self.size_x, 
                        self.size_y)

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
                (g, parent) = cache.get(str(node), (0, None))
                fcost = g + self.heuristic(node, destination)
                if fcost > flimit:
                    fmin = min(fcost, fmin)
                    continue
                if node == destination:
                    found = True
                    break
                    # reversed(node)
                for child in node:
                    g_child = g + 1#distance between(node and child)
                    child_cache = cache.get(str(child), None) 
                    if child_cache != None:
                        (g_cached, parent) = child_cache
                        if g_child >= g_cached:
                            continue
                    if child in fringe:
                        fringe.remove(child)
                    index_node = fringe.index(node)
                    fringe.insert(index_node+1, child)
                    cache[str(child)] = (g_child, node)
                fringe.remove(node)
            flimit = fmin

        if found == True:
            self.reverse_path(cache, destination)

    def reverse_path(self, cache, destination):
        g, parent = cache[str(destination)]
        if parent:
            self.reverse_path(cache, parent)
        print '%s' % destination

def test_map():
    from mathematical.trigonometry import Hex
    return MapChart('my_map',None,10,10).shortest_path(Hex(1,2), Hex(10,20))


