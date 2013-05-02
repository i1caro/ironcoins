from tests.main import MainTestClass
from mapchart.models import Plot
from mapchart.constants import TERRAIN_COSTS
from mapchart.constants import GRASS

class TestPlot(MainTestClass):
    grass_type = GRASS
    grass_cost = TERRAIN_COSTS[GRASS]
    piece = 'test_piece'

    def create_plot(self):
        return Plot(self.grass_type)

    def test_creation(self):
        result = self.create_plot()
        self.assertEqual('Piece %s->None' % self.grass_type, str(result))

    def test_cost(self):
        result = self.create_plot().cost()
        self.assertEqual(self.grass_cost, result)

    def test_put_piece(self):
        plot = self.create_plot()
        plot.put_piece(self.piece)
        result = plot.piece
        self.assertEqual(self.piece, result)

    def test_is_full(self):
        plot = self.create_plot()
        plot.put_piece(self.piece)
        result = plot.is_full()
        self.assertTrue(result)

    def test_clear_piece(self):
        plot = self.create_plot()
        plot.put_piece(self.piece)
        plot.clear()
        result = plot.piece
        self.assertEqual(None, result)



