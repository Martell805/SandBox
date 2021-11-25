from random import shuffle
from blocks.default_blocks import Block


class SolidBlock(Block):
    color = (255, 255, 255)
    density = 5000
    movable = True
    id = 'sb_solidBlock'

    def chooseWayDown(self, field):
        neighbour = field[self.x][self.y + 1]
        if neighbour.density < self.density and neighbour.movable:
            return 0, 1

        ways = [(1, 1), (-1, 1)]
        shuffle(ways)
        neighbours = [field[self.x + ways[0][0]][self.y + ways[0][1]],
                      field[self.x + ways[1][0]][self.y + ways[1][1]]]

        if neighbours[0].density < self.density and neighbours[0].movable:
            return ways[0]
        elif neighbours[1].density < self.density and neighbours[1].movable:
            return ways[1]

        return 0, 0

    def updateField(self, field, way):
        if way == (0, 0):
            return

        neighbour = field[self.x + way[0]][self.y + way[1]]
        if self.tick != field.tick and neighbour.tick != field.tick:
            field.set(self.x, self.y, neighbour.__class__)
            field.set(self.x + way[0], self.y + way[1], self.__class__)

    def update(self, field):
        way = self.chooseWayDown(field)

        self.updateField(field, way)


class Sand(SolidBlock):
    color = (252, 221, 118)
    density = 3000
    id = 'sb_sand'


class Stone(SolidBlock):
    color = (200, 200, 200)
    density = 5000
    id = 'sb_stone'
