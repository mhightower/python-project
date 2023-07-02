from typing import List

from src.player import Player
from src.rollable import Rollable
from src.player_winner import Winner
from src.game_board import GameBoard


class Game:
    MAX_INDEX = 100
    winner = None
    board: GameBoard

    def __init__(self, players: List[Player], rollable: Rollable) -> None:
        self.players = players
        self.rollable = rollable

    def play(self, board: GameBoard) -> Winner:
        self.board = board
        # Set Players to beginning square
        current_square = dict.fromkeys(self.players, 1)
        # In a loop
        # foreach  player
        # roll the dice
        # add number to current square to get new square
        # if square 100 this player is the winner game stops
        # if Ladder.start get end square
        #        if square 100 this player is the winner game stops
        # if chute.start get end square
        # go to next player
        while True:
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
        return Winner(self.winner)  # The key that value equals 100
