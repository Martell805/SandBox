from random import shuffle

from cell import Cell
from blocks.default_blocks import Block
from moves.move import Move
from moves.sequential_move_set import SMoves


class SolidBlock(Block):
    id = 'sb_solid_block'
    density = 5000
    durability = 5000
    movable = True
    color = (255, 255, 255)

    def can_move_in_cell(self, cell: Cell) -> bool:
        return cell.contains.movable and cell.contains.density < self.density

    def can_update_cell(self, cell: Cell) -> bool:
        return cell.is_free() and self.can_move_in_cell(cell)

    def go_down_straight(self, neighbours: list[list[Cell]]) -> bool:
        if self.can_update_cell(neighbours[2][1]):
            neighbours[2][1].calculated = self
            neighbours[1][1].calculated = neighbours[2][1].contains
            return True

        return False

    def check_for_immovable(self, neighbours) -> bool:
        return not self.movable

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

    def init_moves(self):
        self.moves = SMoves(
            Move(self.check_for_immovable),
            Move(self.go_down_straight),
            Move(self.go_down_diagonal)
        )


class Sand(SolidBlock):
    id = 'sb_sand'
    density = 3000
    durability = 3000
    color = (252, 221, 118)


class Stone(SolidBlock):
    id = 'sb_stone'
    density = 5000
    durability = 5000
    color = (200, 200, 200)


class Granite(SolidBlock):
    color = (173, 165, 135)
    density = 11000
    durability = 11000
    id = 'sb_granite'


class Ice(SolidBlock):
    id = 'sb_ice'
    density = 900
    durability = 900
    color = (219, 241, 253)


class BlackSand(Sand):
    id = 'sb_black_sand'
    density = 3000
    durability = 3000
    color = (20, 10, 5)
