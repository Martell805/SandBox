from random import shuffle

from cell import Cell


class RandomMoveSet:
    def __init__(self, *moves):
        self.moves = list(moves)

    def perform(self, neighbours: [list[list[Cell]]]) -> bool:
        shuffle(self.moves)

        for move in self.moves:
            if move.perform(neighbours):
                return True

        return False


RMoves = RandomMoveSet
