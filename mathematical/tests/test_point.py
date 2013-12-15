from unittest import TestCase
from mathematical.trigonometry import Point


class TestPoint(TestCase):
    def test_sum(self):
        result = Point(5, 7) + Point(4, 10)
        self.assertEqual('(9,17)', str(result))

    def test_sub(self):
        result = Point(5, 7) - Point(4, 10)
        self.assertEqual('(1,-3)', str(result))

    def test_equality(self):
        result = Point(5, 7)
        self.assertEqual(Point(5, 7), result)

    def test_distance(self):
        result = Point(5, 7).distance(Point(5, 8))
        self.assertEqual(1, result)
