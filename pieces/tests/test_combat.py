from pieces.models import Figure
from pieces.engine import Combat

import pytest


def create_figure(**kwargs):
    stats = kwargs or dict()
    defaults = {'life': 10}
    defaults.update(stats)
    return Figure(name='a', side='',
                  stats=defaults)


@pytest.mark.parametrize(('stats_a', 'stats_b', 'life'), [
    (  # Ranged win
        {'ranged_power': 10},
        {},
        {'figure_a': 10, 'figure_b': 0}
    ),
    (  # Victory Melle
        {'ranged_power': 10, 'melle_power': 10},
        {'ranged_power': 10},
        {'figure_a': 10, 'figure_b': 0}
    ),
    (  # Victory infernal
        {'ranged_power': 10, 'melle_power': 10, 'infernal_power': 10},
        {'ranged_power': 10, 'melle_power': 10},
        {'figure_a': 10, 'figure_b': 0}
    ),
    (  # Tie
        {'ranged_power': 10},
        {'ranged_power': 10},
        {'figure_a': 10, 'figure_b': 10}
    ),
    (  # win at second round
        {'ranged_power': 5},
        {},
        {'figure_a': 10, 'figure_b': 0}
    ),
])
def test_fight_wins_a(stats_a, stats_b, life):
    figure_a = create_figure(**stats_a)
    figure_b = create_figure(**stats_b)

    Combat(figure_a, figure_b).resolve()

    assert figure_a.get('life') == life['figure_a']
    assert figure_b.get('life') == life['figure_b']

