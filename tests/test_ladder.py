import pytest
from src.ladder import Ladder
from src.board_square import BoardSquare
from src.exceptions.misconfigure import Misconfigure


@pytest.fixture
def ladder_start_square_10():
    return BoardSquare(10, 1, 10)


@pytest.fixture
def ladder_end_square_20():
    return BoardSquare(20, 2, 2)


@pytest.fixture
def ladder_l1(ladder_start_square_10, ladder_end_square_20):
    return Ladder(ladder_start_square_10.index, 'L1', ladder_start_square_10, ladder_end_square_20)

@pytest.fixture
def ladder_end_l1(ladder_start_square_10, ladder_end_square_20):
    return Ladder(ladder_end_square_20.index, 'L1', ladder_start_square_10, ladder_end_square_20)


def test_ladder_instance(ladder_l1):
    ladder = ladder_l1
    assert isinstance(ladder, Ladder)


def test_ladder_label(ladder_l1):
    assert ladder_l1.label == 'L1'


def test_ladder_get_index(ladder_l1):
    assert ladder_l1.index == 10

def test_ladder_is_start(ladder_l1):
    assert ladder_l1.is_start()

def test_ladder_is_start_false(ladder_end_l1):
    assert not ladder_end_l1.is_start()

def test_ladder_get_start_square(ladder_l1):
    assert ladder_l1.start.__eq__(ladder_start_square_10)


def test_ladder_end_before_start(ladder_end_square_20, ladder_start_square_10):
    with pytest.raises(Misconfigure):
        assert Ladder(ladder_start_square_10.index, 'L1',
                      ladder_end_square_20, ladder_start_square_10)
