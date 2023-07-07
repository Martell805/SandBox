from typing import Callable

from cell import Cell


class Move:
    def __init__(self, move: Callable[[list[list[Cell]]], bool]):
        self.move = move

    def perform(self, neighbours: [list[list[Cell]]]) -> bool:
        return self.move(neighbours)
