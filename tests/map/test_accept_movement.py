from mapchart.constants import IMPASSABLE as I
from mapchart.constants import GRASS as o
from mapchart.models import HexMap as Map
from mapchart.engine import MovementEngine
from pieces.models import Figure

import pytest


@pytest.fixture
def dirty_map():
    dirty_map = [
    #    0  1  2  3  4  5  6  7
        [o, o, o, o, o, o, o, o],  # 0
        [o, o, o, I, o, I, I, I],  # 1
        [o, o, o, o, o, o, o, o],  # 2
        [o, o, o, o, I, I, I, I],  # 3
        [o, o, o, o, o, o, o, o],  # 4
        [o, o, I, o, o, o, o, o],  # 5
        [o, o, o, o, I, o, o, o],  # 6
        [o, o, o, o, o, o, I, o],  # 7
        [o, o, o, o, o, o, o, o],  # 8
        [o, o, o, o, o, o, o, o],  # 9
    ]
    return Map('dirty_map', dirty_map)


@pytest.fixture
def clean_map():
    clean_map = [[o for y in range(10)]
        for x in range(10)]
    return Map('clean_map', clean_map)


X = 1
Y = 1
@pytest.mark.parametrize(('origin', 'destination', 'reachable'), [
    ((X, Y), (X+0, Y+0), True),    # Same Place
    ((X, Y), (X+0, Y+1), True),    # North
    ((X, Y), (X+1, Y+1), True),    # North East
    ((X, Y), (X+1, Y+0), True),    # East
    ((X, Y), (X+1, Y-1), False),   # South East
    ((X, Y), (X+0, Y-1), True),    # South
    ((X, Y), (X-1, Y-1), False),   # South West
    ((X, Y), (X-1, Y+0), True),    # West
    ((X, Y), (X-1, Y+1), True),    # North West
])
def test_reach_in_hex(origin, destination, reachable):
    assert Map.are_close(origin, destination) == reachable


def create_figure(item):
    return Figure(movement=100,
                  name=item['name'],
                  side=item['side'])


def parse_input(input):
    map_figures = list()
    map_movements = list()
    for item in input:
        figure = create_figure(item)
        map_figures.append({
            'which': figure,
            'where': item['movement'][0]
        })
        map_movements.append({
            'figure': figure,
            'movement': item['movement'][1:]
        })
    return map_figures, map_movements


def assert_fixtures(this_map, input, expected):
    figures, moves = parse_input(input)
    for figure in figures:
        this_map.put_piece(**figure)

    engine = MovementEngine(this_map)
    results = engine.resolve(moves)
    for result, expect in zip(results, expected):
        assert result == expect

## TODO:
## test no piece

@pytest.mark.parametrize(('input', 'expected'), [
    # No movement
    (
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((0, 0),)}],
        [(0, 0)]
    ),
    # ONe movement
    (
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((0, 0), (1, 0))}],
        [(1, 0)]
    ),
    # Normal movement
    (
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((1, 2), (2, 3), (3, 3), (4, 4))}],
        [(4, 4)]
    ),
    # # Location Full for movement
    (
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((3, 2), (2, 2), (3, 3), (4, 3))}],
        [(3, 3)]
    ),
    # # Too much distance for movement
    (
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((4, 5), (5, 6), (7, 7))}],
        [(5, 6)]
    ),
])
def test_simple_moves_in_dirt_map(dirty_map, input, expected):
    assert_fixtures(dirty_map, input, expected)


@pytest.mark.parametrize(('input', 'expected'), [
    (   # No collision normal movement
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((3, 4), (3, 5), (3, 6))},
        {'name': 'PirceB',
        'side': 'B',
        'movement': ((5, 6), (5, 7))}],
        [(3, 6), (5, 7)]
    ),
    # ( # Colision different groups
    #     [{'name': 'PirceA',
    #     'side': 'A',
    #     'movement': ((4, 5), (5, 6), (6, 6), (7, 7))},
    #     {'name': 'PirceB',
    #     'side': 'B',
    #     'movement': ((6, 6), (6, 7))}],
    #     [(6, 6), (6, 7)]
    # ),
    (   # Colision same group same destination
        [{'name': 'PirceA',
        'side': 'A',
        'movement': ((4, 4), (5, 5), (6, 6),)},
        {'name': 'PirceB',
        'side': 'A',
        'movement': ((7, 6), (6, 6), (6, 7))}],
        [(6, 6), (6, 7)]
    ),
    # (    # Colision same group delaied destination
    #     [{'name': 'PirceA',
    #     'side': 'A',
    #     'movement': ((7, 7), (7, 6), (6, 7),)},
    #     {'name': 'PirceB',
    #     'side': 'A',
    #     'movement': ((7, 6), (6, 6), (7, 7))}],
    #     [(6, 7), (7, 7)]
    # ),
#     # Colision same group unreacheable closed destination
#     (
#         [{'name': 'PirceA',
#         'side': 'A',
#         'movement': ((7,7), (6,7),)},
#         {'name': 'PirceB',
#         'side': 'A',
#         'movement': ((7,6), (6,6), (6,7), (5,6), )}],
#         [(6,7), (6,6)]
#     ),
])
def test_concurrent_moves(clean_map, input, expected):
    assert_fixtures(clean_map, input, expected)
