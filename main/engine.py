from mapchart.exceptions import OverWriteError
from mapchart.exceptions import NoMoreActionsError
from collections import deque

import functools


def delay_initiative(initiative):
    return initiative + 1

def rush_initiative(initiative):
    return initiative - 1


class Engine(object):
    TIME = 12

    def __init__(self, actions):
        actions.sort()
        self.timetable = [list() for t in self.TIME]
        self.put_actions_into_timetable(actions)

    def put_actions_into_timetable(self, actions):
        for action in actions:
            self.timetable[action.initiative].append(action)

    def start(self):
        for action in self.timetable:
            unplayed = self.play_actions(actions)
            try:
                self.put_actions_into_timetable(unplayed)
            except IndexError:
                pass            

    def play_actions(self, actions):
        unplayed = list()
        for action in actions:
            try:
                action.do()
            except NoMoreActionsError:
                pass
            except OverWriteError:
                delayed = self.delay_action(action)
                uplayed.extend(delayed)
        return unplayed

    def delay_action(self, action):
        next_initiative = action.get_next_initiative()
        if next_initiative:
            action.initiative = next_initiative
            return [action]
        return []


@functools.total_ordering
class Action(object):
    def __init__(self, initiative):
        self.initiative = initiative

    def __eq__(self, other):
        return (self.initiative == other.initiative)

    def __lt__(self, other):
        return (self.initiative < other.initiative)

    def get_next_initiative(self):
        return None


class Movement(Action):
    def __init__(self, initiative, piece, destination):
        self.piece = piece
        self.destination = destination
        self.path = self.create_path(piece, destination)
        self.in_bettween_move = None
        super(Movement, self).__init__(initiative)

    def create_path(self, piece, destination):
        from mathematical.trigonometry import Hex
        import random
        sample_list = [Hex(1,2), Hex(4,2), Hex(2,2), Hex(5,3), Hex(6,2),
                        Hex(5,4), Hex(4,5), Hex(2,6), Hex(1,3), Hex(4,4)]
        rrange = random.randrange(1,6)
        return random.sample(sample_list, rrange)
    #     map_matrix = self.piece.map
    #     return map_matrix.shortest_path(piece.position, destination)

        
    def do(self):
        if not self.in_bettween_move:
            try:
                self.in_bettween_move = self.path.pop(0)
            except IndexError:
                raise NoMoreActionsError
        self.piece.move(move)
        self.in_bettween_move = None

    def get_next_initiative(self):
        if self.path:
            self.initiative = delay_initiative(self.initiative)
            return self.initiative
        return None








