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
        moves = self.add_current_move(figure, movement)
        return (figure, moves)
        # return (figure, izip(moves[:-1], moves[1:]))

    def resolve(self, moves_pieces):
        result = list()
        clean_moves_pieces = [self.clean_movement(**moves_piece)
            for moves_piece in moves_pieces]

        for piece, moves in clean_moves_pieces:
            last_stand = self.run_until_blocked(piece, moves)
            result.append(last_stand)

        # number_of_items = len(clean_moves_pieces)
        # number_of_movement_ends = 0
        # while number_of_items >= number_of_movement_ends:
            # for piece, move in clean_moves_pieces:
            #     try:
            #         previous, current = move.next()
            #     except StopIteration:
            #         number_of_movement_ends += 1
            #     else:
            #         if not (self.is_move_available(current) and
            #             is_hex_distance_reachable(previous,
            #                                       current)):


        return result
