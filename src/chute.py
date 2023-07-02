from src.game_board_item import GameBoardItem
from src.board_square import BoardSquare
from src.exceptions.misconfigure import Misconfigure


class Chute(GameBoardItem):
    '''Represents a chute/snake object on the game board'''
    index: int
    start: BoardSquare
    end: BoardSquare

    def __init__(self, index: int, label: str, start: BoardSquare, end: BoardSquare):
        if start.is_after(end):
            self.index = index
            self.label = label
            self.start = start
            self.end = end
        else:
            raise Misconfigure('A misconfiguration')

    def get_label(self):
        return self.label

    def is_start(self) -> bool:
        return self.index == self.start.index
