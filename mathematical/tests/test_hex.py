from unittest import TestCase
from mathematical.trigonometry import Hex


class TestHex(TestCase):
    hex_tile = Hex(2, 2)

    def test_side_north_west(self):
        result = self.hex_tile.side_north_west
        self.assertEqual('(1,2)', str(result))

    def test_side_north(self):
        result = self.hex_tile.side_north
        self.assertEqual('(2,3)', str(result))

    def test_side_north_east(self):
        result = self.hex_tile.side_north_east
        self.assertEqual('(3,2)', str(result))

    def test_side_south_east(self):
        result = self.hex_tile.side_south_east
        self.assertEqual('(3,1)', str(result))

    def test_side_south(self):
        result = self.hex_tile.side_south
        self.assertEqual('(2,1)', str(result))

    def test_side_south_west(self):
        result = self.hex_tile.side_south_west
        self.assertEqual('(1,1)', str(result))

    def test_all_sides(self):
        result = sum([1 for i in self.hex_tile.children()])
        self.assertEqual(6, result)

    def test_distance(self):
        hex_a = self.hex_tile.side_south
        hex_b = self.hex_tile.side_north_east
        result = hex_a.distance(hex_b)
        self.assertEqual(2, result)
