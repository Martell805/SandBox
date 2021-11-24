import pygame


class Block:
    density = 1000000000000000
    movable = False
    id = 'sb_block'
    color = (0, 0, 0)

    def __init__(self, x, y, tick):
        self.x = x
        self.y = y
        self.tick = tick

    def __repr__(self):
        return f"{self.id}: {(self.x, self.y)}"

    def update(self, field):
        pass

    def draw(self, surface, ts):
        pygame.draw.rect(surface, self.color, (self.x * ts, self.y * ts, ts, ts))


class Wall(Block):
    color = (136, 69, 53)
    id = 'sb_wall'

