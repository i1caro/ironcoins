from tests.main import MainTestClass
# from main.engine import Action

# class TestAction(MainTestClass):
#     # def setUp(self):
#     #     super(MainTestClass, self).setUp()

#     def test_action_initiative(self):
#         a = Action(4)
#         self.assertEqual(4, a.initiative)

#     def test_action_equality(self):
#         a = Action(4)
#         b = Action(4)
#         self.assertEqual(b, a)

#     def test_action_greater(self):
#         a = Action(4)
#         b = Action(5)
#         self.assertGreater(b, a)

from pieces.models import Figure
from mathematical.trigonometry import Hex


class TestMovementOnePiece(MainTestClass):
    def setUp(self):
        colision_map = 
        self.figure = Figure(name='FigureA',
                    position=Hex(0,0),
                    located_map=self.located_map,
                    movement=0)
        super(TestMovement, self).setUp()



        