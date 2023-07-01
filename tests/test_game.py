import pytest
from src.game import Game
from src.player import Player
from src.game_dice import game_dice
from src.dice.four_sided_die import four_sided_die
from src.dice.six_sided_die import six_sided_die
from src.player_winner import Winner
from src.board_config import BoardReader


def test_create_game():
    player01 = Player(10)
    player02 = Player(20)
    player03 = Player(30)
    chutes_and_ladders = Game([player01, player02, player03], game_dice(
        four_sided_die(), six_sided_die()))
    assert isinstance(chutes_and_ladders, Game)

def test_play_game():
    player01 = Player(10)
    player02 = Player(20)
    player03 = Player(30)
    chutes_and_ladders = Game([player01, player02, player03], game_dice(
        four_sided_die(), six_sided_die()))
    board = BoardReader('data/boards/board1.csv')
    winner = chutes_and_ladders.play(board.get_board())
    assert isinstance(winner, Winner)
