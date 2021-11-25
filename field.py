import pygame.surface
from blocks.default_blocks import Wall
from blocks.fluid_blocks import Void

from random import shuffle


class Field:
    tick = 0

    def __init__(self, size: int):
        self.size = size + 2

        self.field = [[Void(q, w, self.tick) for w in range(self.size)] for q in range(self.size)]

        for q in range(self.size):
            for w in range(self.size):
                if q == 0 or q == self.size - 1 or w == 0 or w == self.size - 1:
                    self.field[q][w] = Wall(q, w, self.tick)

    def __getitem__(self, item: int) -> list:
        return self.field[item]

    def set(self, x: int, y: int, block_type: type):
        self.field[x][y] = block_type(x, y, self.tick)

    def get(self, x: int, y: int):
        return self.field[x][y]

    def update(self):

        q_order = list(range(self.size))
        shuffle(q_order)
        w_order = list(range(self.size))
        shuffle(w_order)

        for q in q_order:
            for w in w_order:
                self.field[q][w].update(self)
        self.tick += 1

    def draw(self, screen: pygame.surface, ts: int):
        temp_screen = pygame.surface.Surface((self.size * ts, self.size * ts))

        for q in range(self.size):
            for w in range(self.size):
                self.field[q][w].draw(temp_screen, ts)

        screen.blit(temp_screen, (-ts, -ts))
