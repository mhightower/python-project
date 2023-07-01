from dataclasses import dataclass


@dataclass(frozen=True)
class BoardSquare:
    '''Represents a game board square'''

    id: int
    coordinate_x: int
    coordinate_y: int

    def is_before(self, other):
        return bool(self.id < other.id)

    def is_after(self, other):
        return bool(self.id > other.id)
