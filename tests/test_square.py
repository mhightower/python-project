import pytest

from src.board_square import BoardSquare


def test_board_square() -> None:
    square = BoardSquare(1)
    assert isinstance(square, BoardSquare)


def test_board_is_after() -> None:
    square = BoardSquare(5)
    assert square.is_after(BoardSquare(1)) == True


def test_board_is_after_false() -> None:
    square = BoardSquare(5)
    assert square.is_after(BoardSquare(10)) == False
