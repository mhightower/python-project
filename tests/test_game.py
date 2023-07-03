import pytest

from src.board_config import BoardReader
from src.dice.four_sided_die import four_sided_die
from src.dice.six_sided_die import six_sided_die
from src.game import Game
from src.game_dice import game_dice
from src.player import Player
from src.player_winner import Winner

@pytest.fixture
def player_list():
    return [Player(10), Player(20), Player(30)]

@pytest.fixture
def player_list_plus():
    return [Player(10), Player(20), Player(30), Player(100)]

def test_create_game():
    player01 = Player(10)
    player02 = Player(20)
    player03 = Player(30)
    chutes_and_ladders = Game([player01, player02, player03], game_dice(
        four_sided_die(), six_sided_die()))
    assert isinstance(chutes_and_ladders, Game)


def test_play_game_board1(player_list):
    chutes_and_ladders = Game(player_list, game_dice(
        four_sided_die(), six_sided_die()))
    board_reader = BoardReader('data/boards/board1.csv')
    winner = chutes_and_ladders.play(board_reader.get_board())
    assert isinstance(winner, Winner)

def test_play_game_board1_four_players(player_list_plus):
    chutes_and_ladders = Game(player_list_plus, game_dice(
        four_sided_die(), six_sided_die()))
    board_reader = BoardReader('data/boards/board1.csv')
    winner = chutes_and_ladders.play(board_reader.get_board())
    assert isinstance(winner, Winner)

def test_play_game_board2(player_list):
    chutes_and_ladders = Game(player_list, game_dice(
        four_sided_die(), six_sided_die()))
    board_reader = BoardReader('data/boards/board2.csv')
    winner = chutes_and_ladders.play(board_reader.get_board())
    assert isinstance(winner, Winner)

def test_play_game_board3(player_list):
    chutes_and_ladders = Game(player_list, game_dice(
        four_sided_die(), six_sided_die()))
    board_reader = BoardReader('data/boards/board3.csv')
    winner = chutes_and_ladders.play(board_reader.get_board())
    assert isinstance(winner, Winner)
