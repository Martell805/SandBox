from random import shuffle

from new_blocks.default_blocks import Block


class SolidBlock(Block):
    id = 'sbn_solid_block'
    density = 5000
    movable = True
    destructible = True
    color = (255, 255, 255)

    def update(self, neighbours):
        if not self.movable:
            return

        if self.can_update_cell(neighbours[2][1]):
            neighbours[2][1].calculated = self
            neighbours[1][1].calculated = neighbours[2][1].contains
            return

        ways = [0, 2]
        shuffle(ways)

        if self.can_move_in_cell(neighbours[1][ways[0]]) and self.can_update_cell(neighbours[2][ways[0]]):
            neighbours[2][ways[0]].calculated = self
            neighbours[1][1].calculated = neighbours[2][ways[0]].contains
            return

        if self.can_move_in_cell(neighbours[1][ways[1]]) and self.can_update_cell(neighbours[2][ways[1]]):
            neighbours[2][ways[1]].calculated = self
            neighbours[1][1].calculated = neighbours[2][ways[1]].contains
            return


class Sand(SolidBlock):
    id = 'sbn_sand'
    density = 3000
    color = (252, 221, 118)


class Stone(SolidBlock):
    id = 'sbn_stone'
    density = 5000
    color = (200, 200, 200)


class Granite(SolidBlock):
    color = (173, 165, 135)
    density = 6000
    destructible = False
    id = 'sbn_granite'
