from old_blocks.default_blocks import Block
from old_blocks.fluid_blocks import Void
from old_blocks.solid_blocks import SolidBlock


class Wire(Block):
    id = 'sb_wire'
    destructible = True
    color = (255, 255, 255)

    def check_for_electrified(self, field):
        signal_count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                signal_count += int(field[self.x + dx][self.y + dy].electrified)
                if signal_count > 2:
                    return False
        return bool(signal_count)

    def update_wire(self, field):
        if self.check_for_electrified(field):
            return Signal
        return None


class Spark(SolidBlock):
    id = 'sb_spark'
    density = 1
    electrified = True
    color = (255, 255, 0)

    def update(self, field):
        if not self.movable:
            return

        way = self.chooseWayDown(field)

        if way == (0, 0):
            field.set(self.x)

        self.move(field, way)


class Signal(Block):
    id = 'sb_signal'
    destructible = True
    electrified = True
    color = (255, 255, 0)

    def update_wire(self, field):
        return SignalTail


class SignalTail(Block):
    id = 'sb_signalTail'
    destructible = True
    color = (255, 0, 0)

    def update_wire(self, field):
        return Wire


class Detector(Block):
    id = 'sb_detector'
    destructible = False
    color = (100, 100, 100)

    def check_same_neighbours(self, field):
        neighbours = [(self.x, self.y - 1), (self.x + 1, self.y), (self.x - 1, self.y)]
        target_class = field[self.x][self.y + 1].__class__

        if target_class == Void:
            return False

        for neighbour in neighbours:
            if field[neighbour[0]][neighbour[1]].__class__ == target_class:
                return True
        return False

    def update_wire(self, field):
        field[self.x][self.y + 1].lock()

        self.electrified = self.check_same_neighbours(field)
        return None


class Creator(Wire):
    id = 'sb_detector'
    destructible = False
    color = (100, 0, 100)

    def update_wire(self, field):
        field[self.x][self.y - 1].lock()

        return None

    def update(self, field):
        target_class = field[self.x][self.y - 1].__class__
        if target_class != Void and self.check_for_electrified(field) and field[self.x][self.y + 1].destructible:
            field.set(self.x)
