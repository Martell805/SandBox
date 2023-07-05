from random import shuffle, getrandbits

from cell import Cell
from new_blocks.default_blocks import Block


class SolidBlock(Block):
    id = 'sbn_solid_block'
    density = 5000
    durability = 5000
    movable = True
    color = (255, 255, 255)

    def can_move_in_cell(self, cell: Cell) -> bool:
        return cell.contains.movable and cell.contains.density < self.density

    def can_update_cell(self, cell: Cell) -> bool:
        return cell.is_free() and self.can_move_in_cell(cell)

    def go_down_straight(self, neighbours: list[list[Cell]]) -> bool:
        if self.can_move_in_cell(neighbours[2][1]):
            neighbours[2][1].calculated = self
            neighbours[1][1].calculated = neighbours[2][1].contains
            return True

        return False

    def go_down_diagonal(self, neighbours: list[list[Cell]]) -> bool:
        ways = [0, 2]
        shuffle(ways)

        if self.can_move_in_cell(neighbours[1][ways[0]]) and self.can_update_cell(neighbours[2][ways[0]]):
            neighbours[2][ways[0]].calculated = self
            neighbours[1][1].calculated = neighbours[2][ways[0]].contains
            return True

        if self.can_move_in_cell(neighbours[1][ways[1]]) and self.can_update_cell(neighbours[2][ways[1]]):
            neighbours[2][ways[1]].calculated = self
            neighbours[1][1].calculated = neighbours[2][ways[1]].contains
            return True

        return False

    def go_down(self, neighbours: list[list[Cell]]) -> bool:
        if self.go_down_straight(neighbours):
            return True

        if self.go_down_diagonal(neighbours):
            return True

        return False

    def update(self, neighbours: list[list[Cell]]) -> None:
        if not self.movable:
            return

        if self.go_down(neighbours):
            return


class Sand(SolidBlock):
    id = 'sbn_sand'
    density = 3000
    durability = 3000
    color = (252, 221, 118)


class Stone(SolidBlock):
    id = 'sbn_stone'
    density = 5000
    durability = 5000
    color = (200, 200, 200)


class Granite(SolidBlock):
    color = (173, 165, 135)
    density = 11000
    durability = 11000
    id = 'sbn_granite'


class Ice(SolidBlock):
    id = 'sbn_ice'
    density = 900
    durability = 900
    color = (219, 241, 253)


class BlackSand(Sand):
    id = 'sbn_black_sand'
    density = 3000
    durability = 3000
    color = (20, 10, 5)
