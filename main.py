# VERSION 3.6.0

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame

from config import *

from field import Field

from blocks.default_blocks import Wall, Void
from blocks.solid_blocks import Sand, Stone, Granite, Ice, BlackSand
from blocks.fluid_blocks import Water, Oil, Acid
from blocks.gas_blocks import CarbonicGas, Gas
from blocks.wire_blocks import Spark, Wire, InactiveDetector, Creator


class SandBox:
    BLOCK_LIST = [
        Wall, Sand, Stone, Granite, BlackSand,
        Ice, Water, Oil, Acid,
        CarbonicGas, Gas,
        Spark, Wire, InactiveDetector, Creator
    ]

    KEY_LIST = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_q, pygame.K_w,
                pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i]

    UI_WIDTH = 400

    MINI_WINDOW_TILES = 15
    MINI_WINDOW_TILE_SIZE = 20
    MINI_WINDOW_SIZE = MINI_WINDOW_TILES * MINI_WINDOW_TILE_SIZE

    def __init__(self):
        self.selected_block_type = Sand
        self.SCREEN_SIZE = FIELD_SIZE * TILE_SIZE

        pygame.init()
        pygame.display.set_caption('SandBox')

        self.screen = pygame.display.set_mode((self.SCREEN_SIZE + self.UI_WIDTH, self.SCREEN_SIZE))
        self.sb_field = Field(FIELD_SIZE)
        self.clock = pygame.time.Clock()
        self.pause = False
        self.placement_radius = 1
        self.window_x = -1
        self.window_y = -1

    def pickBlock(self, key):
        try:
            result = self.BLOCK_LIST[self.KEY_LIST.index(key)]
            return result
        except (ValueError, IndexError):
            return self.selected_block_type

    def place_blocks(self, x_pos, y_pos, block_type):
        for x in range(1, FIELD_SIZE + 1):
            for y in range(1, FIELD_SIZE + 1):
                if (x - x_pos) ** 2 + (y - y_pos) ** 2 < self.placement_radius ** 2:
                    self.sb_field.set(x, y, block_type())

    def handle_mouse_in_mini_window(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        correct_x = (
                self.SCREEN_SIZE + (self.UI_WIDTH - self.MINI_WINDOW_SIZE) // 2
                <= mouse_x <=
                self.SCREEN_SIZE + (self.UI_WIDTH - self.MINI_WINDOW_SIZE) // 2 + self.MINI_WINDOW_SIZE
        )

        correct_y = 400 <= mouse_y <= 400 + self.MINI_WINDOW_SIZE

        if not correct_x or not correct_y:
            return False

        rel_pos_x = self.window_x + (mouse_x - (self.SCREEN_SIZE + (self.UI_WIDTH - self.MINI_WINDOW_SIZE) // 2)) // self.MINI_WINDOW_TILE_SIZE
        rel_pos_y = self.window_y + (mouse_y - 400) // self.MINI_WINDOW_TILE_SIZE

        if pygame.mouse.get_pressed(3)[0]:
            if pygame.key.get_mods() == 64:
                self.window_x = rel_pos_x
                self.window_y = rel_pos_y
                return
            self.place_blocks(rel_pos_x, rel_pos_y, self.selected_block_type)
        elif pygame.mouse.get_pressed(3)[1]:
            selected_block = self.sb_field.get(rel_pos_x, rel_pos_y)
            if type(selected_block) not in (Void, self.selected_block_type):
                self.selected_block_type = type(selected_block)
                self.screen.blit(self.draw_ui(), (self.SCREEN_SIZE, 0))
        elif pygame.mouse.get_pressed(3)[2]:
            self.place_blocks(rel_pos_x, rel_pos_y, Void)

        return True

    def handle_mouse(self):
        x_pos = pygame.mouse.get_pos()[0] // TILE_SIZE + 1
        y_pos = pygame.mouse.get_pos()[1] // TILE_SIZE + 1

        if self.handle_mouse_in_mini_window():
            return

        if 0 > x_pos or x_pos > FIELD_SIZE + 1 or 0 > y_pos or y_pos > FIELD_SIZE + 1:
            return

        if pygame.mouse.get_pressed(3)[0]:
            if pygame.key.get_mods() == 64:
                self.window_x = x_pos
                self.window_y = y_pos
                return
            self.place_blocks(x_pos, y_pos, self.selected_block_type)
        elif pygame.mouse.get_pressed(3)[1]:
            selected_block = self.sb_field.get(x_pos, y_pos)
            if type(selected_block) not in (Void, self.selected_block_type):
                self.selected_block_type = type(selected_block)
                self.screen.blit(self.draw_ui(), (self.SCREEN_SIZE, 0))
        elif pygame.mouse.get_pressed(3)[2]:
            self.place_blocks(x_pos, y_pos, Void)

    def handle_events(self):
        self.handle_mouse()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause
                    continue

                self.selected_block_type = self.pickBlock(event.key)
                self.screen.blit(self.draw_ui(), (self.SCREEN_SIZE, 0))

            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.placement_radius += 1
                else:
                    self.placement_radius -= 1
                    self.placement_radius = max(self.placement_radius, 1)

                self.screen.blit(self.draw_ui(), (self.SCREEN_SIZE, 0))

    def draw_text(self, surface: pygame.Surface, x: int, y: int, text: str,
                  size: int = 20,
                  color: tuple[int, int, int] = (255, 255, 255),
                  font: str = 'Times New Roman'):
        font = pygame.font.SysFont(font, size)

        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def draw_mini_window(self):
        if pygame.key.get_mods() == 64:
            hint_x = pygame.mouse.get_pos()[0] // TILE_SIZE * TILE_SIZE
            hint_y = pygame.mouse.get_pos()[1] // TILE_SIZE * TILE_SIZE

            pygame.draw.rect(self.screen, (255, 255, 255),
                             (hint_x, hint_y,
                              self.MINI_WINDOW_TILES * TILE_SIZE, self.MINI_WINDOW_TILES * TILE_SIZE),
                             2)

        surface = pygame.Surface((self.MINI_WINDOW_SIZE, self.MINI_WINDOW_SIZE))

        if self.window_x == -1:
            surface.fill((100, 100, 0))
            self.screen.blit(surface, (self.SCREEN_SIZE + (self.UI_WIDTH - self.MINI_WINDOW_SIZE) // 2, 400))
            return

        if self.window_x + self.MINI_WINDOW_TILES >= FIELD_SIZE:
            self.window_x = FIELD_SIZE - self.MINI_WINDOW_TILES + 1

        if self.window_y + self.MINI_WINDOW_TILES >= FIELD_SIZE:
            self.window_y = FIELD_SIZE - self.MINI_WINDOW_TILES + 1

        for x in range(0, self.MINI_WINDOW_TILES):
            for y in range(0, self.MINI_WINDOW_TILES):
                real_x = self.window_x + x
                real_y = self.window_y + y
                self.sb_field[real_x][real_y].draw_on_surface(surface, x, y, self.MINI_WINDOW_TILE_SIZE)

        self.screen.blit(surface, (self.SCREEN_SIZE + (self.UI_WIDTH - self.MINI_WINDOW_SIZE) // 2, 400))

    def draw_ui(self):
        surface = pygame.Surface((self.UI_WIDTH, self.SCREEN_SIZE))

        self.draw_text(surface, 10, 10, f"SandBox", 30)
        self.draw_text(surface, 10, 50, f"Placement radius: {self.placement_radius}")
        self.draw_text(surface, 10, 80, f"Selected block: {self.selected_block_type.id}")

        return surface

    def run(self):
        while True:
            if not self.pause:
                self.sb_field.update()
                pygame.display.set_caption(f'SandBox (tick {self.sb_field.tick}) {self.clock.get_fps():.2f} TPS')

            self.handle_events()

            self.sb_field.draw(self.screen)
            self.draw_mini_window()

            self.clock.tick(TPS)
            pygame.display.flip()

    def start(self):
        control_tip = "Управление: \n" \
                      "Чтобы поставить мир на паузу нажмите SPACE На ПКМ всегда ставится Void. \n" \
                      "Чтобы изменить блок на ЛКМ выберите его, нажав на клавишу, указанную в списке."
        print(control_tip)
        print("Список блоков:")
        for q, block_type in enumerate(self.BLOCK_LIST):
            print(f"{pygame.key.name(self.KEY_LIST[q])}. {block_type.__name__}")

        self.screen.blit(self.draw_ui(), (self.SCREEN_SIZE, 0))
        self.run()


if __name__ == '__main__':
    sand_box = SandBox()
    sand_box.start()
