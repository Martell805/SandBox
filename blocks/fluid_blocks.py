from random import shuffle, randint

from blocks.solid_blocks import SolidBlock


class FluidBlock(SolidBlock):
    id = 'sb_fluidBlock'
    density = 500
    color = (0, 0, 255)

    def chooseWaySide(self, field):
        ways = [(1, 0), (-1, 0)]
        shuffle(ways)
        neighbours = [field[self.x + ways[0][0]][self.y + ways[0][1]],
                      field[self.x + ways[1][0]][self.y + ways[1][1]]]

        if neighbours[0].density < self.density and neighbours[0].movable:
            return ways[0]
        elif neighbours[1].density < self.density and neighbours[1].movable:
            return ways[1]

        return 0, 0

    def update(self, field):
        if not self.movable:
            return

        way = self.chooseWayDown(field)

        if way == (0, 0):
            way = self.chooseWaySide(field)

        self.updateField(field, way)


class Void(FluidBlock):
    id = 'sb_void'
    density = 0
    color = (55, 55, 55)


class Water(FluidBlock):
    id = 'sb_water'
    density = 1000
    color = (0, 149, 182)


class Oil(FluidBlock):
    id = 'sb_oil'
    density = 800
    color = (0, 0, 0)


class Acid(FluidBlock):
    id = 'sb_acid'
    density = 900
    color = (143, 254, 9)

    def get_random_target(self, field):
        ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        shuffle(ways)
        for way in ways:
            if field[self.x + way[0]][self.y + way[1]].id not in ['sb_void', self.id]:
                return way
        return 0, 0

    def update(self, field):
        destruct_way = self.get_random_target(field)

        if destruct_way != (0, 0) and randint(0, 100) < 5 \
                and field[self.x + destruct_way[0]][self.y + destruct_way[1]].destructible:
            field.set(self.x + destruct_way[0], self.y + destruct_way[1], Void)
            if randint(0, 100) < 20:
                field.set(self.x, self.y, Void)
                return

        if not self.movable:
            return

        way = self.chooseWayDown(field)

        if way == (0, 0):
            way = self.chooseWaySide(field)

        self.updateField(field, way)
