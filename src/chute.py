from src.game_board_item import GameBoardItem
from src.board_square import BoardSquare
from src.exceptions.misconfigure import Misconfigure


class Chute(GameBoardItem):
    '''Represents a chute/snake object on the game board'''
    id: str
    start: BoardSquare
    end: BoardSquare

    def __init__(self, id: str, start: BoardSquare, end: BoardSquare):
        if start.is_after(end):
            self.id = id
            self.start = start
            self.end = end
        else:
            raise Misconfigure('A misconfiguration')

    def get_id(self):
        return self.id
