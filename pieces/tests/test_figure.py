from mathematical.trigonometry import Point
from pieces.models import Figure
from tests.main import MainTestClass
import unittest

class TestFigure(MainTestClass):
    source = Point(1,2)
    destination = Point(10,5)

    def get_figure(self):
        return Figure(name='Ogre', position=self.source)

    def test_creation(self):
        result = self.get_figure()
        equals = 'Ogre(%s)' % self.source
        self.assertEqual(equals, str(result))

    @unittest.skip('To implement')
    def test_movement_down(self):
        result = self.get_figure().path_to(self.down)
        self.assertEqual('((0,0),(-1,0))', str(result))

    @unittest.skip('To implement')
    def test_path(self):
        result = self.get_figure().path_to(destination)
        path = '((1,2),(2,3),(3,4),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5))'
        self.assertEqual(path, result)

class TestFigureCircularMovement(TestFigure):
    source = Point(2,2)
    left = Point(1,2)
    top_left = Point(1,3)
    top = Point(2,3)
    top_right = Point(3,3)
    right = Point(3,2)
    down_right = Point(3,1)
    down = Point(2,1)
    down_left = Point(1,1)

    @unittest.skip('To implement')
    def test_movement_left(self):
        result = self.get_figure().path_to(self.left)
        self.assertEqual('((2,2),(1,2))', str(result))

    @unittest.skip('To implement')
    def test_movement_top_left(self):
        result = self.get_figure().path_to(self.top_left)
        self.assertEqual('((2,2),(1,2),(1,3))', str(result))

    @unittest.skip('To implement')
    def test_movement_top(self):
        result = self.get_figure().path_to(self.top)
        self.assertEqual('((2,2),(2,3))', str(result))

    @unittest.skip('To implement')
    def test_movement_top_right(self):
        result = self.get_figure().path_to(self.top_right)
        self.assertEqual('((2,2),(2,3),(3,3))', str(result))

    @unittest.skip('To implement')
    def test_movement_right(self):
        result = self.get_figure().path_to(self.right)
        self.assertEqual('((2,2),(3,2))', str(result))

    @unittest.skip('To implement')
    def test_movement_down_right(self):
        result = self.get_figure().path_to(self.down_right)
        self.assertEqual('((2,2),(3,1))', str(result))

    @unittest.skip('To implement')
    def test_movement_down(self):
        result = self.get_figure().path_to(self.down)
        self.assertEqual('((2,2),(2,1))', str(result))

    @unittest.skip('To implement')
    def test_movement_down_left(self):
        result = self.get_figure().path_to(self.down_left)
        self.assertEqual('((2,2),(1,1))', str(result))

