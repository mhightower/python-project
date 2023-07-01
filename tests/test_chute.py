import pytest
from src.chute import Chute
from src.board_square import BoardSquare
from src.exceptions.misconfigure import Misconfigure


def test_chute_label():
    chute = Chute('S1', BoardSquare(20, 2, 2), BoardSquare(10, 10, 1))
    assert isinstance(chute, Chute)

def test_chute_wrong_way():
    with pytest.raises(Misconfigure):
        Chute('S1', BoardSquare(10, 2, 3), BoardSquare(20, 5, 1))
