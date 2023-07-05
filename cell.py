import pygame

from config import TILE_SIZE
from new_blocks.default_blocks import Block


class Cell:
    def __init__(self, x: int, y: int, contains):
        self.contains: Block = contains
        self.x = x
        self.y = y
        self.calculated = None
        self.neighbours = []

    def calculate_neighbours(self, size, grid):
        x = self.x
        y = self.y

        self.neighbours = [
            [grid[x - 1][y - 1],            grid[x][y],                     grid[(x + 1) % size][y - 1]],
            [grid[x - 1][y],                self,                           grid[(x + 1) % size][y % size]],
            [grid[x - 1][(y + 1) % size],   grid[x % size][(y + 1) % size], grid[(x + 1) % size][(y + 1) % size]],
        ]

    def set_calculated(self, block):
        self.calculated = block

    def set(self, block):
        self.contains = block
        self.calculated = block

    def is_free(self):
        return self.calculated is None

    def update(self):
        if self.is_free():
            self.contains.update(self.neighbours)

    def calculate(self):
        if self.calculated is None:
            return

        self.contains = self.calculated
        self.calculated = None

    def draw(self, surface):
        if self.contains.simple:
            pygame.draw.rect(surface, self.contains.color,
                             (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            return

        surface.blit(self.contains.draw(), (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def __repr__(self):
        return f"Cell(({self.x}, {self.y}), {self.contains} -> {self.calculated})"