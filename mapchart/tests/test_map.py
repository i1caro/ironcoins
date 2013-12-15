from unittest import TestCase
from mapchart.models import HexMap as Map
from pieces.models import Figure
from mapchart.constants import GRASS


def create_grass_map(width, height):
    return [[GRASS for y in range(height)]
            for x in range(width)]


class TestMap(TestCase):
    origin = (2, 2)
    piece = Figure(movement=100, name='test_figure',
                   side='')

    def create_map(self):
        grass_map = create_grass_map(20, 15)
        return Map('my_map', grass_map)

    def test_creation(self):
        self.assertEqual('Map[my_map](20,15)', str(self.create_map()))

    def test_put_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.piece, self.origin)
        result = test_map.get_piece(*self.origin)
        self.assertEqual(self.piece, result)

    def test_clear_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.piece, self.origin)
        test_map.clear_piece(self.origin)
        result = test_map.get_piece(*self.origin)
        self.assertEqual(None, result)








