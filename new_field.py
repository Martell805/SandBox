import pygame.surface
from new_blocks.default_blocks import Wall, Block, Void
from cell import Cell

from random import shuffle

from config import TILE_SIZE


class Field:
    tick = 0

    def __init__(self, size: int):
        self.size = size + 2

        self.field: list[list[Cell]] = [[Cell(x, y, Wall())
                                         if x == 0 or x == self.size - 1 or y == 0 or y == self.size - 1 else
                                         Cell(x, y, Void())
                                         for y in range(self.size)]
                                        for x in range(self.size)]

        self.cell_list: list[Cell] = [cell for row in self.field for cell in row]

        for x, row in enumerate(self.field):
            for y, cell in enumerate(row):
                cell.calculate_neighbours(self.size, self.field)

    def __getitem__(self, item: int) -> list[Cell]:
        return self.field[item]

    def set(self, x: int, y: int, block) -> None:
        if not isinstance(block, self.field[x][y].__class__):
            self.field[x][y].set(block)

    def get(self, x: int, y: int) -> Block:
        return self.field[x][y].contains

    def update(self):
        shuffle(self.cell_list)
        for cell in self.cell_list:
            cell.update()

        for cell in self.cell_list:
            cell.calculate()
            
        self.tick += 1

    def draw(self, screen: pygame.surface):
        temp_screen = pygame.surface.Surface((self.size * TILE_SIZE, self.size * TILE_SIZE))
        temp_screen.fill((55, 55, 55))

        for x in range(self.size):
            for y in range(self.size):
                self.field[x][y].draw(temp_screen)

        screen.blit(temp_screen, (-TILE_SIZE, -TILE_SIZE))
