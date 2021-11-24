from random import shuffle
from blocks.solid_blocks import SolidBlock


class FluidBlock(SolidBlock):
    color = (0, 0, 255)
    density = 500
    id = 'sb_fluidBlock'

    def chooseWaySide(self, field):
        ways = [(1, 0), (-1, 0)]
        shuffle(ways)
        neighbours = [field.get(self.x + ways[0][0], self.y + ways[0][1]),
                      field.get(self.x + ways[1][0], self.y + ways[1][1])]

        if neighbours[0].density < self.density and neighbours[0].movable:
            return ways[0]
        elif neighbours[1].density < self.density and neighbours[1].movable:
            return ways[1]

        return 0, 0

    def update(self, field):
        way = self.chooseWayDown(field)

        if way == (0, 0):
            way = self.chooseWaySide(field)

        self.updateField(field, way)


class Void(FluidBlock):
    color = (55, 55, 55)
    density = 0
    movable = True
    id = 'sb_void'


class Water(FluidBlock):
    color = (0, 149, 182)
    density = 1000
    id = 'sb_water'


class Oil(FluidBlock):
    color = (0, 0, 0)
    density = 800
    id = 'sb_oil'
