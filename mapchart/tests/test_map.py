from tests.main import MainTestClass
from mapchart.models import MapMatrix
from mathematical.trigonometry import Hex
import numpy as np


class TestMap(MainTestClass):
    def setUp(self):
        super(TestMap, self).setUp()
        self.map = MapMatrix(
                    name='MyMap',
                    width=5,
                    height=10
                    )

    def test_creation(self):
        result = str(self.map)
        self.assertEqual('Map[MyMap](5,10)', result)

    def test_map_path(self):
        x = self.map.width
        y = self.map.height
        origin = Hex(1, y-1)
        destination = Hex(x-1, 1)
        my_maph.set_map(self.prepare_map())
        path = my_maph.shortest_path(origin, destination)
        print path
        self.assertEqual('Kk', path)
    
