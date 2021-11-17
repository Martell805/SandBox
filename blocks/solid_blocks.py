from random import shuffle
from blocks.immovable_blocks import Block


class SolidBlock(Block):
    def __init__(self, x, y, tick):
        super().__init__(x, y, tick)
        self.color = (255, 255, 255)
        self.density = 5000
        self.movable = True
        self.id = 'sb_solidBlock'

    def chooseWayDown(self, field):
        neighbour = field.get(self.x, self.y + 1)
        if neighbour.density < self.density and neighbour.movable:
            return 0, 1

        ways = [(1, 1), (-1, 1)]
        shuffle(ways)
        neighbours = [field.get(self.x + ways[0][0], self.y + ways[0][1]),
                      field.get(self.x + ways[1][0], self.y + ways[1][1])]

        if neighbours[0].density < self.density and neighbours[0].movable:
            return ways[0]
        elif neighbours[1].density < self.density and neighbours[1].movable:
            return ways[1]

        return 0, 0

    def updateField(self, field, way):
        if way == (0, 0):
            return

        neighbour = field.get(self.x + way[0], self.y + way[1])
        if self.tick != field.tick and neighbour.tick != field.tick:
            field.set(self.x, self.y, neighbour.__class__)
            field.set(self.x + way[0], self.y + way[1], self.__class__)

    def update(self, field):
        way = self.chooseWayDown(field)

        self.updateField(field, way)


class Void(SolidBlock):
    def __init__(self, x, y, tick):
        super().__init__(x, y, tick)
        self.color = (55, 55, 55)
        self.density = 0
        self.id = 'sb_void'


class Sand(SolidBlock):
    def __init__(self, x, y, tick):
        super().__init__(x, y, tick)
        self.color = (252, 221, 118)
        self.density = 3000
        self.id = 'sb_sand'


class Stone(SolidBlock):
    def __init__(self, x, y, tick):
        super().__init__(x, y, tick)
        self.color = (200, 200, 200)
        self.density = 5000
        self.id = 'sb_stone'
