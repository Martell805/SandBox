from random import shuffle


class RandomMoveSet:
    def __init__(self, *moves):
        self.moves = list(moves)

    def perform(self, neighbours) -> bool:
        shuffle(self.moves)

        for move in self.moves:
            if move.perform(neighbours):
                return True

        return False


RMoves = RandomMoveSet
