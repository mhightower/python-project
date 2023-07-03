import sys

from src.board_config import BoardReader
from src.dice.four_sided_die import four_sided_die
from src.dice.six_sided_die import six_sided_die
from src.game import Game
from src.game_dice import game_dice
from src.player import Player
from src.exceptions.draw_game import Draw


def main() -> int:
    player01 = Player(10, 'Bob')
    player02 = Player(20, 'Bill')
    player03 = Player(30, 'Beyonce')
    chutes_and_ladders = Game(
        [player01, player02, player03],
        game_dice(four_sided_die(), six_sided_die())
    )
    board_reader = BoardReader('data/boards/board1.csv')
    try:
        winner = chutes_and_ladders.play(board_reader.get_board())
        print('The winner is %s' % winner.name)
    except Draw:
        print('Draw game')
    return 0


if __name__ == '__main__':
    sys.exit(main())
