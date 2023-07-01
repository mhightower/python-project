import pytest

from src.dice.six_sided_die import six_sided_die

'''TODO For completeness another test should be added to test randomness'''


def test_six_sided_die_int() -> None:
    die = six_sided_die()
    assert isinstance(die.roll(), int)


def test_six_sided_die_between_one_and_six() -> None:
    die = six_sided_die()
    roll = die.roll()
    assert roll <= 6
    assert roll > 0
