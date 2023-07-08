import pygame

from config import TILE_SIZE


class Cell:
    def __init__(self, x: int, y: int, contains):
        self.contains = contains
        self.x = x
        self.y = y
        self.calculated = None
        self.neighbours = []

    def calculate_neighbours(self, size, grid):
        x = self.x
        y = self.y

        self.neighbours = [
            [grid[x - 1][y - 1],            grid[x][y - 1],        grid[(x + 1) % size][y - 1]],
            [grid[x - 1][y],                self,                           grid[(x + 1) % size][y % size]],
            [grid[x - 1][(y + 1) % size],   grid[x % size][(y + 1) % size], grid[(x + 1) % size][(y + 1) % size]],
        ]

    def set_calculated(self, block) -> None:
        self.calculated = block

    def set(self, block) -> None:
        self.contains = block
        self.calculated = block

    def is_free(self) -> bool:
        return self.calculated is None

    def update(self) -> None:
        if self.is_free():
            self.contains.update(self.neighbours)

    def calculate(self) -> None:
        if self.calculated is None:
            return

        self.contains = self.calculated
        self.calculated = None

    def draw_on_surface(self, surface, x, y, surface_tile_size) -> None:
        pygame.draw.rect(surface, self.contains.color,
                         (x * surface_tile_size, y * surface_tile_size, surface_tile_size, surface_tile_size))

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.contains.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def __repr__(self):
        return f"Cell(({self.x}, {self.y}), {self.contains} -> {self.calculated})"
