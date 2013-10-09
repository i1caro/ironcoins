from mapchart.constants import IMPASSABLE as X
from mapchart.constants import GRASS as o
from mapchart.models import MapMatrix as Map


import pytest


@pytest.fixture
def dirty_map():
    dirty_map = [
        [o, o, o, o, o, o, o, o],
        [o, X, o, X, o, X, X, X],
        [o, o, o, o, o, o, o, o],
        [o, X, o, X, X, X, X, X],
        [o, o, o, o, o, o, o, o],
        [o, o, X, o, o, o, o, o],
        [o, o, o, o, X, o, o, o],
        [o, o, o, o, o, o, X, o],
        [o, o, o, o, o, o, o, o],
        [o, o, o, o, o, o, o, o],
    ]
    return Map('dirty_map', dirty_map)


@pytest.fixture
def clean_map():
    clean_map = [[o for y in range(10)]
        for x in range(10)]
    return Map('clean_map', clean_map)

@pytest.mark.skipif(True)
@pytest.mark.parametrize(('input', 'expected'), [
    # Normal movement
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((0,0), (1,1), (1,3), (3,3), (4,4))}],
        [(4,4)]
    ),
    # Xnvalid movement
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((4,5), (4,6), (7,8))}],
        [(4,6)]
    ),
    # Xnvalid location for movement
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((4,5), (5,5), (5,6))}],
        [(5,5)]
    ),
])
def test_simple_moves_in_dirt_map(dirty_map, input, expected):
    results = resolve_movement(dirty_map, input)
    for result, expect in zip(results, expected):
        assert result == expected


@pytest.mark.skipif(True)
@pytest.mark.parametrize(('input', 'expected'), [
    # Colision different groups
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((4,5), (5,6), (6,6), (7,7))},
        {'id': 'PirceB'
        'group': 'B',
        'movement': ((6,6), (6,7))}],
        [(6,6), (6,7)]
    ),
    # Colision same group same destination
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((4,4), (5,5), (6,6),)},
        {'id': 'PirceB'
        'group': 'A',
        'movement': ((7,7), (6,6), (6,7))}],
        [(6,6), (6,7)]
    ),
    # Colision same group delaied destination
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((7,7), (6,6), (6,7),)},
        {'id': 'PirceB'
        'group': 'A',
        'movement': ((7,6), (6,6), (7,7))}],
        [(6,7), (7,7)]
    ),
    # Colision same group unreacheable close destination
    (
        [{'id': 'PirceA'
        'group': 'A',
        'movement': ((7,7), (6,7),)},
        {'id': 'PirceB'
        'group': 'A',
        'movement': ((7,6), (6,6), (6,7), (5,6), )}],
        [(6,7), (6,6)]
    ),
])
def test_simple_moves_in_dirt_map(dirty_map, input, expected):
    results = resolve_movement(dirty_map, input)
    for result, expect in zip(results, expected):
        assert result == expected



