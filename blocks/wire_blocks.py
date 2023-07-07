from blocks.default_blocks import Void, Block
from blocks.solid_blocks import SolidBlock
from cell import Cell
from moves.move import Move
from moves.sequential_move_set import SMoves


class Spark(SolidBlock):
    id = 'sb_spark'
    density = 10
    durability = 10
    electrified = True
    color = (255, 255, 0)

    life_counter = 1

    def kill_if_cant_move(self, neighbours: list[list[Cell]]):
        if self.life_counter == 0:
            neighbours[1][1].calculated = Void()
            return True

        self.life_counter -= 1
        return False

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.check_for_immovable),
            Move(self.go_down_straight),
            Move(self.go_down_diagonal),
            Move(self.kill_if_cant_move)
        )


class Wire(Block):
    id = 'sb_wire'
    durability = 10
    electrified = False
    color = (255, 255, 255)

    def check_for_electrified(self, neighbours: list[list[Cell]]) -> bool:
        four_neighbours = [neighbours[0][1], neighbours[2][1], neighbours[1][0], neighbours[1][2]]
        electrified_neighbour = False

        for neighbour in four_neighbours:
            if hasattr(neighbour.contains, "electrified"):
                electrified_neighbour = electrified_neighbour or neighbour.contains.electrified

        return electrified_neighbour

    def turn_signal(self, neighbours: list[list[Cell]]) -> bool:
        if self.check_for_electrified(neighbours):
            neighbours[1][1].calculated = Signal()
            return True

        return False

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.turn_signal)
        )


class Signal(Block):
    id = 'sb_signal'
    durability = 10
    electrified = True
    color = (255, 255, 0)

    def turn_into_tail(self, neighbours: list[list[Cell]]) -> bool:
        neighbours[1][1].calculated = Tail()

        return True

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.turn_into_tail)
        )


class Tail(Block):
    id = 'sb_tail'
    durability = 10
    electrified = False
    color = (255, 0, 0)

    def turn_into_wire(self, neighbours: list[list[Cell]]) -> bool:
        neighbours[1][1].calculated = Wire()

        return True

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.turn_into_wire)
        )


class InactiveDetector(Block):
    id = 'sb_inactive_detector'
    durability = 10000
    color = (100, 100, 100)
    electrified = False

    def lock_top_block(self, neighbours: list[list[Cell]]) -> bool:
        neighbours[0][1].contains.lock()

        return False

    def detect(self, neighbours: list[list[Cell]]) -> bool:
        detected_block = neighbours[0][1].contains.id

        if (
                detected_block == neighbours[2][1].contains.id or
                detected_block == neighbours[1][0].contains.id or
                detected_block == neighbours[1][2].contains.id
        ):
            neighbours[1][1].calculated = ActiveDetector()
            return True

        return False

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.lock_top_block),
            Move(self.detect)
        )


class ActiveDetector(Block):
    id = 'sb_active_detector'
    color = (200, 200, 200)
    electrified = True

    def turn_inactive(self, neighbours: list[list[Cell]]) -> bool:
        neighbours[1][1].calculated = InactiveDetector()

        return False

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.turn_inactive)
        )


class Creator(Wire, InactiveDetector):
    id = 'sb_creator'
    durability = 10000
    color = (100, 0, 100)
    electrified = False

    def create_if_electrified(self, neighbours: list[list[Cell]]) -> bool:
        detected_block = neighbours[0][1].contains

        if self.check_for_electrified(neighbours):
            neighbours[2][1].calculated = detected_block.__class__()
            return True

        return False

    def init_moves(self) -> None:
        self.moves = SMoves(
            Move(self.lock_top_block),
            Move(self.create_if_electrified)
        )
