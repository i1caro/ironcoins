from tests.main import MainTestClass
from mapchart.models import MapChart
from mathematical.trigonometry import Hex

class TestMapChart(MainTestClass):
    def test_creation(self):
        result = MapChart(
                    name='MyMap',
                    point_class=Hex,
                    size_x=20,
                    size_y=25,
                    )
        self.assertEqual('Map[MyMap](20,25)', str(result))
    
