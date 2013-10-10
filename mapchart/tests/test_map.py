from tests.main import MainTestClass
from mapchart.models import MapBuilder
from mathematical.trigonometry import Hex
from mapchart.constants import GRASS


def create_grass_map(width, height):
    return [[GRASS for y in range(height)]
        for x in range(width)]


class TestMap(MainTestClass):
    origin = Hex(2,2)
    destination = Hex(5,9)
    piece = 'test_piece'

    def setUp(self):
        grass_map = create_grass_map(20, 15)
        self.map = MapBuilder('my_map', grass_map)
        super(TestMap, self).setUp()

    def test_creation(self):
        self.assertEqual('Map[my_map](20,15)', str(self.map))

    # def test_cost(self):
    #     result = self.create_map().cost(self.origin)
    #     self.assertTrue(isinstance(result, int))

    def test_put_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.piece, self.origin)
        result = test_map.get_piece(self.origin)
        self.assertEqual(self.piece, result)

    def test_clear_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.piece, self.origin)
        test_map.clear_piece(self.origin)
        result = test_map.get_piece(self.origin)
        self.assertEqual(None, result)








