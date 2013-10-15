from mapchart.constants import IMPASSABLE
from itertools import izip


class MovementEngine():
    def __init__(self, in_map):
        self.in_map = in_map

    def is_move_available(self, move):
        return (self.in_map.cost(move) is not IMPASSABLE)

    def run_until_blocked(self, piece, moves):
        for move in moves:
            try:
                self.in_map.move(piece, move)
            except:
                break
        return self.in_map.get_piece_location(piece)

    def add_current_move(self, figure, movement):
        return (self.in_map.get_piece_location(figure),) + movement

    def clean_movement(self, figure, movement):
        return (figure, iter(movement))

    def resolve(self, moves_pieces):
        result = list()
        clean_moves_pieces = [self.clean_movement(**moves_piece)
            for moves_piece in moves_pieces]

        number_of_items = len(clean_moves_pieces)
        number_of_movement_ends = 0
        pieces_current_move = dict()
        safe_tries = 0
        while number_of_items >= number_of_movement_ends and safe_tries < 10:
            for piece, move in clean_moves_pieces:
                if not pieces_current_move.get(piece):
                    try:
                        current_move = move.next()
                    except StopIteration:
                        number_of_movement_ends += 1
                        continue
                    try:
                        self.in_map.move(piece, current_move)
                    except:
                        safe_tries+=1
                        pieces_current_move[piece] = current_move
                    else:
                        pieces_current_move[piece] = None
                else:
                    current_move = pieces_current_move[piece]
                    try:
                        self.in_map.move(piece, current_move)
                    except:
                        safe_tries+=1
                    else:
                        pieces_current_move[piece] = None
        return result
