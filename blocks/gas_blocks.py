from random import shuffle

from blocks.fluid_blocks import FluidBlock


class GasBlock(FluidBlock):
    id = 'sb_gas_block'
    density = 50
    durability = 100
    color = (200, 200, 200)

    def go_down_or_side(self, neighbours):
        moves = [self.go_down, self.go_side]
        shuffle(moves)

        if moves[0](neighbours):
            return True

        if moves[1](neighbours):
            return True

        return False

    def update(self, neighbours) -> None:
        if not self.movable:
            return

        if self.go_down_or_side(neighbours):
            return


class CarbonicGas(GasBlock):
    id = 'sb_carbonicGas'
    density = 500
    color = (30, 30, 30)


class Gas(GasBlock):
    id = 'sb_gas'
    density = 200
    color = (100, 200, 0)
