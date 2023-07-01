import pytest
from src.game_dice import game_dice
from src.dice.four_sided_die import four_sided_die
from src.dice.six_sided_die import six_sided_die

def test_game_dice_int() -> None:
    dice = game_dice(four_sided_die(), six_sided_die())
    assert isinstance(dice.roll(), int)


def test_four_sided_die_result_between_one_and_four() -> None:
    dice = game_dice(four_sided_die(), six_sided_die())
    roll = dice.roll()
    assert roll <= 10
    assert roll >= 2
