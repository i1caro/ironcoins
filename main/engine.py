import sys

CONTINUE = True
FINISH = False


class Action(object):
    def __init__(self, item, iniative):
        self.item = item
        self.initiative = initiative

    def prepare(self, attribute, args={}):
        self.attribute = attribute
        self.args = args

    def do(self):
        function = getattr(self.item, self.attribute)
        return function(**self.args)

    def __cmp__(self, other):
        if self.initiative > other.initiative:
            return -1
        if self.initiative == other.initiative:
            return 0
        else:
            return 1

class Move(Action):
    MAX_MOVEMENT = sys.maxint
    MOVE_FUNCTION = 'move'
    path_index = 0

    def __init__(self, initiative, item, path, chart):
        self.path = path
        self.chart = chart
        super(Move, self).__init__(initiative, item)

    def do(self):
        super(Move, self).do()
        if self.prepare_next_move():
            return [self]
        else:
            return None

    def prepare_next_move(self):
        self.initiative = self.calc_new_initiative()
        next_point = self.get_next_point()
        if next_point:
            cost = self.get_move_cost(next_point)
            if self.can_move(cost):
                args = self.create_args(next_point, cost)
                self.prepare(self.MOVE_FUNCTION, args)
            return self.CONTINUE
        else:
            return self.FINISH

    def create_args(self, point, movement_cost):
        result = {'movement_cost':movement_cost, 
                        'point':point}
        return result

    def get_next_point(self):
        if self.path_index > len(self.path)-1:
            result = self.path[self.path_index]
            self.path_index += 1
        else:
            result = None
        return result

    def can_move(self, cost):
        return cost <= self.item.get_movement()

    def calc_movement_cost(self, point):
        cost = self.chart[point.x][point.y]
        if cost:
            return cost
        else:
            return self.MAX_MOVEMENT

    def calc_new_initiative(self):
        return self.initiative -=1

    def calc_new_path(self):
        return self.path[1:]

    def prepare(self, iniative, path):
        self.attribute = attribute
        self.args = args


class Engine(object):
    def __init__(self, actions=list()):
        self.actions = actions
        self.actions.sort(reverse=True)

    def start(self):
        while(self.actions):
            act = self.actions.pop()
            new_actions = act.do()
            if new_actions:
                self.queu_insert(new_actions)

    def queu_insert(self, new_actions):
        self.actions.extend(new_actions)
        self.actions.sort(reverse=True)





















