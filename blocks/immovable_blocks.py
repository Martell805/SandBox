import pygame


class Block:
    def __init__(self, x, y, tick):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.tick = tick
        self.density = 0
        self.movable = False
        self.id = 'sb_block'

    def __repr__(self):
        return f"{self.id}: {(self.x, self.y)}"

    def update(self, field):
        pass

    def draw(self, surface, ts):
        pygame.draw.rect(surface, self.color, (self.x * ts, self.y * ts, ts, ts))


class Wall(Block):
    def __init__(self, x, y, tick):
        super().__init__(x, y, tick)
        self.color = (136, 69, 53)
        self.id = 'sb_wall'


