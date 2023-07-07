from cell import Cell


class SequentialMoveSet:
    def __init__(self, *moves):
        self.moves = list(moves)

    def perform(self, neighbours: [list[list[Cell]]]) -> bool:
        for move in self.moves:
            if move.perform(neighbours):
                return True

        return False


SMoves = SequentialMoveSet
