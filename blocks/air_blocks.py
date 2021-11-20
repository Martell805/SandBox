from random import shuffle
from blocks.fluid_blocks import FluidBlock


class AirBlock(FluidBlock):
    color = (200, 200, 200)
    density = 100
    id = 'sb_airBlock'

    def chooseWayUp(self, field):
        neighbour = field.get(self.x, self.y + 1)
        if neighbour.density > self.density and neighbour.movable:
            return 0, -1

        ways = [(1, -1), (-1, -1)]
        shuffle(ways)
        neighbours = [field.get(self.x + ways[0][0], self.y + ways[0][1]),
                      field.get(self.x + ways[1][0], self.y + ways[1][1])]

        if neighbours[0].density > self.density and neighbours[0].movable:
            return ways[0]
        elif neighbours[1].density > self.density and neighbours[1].movable:
            return ways[1]

        return 0, 0

    def update(self, field):
        way = self.chooseWayUp(field)

        if way == (0, 0):
            way = self.chooseWaySide(field)

        self.updateField(field, way)
