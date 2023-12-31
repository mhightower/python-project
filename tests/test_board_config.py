import pytest
from src.board_config import BoardReader
from src.game_board import GameBoard

@pytest.fixture
def board_file_01():
    input_path = 'data/boards/board1.csv'
    return input_path

@pytest.fixture
def board_file_02():
    input_path = 'data/boards/board2.csv'
    return input_path

@pytest.fixture
def board_file_03():
    input_path = 'data/boards/board3.csv'
    return input_path

def test_config_board_read01(board_file_01):
    reader = BoardReader(board_file_01)
    assert isinstance(reader.get_board(), GameBoard)

def test_config_board_read02(board_file_02):
    reader = BoardReader(board_file_02)
    assert isinstance(reader.get_board(), GameBoard)

def test_config_board_read03(board_file_03):
    reader = BoardReader(board_file_03)
    assert isinstance(reader.get_board(), GameBoard)