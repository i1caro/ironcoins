from mathematical.trigonometry import VancouverDistance
from mapchart.structure import Fringe

class ShortestDistance(object):
    def __init__(self, base_map):
        self.is_inside_map = base_map.is_inside_map
        self.has_path = base_map.has_path

    def set_cost(self, func):
        self.cost = func

    def children(self, node):
        for child in node.children():
            if self.is_inside_map(child) and self.has_path(child):
                yield child

    def has_path(self, node):
        if self.cost(node):
            return False
        else:
            return True

    def get_cache_h(self, cache, node):
        return cache[node][0] + cache[node][2]

    def heuristic(self, origin, destination):
        vector = VancouverDistance(origin, 
                            destination)
        return vector.calculate_norm()

    def calc(self, origin, destination):
        flimit = self.heuristic(origin, destination)
        cache = {origin : (0, None, flimit)}
        fringe = Fringe()
        fringe.update(len(fringe),origin)

        found = False

        while(found == False and len(fringe)):
            len_fringe = len(fringe)

            for node_index in xrange(len(fringe)):
                node = fringe[node_index]
                g = cache.get(node, (0, None))[0]
                if node == destination:
                    found = True
                    break

                for child in self.children(node):
                    g_child = g + self.cost(child)
                    child_cache = cache.get(child, None) 
                    heuristic = None
                    if child_cache is not None:
                        g_cached = child_cache[0]
                        if g_child >= g_cached:
                            continue
                        heuristic = child_cache[2]
                    if not heuristic:
                        heuristic = self.heuristic(child, destination)
                    cache[child] = (g_child, node, heuristic)
                    fringe.update(node_index+1, child)
                fringe.pop(node_index)

            flimit = min([self.get_cache_h(cache, node) for node in fringe])

        path = False
        if found == True:
            path = self.reverse_path(cache, destination)
        return path

    def reverse_path(self, cache, destination):
        g, parent, nothing = cache[destination]
        if parent:
            return [destination] + self.reverse_path(cache, parent)
        else:
            return [destination]

class MapFrontiers(object):
    name = None
    size_x = None
    size_y = None

    def __init__(self, 
                name, 
                size_x,
                size_y):
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self._shortest_path_func = ShortestDistance(self)
        


    def shortest_path(self, origin, destination, cost_func=None):
        if not cost_func:
            cost_func = self.cost
        self._shortest_path_func.set_cost(cost_func)
        return self._shortest_path_func.calc

    def cost(self, node):
        return self.terrain_map[node.x][node.y]

    def set_map(self, terrain_map):
        self.terrain_map = terrain_map

    def is_inside_map(self, node):
        if node.x >= 0 and node.x < self.size_x and node.y >= 0 and node.y < self.size_y:
            return True
        return False
    
    def __str__(self):
        return 'Map[%s](%s,%s)' % (
                        self.name,
                        self.size_x, 
                        self.size_y)





