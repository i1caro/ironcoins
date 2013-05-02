from tests.main import MainTestClass
from mapchart.models import MapMatrix
from mathematical.trigonometry import Hex


class TestMap(MainTestClass):
    origin = Hex(2,2)
    destination = Hex(5,9)
    piece = 'test_piece'

    def create_map(self):
        return MapMatrix('my_map', 20, 15)

    def test_creation(self):
        result = self.create_map()
        self.assertEqual('Map[my_map](20,15)', str(result))

    def test_inside_size(self):
        result = self.create_map().map
        self.assertEqual(20, len(result))
        self.assertEqual(15, len(result[0]))

    def test_cost(self):
        result = self.create_map().cost(self.origin)
        self.assertTrue(isinstance(int, result))

    def test_put_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.origin, self.piece)
        result = test_map.get_piece(self.origin)
        self.assertEqual(piece, result)

    def test_clear_piece(self):
        test_map = self.create_map()
        test_map.put_piece(self.origin, self.piece)
        test_map.clear_piece(self.origin)
        result = test_map.get_piece(self.origin)
        self.assertEqual(None, result)


    def test_shortest_path(self):
        test_map = self.create_map()        
        result = test_map.shortest_path(self.origin, self.destination)
        path = '(2,2)(2,3)(2,4)'
        self.assertEqual(path, str(result))