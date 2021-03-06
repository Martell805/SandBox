# VERSION 2.1.4

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame

from field import Field

from blocks.default_blocks import Wall
from blocks.solid_blocks import Sand, Stone, Granite
from blocks.fluid_blocks import Void, Water, Oil, Acid
from blocks.air_blocks import CarbonicGas, Gas
from blocks.wire_blocks import Wire, Signal, Detector, Creator, Spark


class SandBox:
    TPS = 30
    FIELD_SIZE = 50
    TILE_SIZE = 16
    selected_block_type = Sand
    selected_block = Sand(0, 0, 0)

    BLOCK_LIST = [Wall, Sand, Stone, Granite, Water,
                  Oil,  Acid, CarbonicGas, Gas, Wire,
                  Signal, Detector, Creator, Spark]

    KEY_LIST = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_q, pygame.K_w,
                pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i]

    def __init__(self):
        self.SCREEN_SIZE = self.FIELD_SIZE * self.TILE_SIZE

        pygame.init()
        pygame.display.set_caption('SandBox')

        self.screen = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))
        self.sb_field = Field(self.FIELD_SIZE)
        self.pause = False
        self.clock = pygame.time.Clock()

    def pickBlock(self, key):
        try:
            return self.BLOCK_LIST[self.KEY_LIST.index(key)]
        except (ValueError, IndexError):
            return self.selected_block_type

    def handle_events(self):
        x_pos = pygame.mouse.get_pos()[0] // self.TILE_SIZE + 1
        y_pos = pygame.mouse.get_pos()[1] // self.TILE_SIZE + 1
        if pygame.mouse.get_pressed(3)[0]:
            self.sb_field.set(x_pos, y_pos, self.selected_block_type)
        elif pygame.mouse.get_pressed(3)[1]:
            selected_block = self.sb_field[x_pos][y_pos]
            if not isinstance(selected_block, (Void, self.selected_block_type)):
                self.selected_block_type = type(selected_block)
            print(f"Вы выбрали {selected_block}")
        elif pygame.mouse.get_pressed(3)[2]:
            self.sb_field.set(x_pos, y_pos, Void)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause

                self.selected_block_type = self.pickBlock(event.key)

    def run(self):
        while True:
            if not self.pause:
                self.sb_field.update()
                pygame.display.set_caption(f'SandBox (tick {self.sb_field.tick}) {self.clock.get_fps():.2f} TPS')

            self.handle_events()

            self.sb_field.draw(self.screen, self.TILE_SIZE)

            self.clock.tick(self.TPS)
            pygame.display.flip()

    def start(self):
        control_tip = "Управление: \n" \
                      "Чтобы поставить мир на паузу нажмите SPACE На ПКМ всегда ставится Void. \n" \
                      "Чтобы изменить блок на ЛКМ выберите егоб нажав на клавишу, указанную в списке."
        print(control_tip)
        print("Список блоков:")
        for q, block_type in enumerate(self.BLOCK_LIST):
            print(f"{pygame.key.name(self.KEY_LIST[q])}. {block_type.__name__}")

        self.run()


if __name__ == '__main__':
    sand_box = SandBox()
    sand_box.start()
