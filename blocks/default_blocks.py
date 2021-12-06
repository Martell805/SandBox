import pygame
from dataclasses import dataclass
from dataclasses import field as f


@dataclass(frozen=True)
class Block:
    id: str = f(default='sb_block', init=False)
    density: int = f(default=1000000000000000, init=False)
    movable: bool = f(default=False, init=False)
    destructible: bool = f(default=False, init=False)
    color: tuple[int, int, int] = f(default=(255, 0, 255), init=False)
    x: int
    y: int
    tick: int

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
    id = 'sb_wall'
    color = (136, 69, 53)
