from mathematical.trigonometry import VancouverDistance
from collections import deque


def is_node_within(width, height, node):
    if 0 <= node.x < width and 0 <= node.y < height:
        return True
    return False

# # Fringe structure for a faster shortest distance
class Fringe(deque):
    def burn_nodes(self):
        while(True):
            try:
                node = self.popleft()
            except IndexError:
                break
            else:
                yield node


class ShortestDistance(object):
    def __init__(self, inside_map_function, node_cost_function):
        self.is_inside_map = inside_map_function
        self.cost = node_cost_function

    def children(self, node):
        for child in node.children():
            if self.is_inside_map(child) and self.has_path(child):
                yield child

    def has_path(self, node):
        return self.cost(node)

    def get_cache_h(self, cache, node):
        return cache[node][0] + cache[node][2]

    def heuristic(self, origin, destination):
        return origin.distance(destination)

    def calc(self, origin, destination):
        flimit = self.heuristic(origin, destination)
        cache = {origin : (0, None, flimit)}
        fringe = Fringe()
        fringe.append(origin)

        found_destination = False

        while(found_destination == False and fringe):

            for node in fringe.burn_nodes():
                g = cache.get(node, (0, None))[0]

                if node == destination:
                    found_destination = True
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
                    
                    cache_heuristic = heuristic or self.heuristic(
                                                    child, destination)

                    cache[child] = (g_child, node, cache_heuristic)
                    fringe.append(child)
            flimit = min([self.get_cache_h(cache, node) for node in fringe])

        result = False
        if found_destination == True:
            result = self.reverse_path(cache, destination)
        return result

    def reverse_path(self, cache, destination):
        g, parent, nothing = cache[destination]
        if parent:
            return [destination] + self.reverse_path(cache, parent)
        else:
            return [destination]
