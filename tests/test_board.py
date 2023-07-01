import pytest
from src.game_board import GameBoard

@pytest.fixture
def board_instance_empty():
    board_output = []
    return board_output

@pytest.fixture
def board_instance_full():
    board_output = ['L1', '', '', 'L2', '', '6', 'S1', '', 'L3', '', '', '', '', 'L2', '', '', 'S1', '', 'S2', '', 'L4', '', '', 'S3', '', '', '', 'L5', '', 'L3', '', '', '', 'S4', '', '', '', 'L1', '', '', '', 'L4', '', '', '', '', '', '', '', '', 'L6', '', '', 'S4', '', '', '', '', '', 'S5', '', 'S2', '', 'S5', '', '', 'L6', '', '', '', 'L7', '', 'S6', '', 'S7', '', '', '', 'S8', 'L8', '', '', '', 'L5', '', '', 'S3', '', '', '', 'L7', '', 'S6', '', 'S7', '', '', 'S8', 'L8', '']
    return board_output

def test_game_board_instance(board_instance_full):
    game_board = GameBoard(board_instance_full)
    assert isinstance(game_board, GameBoard)

def test_get_square_by_index(board_instance_full):
    game_board = GameBoard(board_instance_full)
    assert game_board.get_square_by_index(1).id == 1
