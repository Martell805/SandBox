from blocks.fluid_blocks import FluidBlock


class AirBlock(FluidBlock):
    id = 'sb_airBlock'
    density = -100
    color = (200, 200, 200)


class CarbonicGas(AirBlock):
    id = 'sb_carbonicGas'
    density = -500
    color = (236, 240, 241)


class Gas(AirBlock):
    id = 'sb_gas'
    density = -1000
    color = (100, 200, 0)
