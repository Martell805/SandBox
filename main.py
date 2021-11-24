from os import environ

import pygame

from field import Field

from blocks.default_blocks import Block, Wall
from blocks.solid_blocks import SolidBlock, Sand, Stone
from blocks.fluid_blocks import FluidBlock, Void, Water, Oil
from blocks.air_blocks import AirBlock, Gas

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def pickBlock(event, prev_block):
    match event.key:
        case pygame.K_0:
            return Block
        case pygame.K_1:
            return Wall
        case pygame.K_2:
            return SolidBlock
        case pygame.K_3:
            return Sand
        case pygame.K_4:
            return Stone
        case pygame.K_5:
            return FluidBlock
        case pygame.K_6:
            return Water
        case pygame.K_7:
            return Oil
        case pygame.K_8:
            return AirBlock
        case pygame.K_9:
            return Gas
    return prev_block


class SandBox:
    FPS = 60
    FIELD_SIZE = 50
    TILE_SIZE = 16
    selected_block = Sand

    def __init__(self):
        self.SCREEN_SIZE = self.FIELD_SIZE * self.TILE_SIZE

        pygame.init()
        pygame.display.set_caption('SandBox (tick 0)')

        self.screen = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))

        self.sb_field = Field(self.FIELD_SIZE)

        self.pause = False

        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if pygame.mouse.get_pressed(3)[0]:
            self.sb_field.set(pygame.mouse.get_pos()[0] // self.TILE_SIZE + 1,
                              pygame.mouse.get_pos()[1] // self.TILE_SIZE + 1,
                              self.selected_block)
        elif pygame.mouse.get_pressed(3)[2]:
            self.sb_field.set(pygame.mouse.get_pos()[0] // self.TILE_SIZE + 1,
                              pygame.mouse.get_pos()[1] // self.TILE_SIZE + 1,
                              Void)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.pause = not self.pause

            self.selected_block = pickBlock(event, self.selected_block)

    def run(self):
        print("Чтобы изменить блок на ЛКМ выберите его номер. На ПКМ всегда ставится Void")
        print("Номера блоков:")
        print("0. Block")
        print("1. Wall")
        print("2. SolidBlock")
        print("3. Sand")
        print("4. Stone")
        print("5. FluidBlock")
        print("6. Water")
        print("7. Oil")
        print("8. AirBlock")
        print("9. Gas")

        while True:
            for event in pygame.event.get():
                self.handle_event(event)

            if not self.pause:
                self.sb_field.update()
                pygame.display.set_caption(f'SandBox (tick {self.sb_field.tick})')

            self.sb_field.draw(self.screen, self.TILE_SIZE)

            self.clock.tick(30)
            pygame.display.flip()


if __name__ == '__main__':
    sand_box = SandBox()
    sand_box.run()
