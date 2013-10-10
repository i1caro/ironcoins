from mapchart.exceptions import PieceDoesNotExist
from mapchart.exceptions import PlotIsFullError
from mapchart.constants import GRASS
from mapchart.models import MapBuilder as Map
from pieces.models import Figure
import pytest


def create_figure(name):
    return Figure(name=name,
                  side=name,
                  movement=100)


@pytest.fixture
def figure_a():
    return create_figure('FigurA')


@pytest.fixture
def figure_b():
    return create_figure('FigurB')


@pytest.fixture
def clean_map():
    created_map = [[GRASS for y in range(10)]
        for x in range(10)]
    return Map(name='clean_map',
               map_matrix=created_map)


class TestMovementEngine():
    def setup_method(self, method):
        self.map = clean_map()

    def test_a_exists(self, figure_a):
        self.map.put_piece(figure_a, (5, 5))
        piece = self.map.get_piece(5, 5)
        assert piece is figure_a

    def test_a_is_in_right_place(self, figure_a):
        self.map.put_piece(figure_a, (5, 5))
        assert self.map.get_piece_location(figure_a) == (5, 5)

    def test_b_does_not_exist(self, figure_b):
        with pytest.raises(PieceDoesNotExist):
            self.map.get_piece_location(figure_b)

    def test_plot_is_full(self, figure_a, figure_b):
        self.map.put_piece(figure_a, (5, 5))
        with pytest.raises(PlotIsFullError):
            self.map.put_piece(figure_b, (5, 5))

    def test_piece_a_moves_to_same_location(self, figure_a):
        self.map.put_piece(figure_a, (5, 5))
        self.map.move(figure_a, (5, 5))

    def test_a_goes_to_location_b(self, figure_a):
        self.map.put_piece(figure_a, (5, 5))
        self.map.move(figure_a, (8, 8))
        not_a = self.map.get_piece(5, 5)
        is_a = self.map.get_piece(8, 8)
        assert not_a is None
        assert is_a is figure_a
