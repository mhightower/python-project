import pytest

from src.board_square import BoardSquare
from src.chute import Chute
from src.exceptions.misconfigure import Misconfigure


@pytest.fixture
def chute_start_square_20():
    return BoardSquare(20)


@pytest.fixture
def chute_end_square_10():
    return BoardSquare(10)


@pytest.fixture
def chute_s1(chute_start_square_20, chute_end_square_10):
    return Chute(chute_start_square_20.index, 'S1', chute_start_square_20, chute_end_square_10)

@pytest.fixture
def chute_s1_end(chute_start_square_20, chute_end_square_10):
    return Chute(chute_end_square_10.index, 'S1', chute_start_square_20, chute_end_square_10)



def test_chute_instance(chute_s1):
    assert isinstance(chute_s1, Chute)


def test_chute_label(chute_s1):
    assert chute_s1.label == 'S1'


def test_chute_get_index(chute_s1):
    assert chute_s1.index == 20


def test_chute_get_start_square(chute_s1):
    assert chute_s1.start.__eq__(chute_start_square_20)

def test_chute_is_start(chute_s1):
    assert chute_s1.is_start()

def test_chute_is_start_false(chute_s1_end):
    assert not chute_s1_end.is_start()

def test_chute_wrong_way(chute_end_square_10, chute_start_square_20):
    with pytest.raises(Misconfigure):
        Chute(10, 'S1', chute_end_square_10, chute_start_square_20)
