from mathematical.trigonometry import VancouverDistance


def is_node_within(width, height, node):
    if node.x < width and node.y < height:
        return True
    return False

# Fringe structure for a faster shortest distance
class Fringe(object):
    inside = list()
    index = dict()
    size = 0
    
    def update(self, where, item):
        index_number = self.index.get(item, None)
        if index_number:
            self.inside.pop(index_number)
        else:
            self.size+=1
        self.inside.insert(where, item)
        self.index[item] = where

    def pop(self, where):
        node = self.inside.pop(where)
        self.index.pop(node)
        self.size-=1

    def __getitem__(self, where):
        return self.inside[where]

    def __len__(self):
        return self.size


class ShortestDistance(object):
    def __init__(self, inside_map_function, node_cost_function):
        self.is_inside_map = inside_map_function
        self.cost = node_cost_function

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
        return origin.distance(destination)

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
