from typing import List

from src.player import Player
from src.rollable import Rollable
from src.player_winner import Winner
from src.game_board import GameBoard
from src.exceptions.draw_game import Draw


class Game:
    MAX_INDEX = 100
    MAX_ROLLS = 2000
    winner = None
    board: GameBoard

    def __init__(self, players: List[Player], rollable: Rollable) -> None:
        self.players = players
        self.rollable = rollable

    def play(self, board: GameBoard) -> Winner:
        self.board = board
        # Set Players to beginning square
        current_square = dict.fromkeys(self.players, 1)
        self.__a_check = 0
        while True:
            self.__a_check += 1
            for player in self.players:
                player_move = self.rollable.roll()
                new_square = player_move + current_square.get(player)
                if new_square > self.MAX_INDEX:
                    continue
                elif self.board.is_ladder_start(new_square):
                    current_square[player] = self.board.get_square_by_index(
                        new_square
                    ).end.index

                elif self.board.is_chute_start(new_square):
                    current_square[player] = self.board.get_square_by_index(
                        new_square
                    ).end.index
                else:
                    current_square[player] = new_square

                if current_square[player] == self.MAX_INDEX:
                    self.winner = Winner(player)
                    break
            if isinstance(self.winner, Winner):
                break
            if self.__a_check >= self.MAX_ROLLS:
                raise Draw('Game ended in a draw: %s' % current_square.__str__()) 
        return self.winner  # The key that value equals 100
