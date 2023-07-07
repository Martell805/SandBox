from blocks.fluid_blocks import FluidBlock
from moves.move import Move
from moves.random_move_set import RMoves
from moves.sequential_move_set import SMoves


class GasBlock(FluidBlock):
    id = 'sb_gas_block'
    density = 50
    durability = 100
    color = (200, 200, 200)

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.check_for_immovable),
            RMoves(
                SMoves(
                    Move(self.go_down_straight),
                    Move(self.go_down_diagonal),
                ),
                Move(self.go_side)
            )
        )


class CarbonicGas(GasBlock):
    id = 'sb_carbonicGas'
    density = 500
    color = (30, 30, 30)


class Gas(GasBlock):
    id = 'sb_gas'
    density = 200
    color = (100, 200, 0)
