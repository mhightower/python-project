from typing import List, Union

from src.board_square import BoardSquare
from src.chute import Chute
from src.exceptions.misconfigure import Misconfigure
from src.ladder import Ladder
from src.game_board_item import GameBoardItem


class GameBoard:

    board_output = []
    board = []
    chute_check = {}
    ladder_check = {}

    def __init__(self, board_output: List[str]):
        self.board_output = board_output
        for index, value in enumerate(board_output):
            index += 1
            if value == '' or value.isnumeric():
                self.board.append(BoardSquare(index, 1, 1))  # TODO Broke
            elif value[0] == 'L':
                list_of_squares = [i for i, square in enumerate(self.board_output) if square == value]
                if len(list_of_squares) == 2:
                    ladder_start = list_of_squares[0] + 1
                    ladder_end = list_of_squares[1] + 1
                    self.board.append(Ladder(index,
                                             value,
                                             BoardSquare(ladder_start, 1, 1),
                                             BoardSquare(ladder_end, 0, 0)
                                            )
                                    )
                else:
                    raise Misconfigure('Miscount of ladder labels: ' + value)
            elif value[0] == 'S':
                list_of_squares = [i for i, square in enumerate(self.board_output) if square == value]
                if len(list_of_squares) == 2:
                    chute_end = list_of_squares[0] + 1
                    chute_start = list_of_squares[1] + 1
                    self.board.append(Chute(index,
                                            value,
                                            BoardSquare(chute_start, 1, 1),
                                            BoardSquare(chute_end, 0, 0)
                                            )
                                     )
                else:
                    raise Misconfigure('Miscount of chute labels')

    def get_square_by_index(self, index: int) -> Union[BoardSquare, GameBoardItem]:
        '''Get BoardSquare or GameBoardItem object using index number'''
        return self.board[index - 1]
    
    def is_ladder_start(self, index: int) -> bool:
        return isinstance(self.board[index - 1], Ladder) and self.board[index - 1].is_start()

    def is_chute_start(self, index: int) -> bool:
        return isinstance(self.board[index - 1], Chute) and self.board[index - 1].is_start()
