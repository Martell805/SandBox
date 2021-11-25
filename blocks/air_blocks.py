from blocks.fluid_blocks import FluidBlock


class AirBlock(FluidBlock):
    color = (200, 200, 200)
    density = -500
    id = 'sb_airBlock'


class Gas(AirBlock):
    color = (100, 200, 0)
    density = -100
    id = 'sb_gas'
