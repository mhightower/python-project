from typing import List

from src.player import Player
from src.rollable import Rollable
from src.player_winner import Winner
from src.game_board import GameBoard


class Game:
    board: GameBoard
    def __init__(self, players: List[Player], rollable: Rollable) -> None:
        self.players = players
        self.rollable = rollable
    
    def play(self, board: GameBoard) -> Winner:
        self.board = board
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

                self.board.ladder_check(9)

                if ending_square == 100:
                    break
        return Winner(self.players[0])