from pieces.models import Figure
from cards.exceptions import WrongOwner


def movement(player, target, moves):
    if player.side != target.side:
        error = 'at movement player {} != target {}'
        raise WrongOwner(error.format(player.side, target.side))

    result = {
        'now': [
            [Figure, 'Naruto', ['stats', 'movement', 'turn_add'], [-2]]
        ],
        'end_turn': [
            [Figure, 'Naruto', ['move'], [(1, 2), (1, 3)]]
        ]
    }
    return result

