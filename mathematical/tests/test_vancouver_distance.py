from unittest import TestCase
from mathematical.trigonometry import Hex
from mathematical.trigonometry import VancouverDistance


class TestVancouverDistance(TestCase):
    origin = Hex(4, 7)
    destination = Hex(5, 3)

    def get_object(self):
        return VancouverDistance(self.origin,
                                 self.destination)

    def test_creation(self):
        result = self.get_object()
        self.assertEqual('(1,4)', str(result))

    def test_distance(self):
        result = self.get_object().distance()
        self.assertEqual('(1, 4)', str(result))

    def test_abs(self):
        result_x, result_y = self.get_object().abs(Hex(-2, 6))
        self.assertEqual('2', str(result_x))
        self.assertEqual('6', str(result_y))

    def test_is_odd(self):
        result = self.get_object().is_odd(1)
        self.assertEqual(True, result)

    def test_compare_axis_y(self):
        result = self.get_object().compare_axis_y()
        self.assertEqual(1, result)

    def test_correction(self):
        result = self.get_object().correction()
        self.assertEqual(0, result)

    def test_get_vancouver_max(self):
        result = self.get_object().get_vancouver_max()
        self.assertEqual(4, result)

    def test_norm(self):
        result = self.get_object().calc()
        self.assertEqual(5, result)










