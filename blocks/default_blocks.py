import pygame
from pygame import Surface

from cell import Cell
from config import TILE_SIZE
from moves.sequential_move_set import SMoves


class Block:
    id: str = 'sb_block'
    density: int = 1000000000000000
    durability: int = 1000000000000000

    movable: bool = False
    simple: bool = True
    color: tuple[int, int, int] = (255, 0, 255)
    surface: pygame.Surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
    moves = SMoves()

    def __init__(self):
        self.init_moves()

    def __eq__(self, other):
        return self.id == other.id

    def init_moves(self) -> None:
        pass

    def __repr__(self):
        return f"{self.id}"

    def lock(self) -> None:
        self.movable = False

    def unlock(self) -> None:
        self.movable = True

    def update(self, neighbours: list[list[Cell]]) -> None:
        self.moves.perform(neighbours)

    def draw(self) -> Surface:
        self.surface.fill(self.color)
        return self.surface


class Wall(Block):
    id = 'sb_wall'
    color = (136, 69, 53)


class Void(Block):
    id = 'sb_void'
    density = 0
    color = (55, 55, 55)
    updates = False
    movable = True


