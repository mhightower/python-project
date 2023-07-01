import pytest

from src.dice.four_sided_die import four_sided_die

'''TODO For completeness another test should be added to test randomness'''


def test_four_sided_die_result_int() -> None:
    die = four_sided_die()
    assert isinstance(die.roll(), int)


def test_four_sided_die_result_between_one_and_four() -> None:
    die = four_sided_die()
    roll = die.roll()
    assert roll <= 4
    assert roll > 0
