import pytest
from src.ladder import Ladder
from src.board_square import BoardSquare

@pytest.fixture
def ladder_start_square_10():
    return BoardSquare(10, 1, 10)

@pytest.fixture
def ladder_end_square_20():
    return BoardSquare(20, 2, 2)

@pytest.fixture
def ladder_l1(ladder_start_square_10, ladder_end_square_20):
    return Ladder('L1', ladder_start_square_10, ladder_end_square_20)

def test_ladder_instance(ladder_l1):
    ladder = ladder_l1
    assert isinstance(ladder, Ladder)

def test_ladder_get_id(ladder_l1):
    assert ladder_l1.id == 10

def test_ladder_get_start_square(ladder_li):
    assert ladder_l1.start == ''

def test_ladder_end_before_start(ladder_end_square_20, ladder_start_square_10):
    with pytest.raises(Exception):
        assert Ladder('L1', ladder_end_square_20, ladder_start_square_10)
