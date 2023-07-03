from dataclasses import dataclass


@dataclass(frozen=True)
class BoardSquare:
    '''Represents a game board square'''

    index: int

    def is_before(self, other):
        return bool(self.index < other.index)

    def is_after(self, other):
        return bool(self.index > other.index)
