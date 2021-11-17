import pygame

from field import Field
from blocks.solid_blocks import Void, Sand, Stone


class SandBox:
    def __init__(self):
        self.FPS = 60
        self.FIELD_SIZE = 50
        self.TILE_SIZE = 16

        self.SCREEN_SIZE = self.FIELD_SIZE * self.TILE_SIZE

        pygame.init()
        pygame.display.set_caption('SandBox (tick 0)')

        self.screen = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))

        self.sb_field = Field(self.FIELD_SIZE)

        self.pause = False

        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.sb_field.set(event.pos[0] // self.TILE_SIZE, event.pos[1] // self.TILE_SIZE, Sand)
            elif event.button == 2:
                self.sb_field.set(event.pos[0] // self.TILE_SIZE, event.pos[1] // self.TILE_SIZE, Stone)
            elif event.button == 3:
                self.sb_field.set(event.pos[0] // self.TILE_SIZE, event.pos[1] // self.TILE_SIZE, Void)

        elif event.type == pygame.KEYUP:
            if event.key == 32:
                self.pause = not self.pause

    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)

            if not self.pause:
                self.sb_field.update()
                pygame.display.set_caption(f'SandBox (tick {self.sb_field.tick})')

            self.sb_field.draw(self.screen, self.TILE_SIZE)

            self.clock.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    sand_box = SandBox()
    sand_box.run()
