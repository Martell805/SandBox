import pygame


class Block:
    density = 1000000000000000
    movable = False
    destructible = False
    id = 'sb_block'
    color = (255, 0, 255)

    def __init__(self, x: int, y: int, tick: int):
        self.x = x
        self.y = y
        self.tick = tick

    def __repr__(self):
        return f"{self.id}: {(self.x, self.y)}"

    def update_wire(self, field):
        return None

    def update(self, field):
        pass

    def draw(self, surface: pygame.surface, tile_size: int):
        pygame.draw.rect(surface, self.color,
                         (self.x * tile_size, self.y * tile_size, tile_size, tile_size))


class Wall(Block):
    color = (136, 69, 53)
    id = 'sb_wall'

