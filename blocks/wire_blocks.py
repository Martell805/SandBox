from blocks.default_blocks import Block


class Wire(Block):
    destructible = True
    id = 'sb_wire'
    color = (255, 255, 255)

    def check_for_signals(self, field):
        signal_count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                signal_count += int(isinstance(field[self.x + dx][self.y + dy], Signal))
                if signal_count > 2:
                    return False
        return bool(signal_count)

    def update_wire(self, field):
        if self.check_for_signals(field):
            return Signal
        return None


class Signal(Block):
    destructible = True
    id = 'sb_signal'
    color = (255, 255, 0)

    def update_wire(self, field):
        return SignalTail


class SignalTail(Block):
    destructible = True
    id = 'sb_signalTail'
    color = (255, 0, 0)

    def update_wire(self, field):
        return Wire
