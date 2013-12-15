# from mathematical.trigonometry import Hex
# from pieces.models import Figure
# from unittest import TestCase
# import unittest


# class FigureInit(object):
#     source = Hex(1, 2)
#     destination = Hex(10, 5)
#     located_map = None

#     def create_figure(self):
#         return Figure(name='Ogre',
#                       position=self.source,
#                       located_map=self.located_map,
#                       movement=0)


# class TestFigure(TestCase, FigureInit):
#     def test_creation(self):
#         result = self.create_figure()
#         equals = 'Ogre(%s)' % self.source
#         self.assertEqual(equals, str(result))

#     @unittest.skip('To implement path_to')
#     def test_path(self):
#         result = self.create_figure().path_to(self.destination)
#         path = '((1,2),(2,3),(3,4),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5))'
#         self.assertEqual(path, result)


# class TestFigureCircularMovement(TestCase, FigureInit):
#     source = Hex(2, 2)
#     left = Hex(1, 2)
#     top_left = Hex(1, 3)
#     top = Hex(2, 3)
#     top_right = Hex(3, 3)
#     right = Hex(3, 2)
#     down_right = Hex(3, 1)
#     down = Hex(2, 1)
#     down_left = Hex(1, 1)

#     @unittest.skip('To implement path_to')
#     def test_movement_left(self):
#         result = self.create_figure().path_to(self.left)
#         self.assertEqual('((2,2),(1,2))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_top_left(self):
#         result = self.create_figure().path_to(self.top_left)
#         self.assertEqual('((2,2),(1,2),(1,3))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_top(self):
#         result = self.create_figure().path_to(self.top)
#         self.assertEqual('((2,2),(2,3))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_top_right(self):
#         result = self.create_figure().path_to(self.top_right)
#         self.assertEqual('((2,2),(2,3),(3,3))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_right(self):
#         result = self.create_figure().path_to(self.right)
#         self.assertEqual('((2,2),(3,2))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_down_right(self):
#         result = self.create_figure().path_to(self.down_right)
#         self.assertEqual('((2,2),(3,1))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_down(self):
#         result = self.create_figure().path_to(self.down)
#         self.assertEqual('((2,2),(2,1))', str(result))

#     @unittest.skip('To implement path_to')
#     def test_movement_down_left(self):
#         result = self.create_figure().path_to(self.down_left)
#         self.assertEqual('((2,2),(1,1))', str(result))

