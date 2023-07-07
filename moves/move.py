class Move:
    def __init__(self, move):
        self.move = move

    def perform(self, neighbours) -> bool:
        return self.move(neighbours)
