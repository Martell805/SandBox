from random import shuffle

from cell import Cell
from new_blocks.default_blocks import Void
from new_blocks.solid_blocks import SolidBlock


class FluidBlock(SolidBlock):
    id = 'sbn_fluid_block'
    density = 500
    durability = 4000
    color = (0, 0, 255)

    side_preference = None

    def go_side(self, neighbours) -> bool:
        if self.side_preference is None:
            self.side_preference = [0, 2]
            shuffle(self.side_preference)

        if self.can_update_cell(neighbours[1][self.side_preference[0]]):
            neighbours[1][self.side_preference[0]].calculated = self
            neighbours[1][1].calculated = neighbours[1][self.side_preference[0]].contains
            return True

        self.side_preference.reverse()

        if self.can_update_cell(neighbours[1][self.side_preference[1]]):
            neighbours[1][self.side_preference[1]].calculated = self
            neighbours[1][1].calculated = neighbours[1][self.side_preference[1]].contains
            return True

        return False

    def go_down_then_side(self, neighbours) -> bool:
        if self.go_down(neighbours):
            return True

        if self.go_side(neighbours):
            return True

        return False

    def update(self, neighbours) -> None:
        if not self.movable:
            return

        if self.go_down_then_side(neighbours):
            return


class Water(FluidBlock):
    id = 'sbn_water'
    density = 1000
    durability = 1000
    color = (0, 149, 182)


class Oil(FluidBlock):
    id = 'sbn_oil'
    density = 800
    durability = 800
    color = (0, 0, 0)


class Acid(FluidBlock):
    id = 'sbn_acid'
    density = 900
    durability = 6000
    power = 6000
    color = (143, 254, 9)

    def can_destroy_cell(self, cell) -> bool:
        return cell.is_free() and self.power > cell.contains.durability

    def get_random_target(self, neighbours) -> Cell | None:
        targets = [neighbours[0][1], neighbours[2][1], neighbours[1][0], neighbours[1][2]]
        shuffle(targets)
        for target in targets:
            if self.can_destroy_cell(target):
                return target

        return None

    def destroy_random_neighbour(self, neighbours) -> bool:
        destroyed_cell = self.get_random_target(neighbours)

        if destroyed_cell is None:
            return False

        neighbours[1][1].calculated = Void()
        destroyed_cell.calculated = Void()

        return True

    def update(self, neighbours) -> None:
        if not self.movable:
            return

        if self.destroy_random_neighbour(neighbours):
            return

        if self.go_down_then_side(neighbours):
            return
