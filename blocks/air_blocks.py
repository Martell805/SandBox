from blocks.fluid_blocks import FluidBlock


class AirBlock(FluidBlock):
    color = (200, 200, 200)
    density = -100
    id = 'sb_airBlock'


class CarbonicGas(FluidBlock):
    color = (236, 240, 241)
    density = -500
    id = 'sb_carbonicGas'


class Gas(AirBlock):
    color = (100, 200, 0)
    density = -1000
    id = 'sb_gas'
