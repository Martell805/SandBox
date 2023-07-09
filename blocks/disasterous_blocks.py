from blocks.fluid_blocks import Acid
from cell import Cell
from moves.move import Move
from moves.sequential_move_set import SMoves


class GrayGoo(Acid):
    id = 'sb_gray_goo'
    density = 900
    durability = 5000
    power = 5000
    color = (150, 150, 150)

    def convert_random_neighbour(self, neighbours: list[list[Cell]]) -> bool:
        destroyed_cell = self.get_random_target(neighbours)

        if destroyed_cell is None:
            return False

        destroyed_cell.calculated = self.__class__()

        return True

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.convert_random_neighbour),
        )
