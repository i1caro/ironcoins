from tests.main import MainTestClass
from mapchart.models import MapFrontiers
from mathematical.trigonometry import Hex
import numpy as np


class TestMapFrontiers(MainTestClass):
    def setUp(self):
        super(TestMapFrontiers, self).setUp()
        self.map = MapFrontiers(
                    name='MyMap',
                    size_x=5,
                    size_y=10
                    )

    def prepare_map(self):
        x = self.map.size_x
        y = self.map.size_y
        terrain_map = np.abs(np.eye(x,y)-1)
        terrain_map[1][1]=1
        return terrain_map

    def test_creation(self):
        result = str(self.map)
        self.assertEqual('Map[MyMap](5,10)', result)

    def test_map_path(self):
        x = self.map.size_x
        y = self.map.size_y
        origin = Hex(1, y-1)
        destination = Hex(x-1, 1)
        my_maph.set_map(self.prepare_map())
        path = my_maph.shortest_path(origin, destination)
        print path
        self.assertEqual('Kk', path)
    
