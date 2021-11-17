from blocks.immovable_blocks import Wall
from blocks.solid_blocks import Void


class Field:
    def __init__(self, size):
        self.tick = 0
        self.size = size

        self.field = [[Void(q, w, self.tick) for w in range(self.size)] for q in range(self.size)]

        for q in range(self.size):
            for w in range(self.size):
                if q == 0 or q == self.size - 1 or w == 0 or w == self.size - 1:
                    self.field[q][w] = Wall(q, w, self.tick)

    def set(self, x, y, type):
        self.field[x][y] = type(x, y, self.tick)

    def get(self, x, y):
        return self.field[x][y]

    def update(self):
        for q in range(self.size):
            for w in range(self.size):
                self.field[q][w].update(self)
        self.tick += 1

    def draw(self, screen, ts):
        for q in range(self.size):
            for w in range(self.size):
                self.field[q][w].draw(screen, ts)
