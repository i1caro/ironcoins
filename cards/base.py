from cards.exceptions import ErrorCreatureOwner
from cards.exceptions import InvalidParameter
from cards.exceptions import CreatureNotFound
from mapchart.models import HexMap as Map


def play_card(hexmap, player, card, targets):
    result = {'card': card}
    piece = hexmap.get_piece(*targets[0])
    result.update(movement(hexmap, player, piece, targets[0] + targets[1]))
    return result


def movement(hexmap, player, target_creature, moves):
    if player.side != target_creature.side:
        error = 'at movement player {} != {}'
        raise ErrorCreatureOwner(
            error.format(player.side, target_creature.side)
        )

    creature_location = moves[0]
    if hexmap.get_piece(*creature_location) is not target_creature:
        piece = hexmap.get_piece(*creature_location)
        error = 'at movement {}[{}] != {}'
        raise CreatureNotFound(
            error.format(piece, creature_location, target_creature)
        )

    for previous, current in zip(moves[:-1], moves[1:]):
        if not Map.are_close(previous, current):
            raise InvalidParameter('moves {}'.format(moves))

    result = {
        'map': moves[1:],
        'creature': moves[0]
    }
    return result


