import pygame

from config import TILE_SIZE


class Block:
    id: str = 'sbn_block'
    density: int = 1000000000000000
    durability: int = 1000000000000000

    movable: bool = False
    electrified: bool = False
    simple: bool = True
    color: tuple[int, int, int] = (255, 0, 255)
    surface: pygame.Surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def __repr__(self):
        return f"{self.id}"

    def lock(self, unlocked=False):
        self.movable = unlocked

    def update(self, neighbours):
        pass

    def draw(self):
        self.surface.fill(self.color)
        return self.surface


class Wall(Block):
    id = 'sbn_wall'
    color = (136, 69, 53)


class Void(Block):
    id = 'sbn_void'
    density = 0
    color = (55, 55, 55)
    updates = False
    movable = True


