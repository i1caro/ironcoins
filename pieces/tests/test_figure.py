from pieces.models import Figure
import pytest


@pytest.fixture
def common_figure():
    return Figure(name='Ogre', side='MySide',
                  stats={'life': 10, 'melle_power': 20, 'movement': 2})


def test_create_figure():
    figure = Figure(name='Ogre', side='MySide')
    assert figure.name == 'Ogre'
    assert figure.side == 'MySide'


def test_common_status(common_figure):
    assert common_figure.get('life') == 10
    assert common_figure.get('melle_power') == 20


def test_damage(common_figure):
    common_figure.damage(5)
    assert common_figure.get('life') == 5

    common_figure.damage(10)
    assert common_figure.get('life') == 0


def test_regenerate(common_figure):
    common_figure.damage(5)
    common_figure.regenerate()
    assert common_figure.get('life') == 10


def test_death(common_figure):
    assert common_figure.is_dead is False
    common_figure.damage(10)
    assert common_figure.is_dead is True


def test_set_value(common_figure):
    common_figure.set('movement', 10)
    assert common_figure.get('movement') == 10
    common_figure.regenerate()
    assert common_figure.get('movement') == 10


def test_move(common_figure):
    common_figure.set('movement', 10)
    common_figure.move(2)
    assert common_figure.get('movement') == 8
    common_figure.regenerate()
    assert common_figure.get('movement') == 10



