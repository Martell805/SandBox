class SequentialMoveSet:
    def __init__(self, *moves):
        self.moves = list(moves)

    def perform(self, neighbours) -> bool:
        for move in self.moves:
            if move.perform(neighbours):
                return True

        return False


SMoves = SequentialMoveSet
