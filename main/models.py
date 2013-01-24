# from main.engine import Action
# import sys

# class Movement(object):
#     MAX_MOVEMENT = sys.maxint

#     def __init__(self, initiative, item, path, chart):
#         self.initiative = initiative
#         self.path = path
#         self.item = item
#         self.chart = chart
#         self.actions = list()

#     def calc_action(self):
#         movement = item.get_movement()
#         initiative = self.initiative
#         for point in self.path:
#             cost = self.calc_movement_cost(point, self.chart)

#             if self.can_move(cost, movement_cost):
#                 args = self.create_args(cost, point)
#                 action = self.create_action(initiative, args)
#                 self.add_action_into_list(action)
#                 movement = self.get_new_movement(movement, cost)
#                 initiative = self.update_initative(initiative)

#         return self.actions

#     def can_move(self, cost, movement):
#         return cost <= movement

#     def update_initative(self, initiative, cost):
#         return initiative -=cost

#     def create_args(self, movement_cost, point):
#         result = {'movement_cost':movement_cost, 
#                         'point':point}
#         return result

#     def add_action_into_list(self, action):
#         self.actions.append(action)

#     def create_action(self, initiative, args):
#         function = 'move'
#         action = Action(initiative, self.item)
#         action.prepare(function, args)
#         return action

#     def get_new_movement(self, old_movement, movement_cost):
#         new_movement = old_movement - movement_cost
#         return new_movement

#     def calc_movement_cost(self, point, chart):
#         cost = chart[point.x][point.y]
#         if cost:
#             return cost
#         else:
#             return self.MAX_MOVEMENT


# class RunSpecial(object):
#     def run(self, queu):
        for element in queu:
            element.action()


