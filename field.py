import pygame.surface
from blocks.default_blocks import Wall
from blocks.fluid_blocks import Void

from random import shuffle


class Field:
    tick = 0

    def __init__(self, size: int):
        self.size = size + 2

        self.field = [[Void(x, y, self.tick) for y in range(self.size)] for x in range(self.size)]
        self.wire_changes = [[None for _ in range(self.size)] for _ in range(self.size)]

        for x in range(self.size):
            for y in range(self.size):
                if x == 0 or x == self.size - 1 or y == 0 or y == self.size - 1:
                    self.set(x, y, Wall)

    def __getitem__(self, item: int) -> list:
        return self.field[item]

    def set(self, x: int, y: int, block_type: type):
        """Sets block of block_type in (x, y)"""
        if self.field[x][y].__class__ != block_type:
            self.field[x][y] = block_type(x, y, self.tick)

    def get(self, x: int, y: int):
        """Returns block in (x, y)"""
        return self.field[x][y]
    
    def update_wire(self):
        """Updates all wire on field"""
        for x in range(self.size):
            for y in range(self.size):
                self.wire_changes[x][y] = self.field[x][y].update_wire(self.field)
                if self.wire_changes[x][y] is not None:
                    print(self.wire_changes[x][y])

    def update(self):
        """Updates all blocks on field"""
        self.update_wire()

        x_order = list(range(self.size))
        shuffle(x_order)
        y_order = list(range(self.size))
        shuffle(y_order)

        for x in x_order:
            for y in y_order:
                if self.wire_changes[x][y] is not None:
                    self.set(x, y, self.wire_changes[x][y])
                    self.wire_changes[x][y] = None
                self.field[x][y].update(self)
            
        self.tick += 1

    def draw(self, screen: pygame.surface, ts: int):
        """Draws all blocks on field"""
        temp_screen = pygame.surface.Surface((self.size * ts, self.size * ts))
        temp_screen.fill((55, 55, 55))

        for x in range(self.size):
            for y in range(self.size):
                if self.field[x][y].id != 'sb_void':
                    self.field[x][y].draw(temp_screen, ts)

        screen.blit(temp_screen, (-ts, -ts))
